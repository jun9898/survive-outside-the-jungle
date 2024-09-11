import discord


async def create_forum_post(self, item):
    guild_info_id = item["guildInfoId"]
    registration_at = item["registrationAt"]
    algorithm_type = item["algorithmType"]
    algorithm_forum_id = item["algorithmForumId"]

    print("item : ", item)

    # 날짜 포맷팅

    # 제목과 내용 생성
    title = f"{registration_at} 알고리즘 유형 : {algorithm_type}"
    content = f"{algorithm_type}에 해당하는 알고리즘 문제를 풀고 인증해주세요."

    # 포럼 채널에서 스레드 생성
    forum = self.bot.get_guild(int(guild_info_id)).get_channel(int(algorithm_forum_id))
    if isinstance(forum, discord.ForumChannel):
        await forum.create_thread(name=title, content=content)
    else:
        print(f"Channel with ID {algorithm_forum_id} is not a forum channel.")



