from pymongo import MongoClient
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

def get_database():
    """
    MongoDB 데이터베이스 객체를 반환합니다.
    .env 파일에서 MONGO_URI와 DB_NAME을 읽어옵니다.
    """
    # MongoDB 클라이언트 생성
    client = MongoClient(os.getenv("MONGO_URI"))

    # 데이터베이스 이름 가져오기
    db_name = os.getenv("DB_NAME")
    if not db_name:
        raise ValueError("Database name (DB_NAME) is not set in .env file.")

    # 데이터베이스 반환
    return client[db_name]
