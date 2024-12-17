from services.graph_service import graph

def main():
    """
    LangChain RAG 애플리케이션 실행.
    """
    initial_state = {"question": "이영훈"}  # 사용자 이름 입력
    result = graph.invoke(initial_state)
    
    print(f"Context: {result['context']}\n")
    print(f"Answer: {result['answer']}")

if __name__ == "__main__":
    main()
