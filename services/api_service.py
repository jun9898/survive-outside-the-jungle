import aiohttp
from config import SPRING_SERVER_URL

async def spring_request():
    url = SPRING_SERVER_URL + "/bot-test"  # 또는 실제 서버 주소
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return f"Error: {response.status}"
    except Exception as e:
        return f"Connection error: {e}"

async def spring_algorithm_registration(data):
    url = SPRING_SERVER_URL + "/algorithm-registration"  # 또는 실제 서버 주소
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return f"Error: {response.status}"
    except Exception as e:
        return f"Connection error: {e}"

