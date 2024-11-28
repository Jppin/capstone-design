import streamlit as st
from database.crud import get_all_user_names, get_user, save_to_custom_logs
from langchain_service.openai_integration import LangChainService
from datetime import datetime

def show():
    st.title("Personalized LangChain Demo")

    # 사용자 선택
    st.subheader("Select a User")

    # 모든 사용자 목록 가져오기
    try:
        users = get_all_user_names()
    except Exception as e:
        st.error(f"Error fetching users: {e}")
        return

    # 사용자 이름 목록 생성
    user_names = [f"{user['name']} ({user['_id']})" for user in users]
    selected_user_index = st.selectbox("Choose a user:", range(len(users)), format_func=lambda idx: user_names[idx])

    # 선택된 사용자의 ObjectId 가져오기
    selected_user_id = users[selected_user_index]["_id"]

    # 사용자 프로필 데이터 가져오기
    try:
        user_profile = get_user(str(selected_user_id))
    except Exception as e:
        st.error(f"Error fetching user profile: {e}")
        return

    if user_profile:
        # 사용자 데이터 표시
        st.write(f"**Name**: {user_profile['name']}")
        st.write(f"**Age**: {user_profile['age']}")
        st.write(f"**Gender**: {user_profile['gender']}")
        st.write(f"**Health Interests**: {', '.join(user_profile['health_interests'])}")

        # LangChain 서비스 초기화
        service = LangChainService()

        # 추천 로직 실행
        st.subheader("Personalized Recommendations")
        try:
            recommendations_data = service.generate_recommendations(str(selected_user_id))
            if "recommendations" in recommendations_data and recommendations_data["recommendations"]:
                recommendations = recommendations_data["recommendations"]
                st.write("### Recommended Supplements:")
                for rec in recommendations:
                    st.write(f"- **{rec['name']}**")
                    st.write(f"  - **Reason**: {rec['reason']}")
                    st.write(f"  - **Dosage**: {rec.get('dosage', 'No dosage info available')}")
                    st.write(f"  - **Precautions**: {', '.join(rec.get('precautions', ['None']))}")
                    st.write("---")
                if "message" in recommendations_data:
                    st.write("### Summary Message:")
                    st.write(recommendations_data["message"])
            else:
                st.warning("No recommendations could be generated for this user.")

        except Exception as e:
            st.error(f"Error generating recommendations: {e}")