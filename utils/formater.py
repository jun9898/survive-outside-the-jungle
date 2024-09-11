import json


def format_algorithm_info(data):
    try:
        date = data.get("registrationAt", "날짜 정보 없음")
        algorithm_type = data.get("algorithmType", "알 수 없음")
        # 포맷된 문자열 반환
        return f"{date} 알고리즘 타입: {algorithm_type}"
    except json.JSONDecodeError:
        return "올바르지 않은 JSON 형식입니다."
    except KeyError as e:
        return f"필요한 키를 찾을 수 없습니다: {str(e)}"
