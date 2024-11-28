def recommend_supplements_for_user(user, prescriptions, nutrients, interactions):
    recommendations = []

    # Step 1: 건강 관심사 매칭
    for nutrient in nutrients:
        if 'functions' in nutrient:
            matched_interests = [
                interest for interest in user.get('health_interests', [])
                if any(interest in nutrient['functions'] for interest in interest.split())
            ]
            if matched_interests:
                recommendations.append({
                    'name': nutrient['name'],
                    'reason': f"Aligned with health interests: {', '.join(matched_interests)}",
                    'priority': 2,
                    'precautions': nutrient.get('conflicting_medications', []),
                    'dosage': nutrient.get('recommended_dosage', "No dosage info available")
                })

    # Step 2: 과거 병력 매칭
    synonyms = {
        "Hypertension": ["Cardiovascular Health"],
        "Asthma": ["Lung Health"]
    }
    for condition in user.get('past_history', []):
        for nutrient in nutrients:
            if 'functions' in nutrient:
                if condition in nutrient['functions'] or any(syn in nutrient['functions'] for syn in synonyms.get(condition, [])):
                    recommendations.append({
                        'name': nutrient['name'],
                        'reason': f"Addresses past condition: {condition}",
                        'priority': 1,
                        'precautions': nutrient.get('conflicting_medications', []),
                        'dosage': nutrient.get('recommended_dosage', "No dosage info available")
                    })

    # Step 3: 상호작용 필터링
    for prescription in prescriptions:
        for medication in prescription.get('medications', []):
            for rec in recommendations:
                if any(medication['name'] == interaction['source'] and rec['name'] == interaction['target']
                       for interaction in interactions):
                    rec['priority'] = -1  # 상호작용 발생 시 제외

    # Step 4: 추천 결과 정리
    recommendations = [rec for rec in recommendations if rec['priority'] > 0]
    recommendations.sort(key=lambda x: -x['priority'])

    return recommendations
