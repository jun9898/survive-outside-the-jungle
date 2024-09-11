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

async def join_server(data):
    print(data)
    print("join-server : ", data)
    url = SPRING_SERVER_URL + "/join-server"  # 또는 실제 서버 주소
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    print(f"Successfully registered guild {data['guild_id']} with the server.")
                else:
                    print(f"Failed to register guild {data['guild_id']}. Server responded with status {response.status}")
    except Exception as e:
        print(f"An error occurred while trying to register guild {data['guild_id']}: {str(e)}")

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


async def set_algorithm_forum(data):
    url = SPRING_SERVER_URL + "/set-algorithm-forum"  # 또는 실제 서버 주소
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return f"Error: {response.text()}"
    except Exception as e:
        return f"Connection error: {e}"


async def get_weekly_algorithms(guild_info_id):
    url = SPRING_SERVER_URL + "/weekly-algorithms"  # 또는 실제 서버 주소
    params = {'guildInfoId': guild_info_id}  # 수정된 파라미터 이름
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return f"Error: {await response.text()}"
    except Exception as e:
        return f"Connection error: {e}"


async def get_today_algorithm(guild_info_id):
    url = SPRING_SERVER_URL + "/today-algorithm"  # 또는 실제 서버 주소
    params = {'guildInfoId': guild_info_id}  # 수정된 파라미터 이름
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return f"Error: {await response.text()}"
    except Exception as e:
        return f"Connection error: {e}"