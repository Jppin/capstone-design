import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langsmith import Client
from database.crud import get_user, get_prescriptions, get_nutrients, get_interactions
from langchain_service.recommendation_algorithm import recommend_supplements_for_user

# .env 파일 로드
load_dotenv()

class LangChainService:
    def __init__(self):
        # API 키 로드
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.langsmith_api_key = os.getenv("LANGSMITH_API_KEY")

        # LLM 초기화
        self.llm = OpenAI(api_key=self.api_key, temperature=0.7)

        # LangSmith 클라이언트 초기화
        self.langsmith_client = Client(api_key=self.langsmith_api_key)

    def generate_response(self, prompt: str) -> str:
        """
        LLM을 사용하여 프롬프트에 대한 응답 생성
        """
        return self.llm.invoke(prompt)

    def generate_recommendations(self, user_id: str) -> dict:
        try:
            user = get_user(user_id)
            prescriptions = list(get_prescriptions(user_id))
            nutrients = list(get_nutrients())
            interactions = list(get_interactions())

            print(f"User data: {user}")
            print(f"Prescriptions: {prescriptions}")
            print(f"Nutrients: {nutrients}")
            print(f"Interactions: {interactions}")

            recommendations = recommend_supplements_for_user(user, prescriptions, nutrients, interactions)

            print(f"Generated recommendations: {recommendations}")

            if not recommendations:
                raise ValueError("No recommendations generated.")

            prompt = self.create_prompt(user, recommendations)
            response = self.generate_response(prompt)

            print(f"LLM Response: {response}")

            return {
                "recommendations": recommendations,
                "message": response
            }

        except Exception as e:
            print(f"Error in generate_recommendations: {e}")
            raise e


    def create_prompt(self, user: dict, recommendations: list) -> str:
        """
        추천 결과를 기반으로 자연어 프롬프트 생성
        """
        prompt = f"User: {user['name']} (Age: {user['age']}, Gender: {user['gender']})\n\n"
        prompt += "Recommendations:\n"
        for rec in recommendations:
            prompt += f"- {rec['name']}: {rec['reason']} (Dosage: {rec['dosage']})\n"
        prompt += "\nGenerate a friendly response to guide the user about these supplements."
        return prompt

    def log_to_langsmith(self, user_id: str, prompt: str, response: str):
        """
        LangSmith에 요청과 응답을 로깅
        """
        self.langsmith_client.log(
            user_id=user_id,
            request={"prompt": prompt},
            response={"message": response}
        )
