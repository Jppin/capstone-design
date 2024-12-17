from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from services.vector_service import init_vector_store
from services.user_service import get_user_info_byname
from utils.prompt_template import format_prompt
from config.config import llm
from langgraph.graph import START, StateGraph

# State 정의
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

# 벡터 스토어 초기화
vector_store = init_vector_store(collection_name="Supplement_Info", index_name="vector_index")

# Retrieve 단계
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

def generate(state: State):
    # 유저 정보 가져오기
    user_name = state["question"]
    user_info = get_user_info_byname(user_name)

    if not user_info:
        return {"answer": f"User '{user_name}' not found in the database."}

    # Retrieved Context 내용
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])

    # 프롬프트 포맷팅
    input_data = format_prompt(user_info, docs_content)

    # 딕셔너리를 문자열로 변환
    formatted_prompt = f"""
    사용자 이름: {input_data['name']}
    나이: {input_data['age']}
    성별: {input_data['gender']}
    건강 관심사: {input_data['health_interests']}
    과거 병력: {input_data['past_history']}
    현재 복용 중인 약물: {input_data['current_medications']}

    제공된 정보:
    {input_data['context']}
    """

    # LLM 실행
    response = llm.invoke(formatted_prompt)
    return {"answer": response}


# LangGraph 워크플로우 설정
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()
