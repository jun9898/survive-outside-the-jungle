import json
from datetime import datetime


def format_date(date_str):
    date_obj = datetime.fromisoformat(date_str.rstrip('Z'))  # 'Z'가 있다면 제거
    return date_obj.strftime("%Y년 %m월 %d일 %A")

def format_response(response_json):
    # JSON 문자열을 파이썬 객체로 파싱
    response = json.loads(response_json) if isinstance(response_json, str) else response_json

    if isinstance(response, list):
        formatted_response = []
        for item in response:
            date_str = format_date(item['registrationAt'])
            algo_type = item['algorithmType']
            formatted_response.append(f"{date_str} - 알고리즘 유형: {algo_type}")
        return "\n".join(formatted_response)
    elif isinstance(response, dict):
        date_str = format_date(response['registrationAt'])
        algo_type = response['algorithmType']
        return f"{date_str} - 알고리즘 유형: {algo_type}"
    else:
        return "Invalid response format"
