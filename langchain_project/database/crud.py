from bson.objectid import ObjectId
from database.db_connection import get_database

# 데이터베이스 객체 가져오기
db = get_database()

def get_collection(collection_name):
    """
    컬렉션 객체를 반환합니다.
    """
    return db[collection_name]

# 모든 사용자 이름 가져오기
def get_all_user_names():
    """
    모든 사용자의 이름과 ID를 가져옵니다.
    """
    collection = get_collection("Ex_userprofiles")
    users = list(collection.find({}, {"name": 1, "_id": 1}))  # 이름과 _id만 반환
    if not users:
        raise ValueError("No users found in the database.")
    return users

# 특정 사용자 정보 가져오기
def get_user(user_id):
    """
    특정 사용자의 프로필 데이터를 가져옵니다.
    """
    collection = get_collection("Ex_userprofiles")
    user = collection.find_one({"_id": ObjectId(user_id)})  # ObjectId로 변환
    if not user:
        raise ValueError(f"User with ID {user_id} not found.")
    return user

# 처방 데이터 가져오기
def get_prescriptions(user_id):
    """
    특정 사용자의 처방 데이터를 반환합니다.
    """
    collection = get_collection("Ex_prescriptions")
    prescriptions = list(collection.find({"user_id": ObjectId(user_id)}))
    if not prescriptions:
        raise ValueError(f"No prescriptions found for user ID {user_id}.")
    return prescriptions

# 영양소 데이터 가져오기
def get_nutrients():
    """
    모든 영양소 데이터를 반환합니다.
    """
    collection = get_collection("Ex_nutrients")
    nutrients = list(collection.find())
    if not nutrients:
        raise ValueError("No nutrients found in the collection.")
    return nutrients

# 상호작용 데이터 가져오기
def get_interactions():
    """
    모든 상호작용 데이터를 반환합니다.
    """
    collection = get_collection("Ex_interactions")
    interactions = list(collection.find())
    if not interactions:
        raise ValueError("No interactions found in the collection.")
    return interactions

# 로그 저장
def save_to_custom_logs(log_data):
    """
    custom_logs 컬렉션에 로그 데이터를 저장합니다.
    """
    collection = get_collection("custom_logs")
    result = collection.insert_one(log_data)
    return result.inserted_id
