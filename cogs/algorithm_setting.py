import json

import discord
from discord import app_commands, Interaction
from discord.ext import commands

from services import api_service
from services.algorithm_service import create_forum_post
from utils.formater import format_algorithm_info


def check_admin_permissions(user):
    return any(role.permissions.administrator for role in user.roles)

async def check_and_respond(self, interaction: Interaction):
    if not check_admin_permissions(interaction.user):
        await interaction.response.send_message("이 명령어를 사용하려면 관리자 권한이 필요합니다.", ephemeral=True)
        return False
    return True

class AlgorithmSetting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # 슬래시 명령어 등록
    @app_commands.command(name="spring", description="Spring 서버에 요청을 보냅니다.")
    async def request_spring(self, interaction: discord.Interaction):
        response = await api_service.spring_request()
        await interaction.response.send_message(f"Spring 서버 응답: {response}")

    @app_commands.command(name="set_algorithm_forum", description="자동으로 algorithm 유형을 게시할 포럼을 지정합니다.")
    @app_commands.describe(forum_id="forum id를 입력해주세요.")
    async def set_algorithm_forum(self, interaction: discord.Interaction, forum_id: str):
        if not check_and_respond(interaction.user):
            return
        guild_id = int(interaction.guild_id)
        forum_id = str(forum_id)
        data = {
            "guildId": guild_id,
            "forumId": forum_id
        }
        response = await api_service.set_algorithm_forum(data)
        await interaction.response.send_message(f"{response}")


    @app_commands.command(name="algorithm", description="한 주간 알고리즘 유형을 입력 받습니다.")
    @app_commands.describe(
        mon="월요일에 대한 정보",
        tue="화요일에 대한 정보",
        wed="수요일에 대한 정보",
        thu="목요일에 대한 정보",
        fri="금요일에 대한 정보",
        sat="토요일에 대한 정보",
        sun="일요일에 대한 정보"
    )
    async def algorithm_registration(
        self,
        interaction: discord.Interaction,
        mon: str, tue: str, wed: str, thu: str, fri: str, sat: str, sun: str
    ):
        # 관리자 권한 검사
        if not check_and_respond(interaction.user):
            return
        guild_id = int(interaction.guild_id)
        data = {
            "guildInfoId": guild_id,
            "mon": mon,
            "tue": tue,
            "wed": wed,
            "thu": thu,
            "fri": fri,
            "sat": sat,
            "sun": sun
        }
        print(data)
        response = await api_service.spring_algorithm_registration(data)
        await interaction.response.send_message(f"{response}")

    @app_commands.command(name="get_weekly_algorithms", description="이번주 알고리즘 유형을 가져옵니다.")
    async def get_weekly_algorithms(self, interaction):
        guild_id = int(interaction.guild_id)
        response = await api_service.get_weekly_algorithms(guild_id)
        response = json.loads(response)
        algorithm_info = ""
        for i in response:
            algorithm_info += f"{format_algorithm_info(i)}\n"
        await interaction.response.send_message(f"이번 주 알고리즘:\n{algorithm_info}")

    @app_commands.command(name="get_today_algorithm", description="오늘 알고리즘 유형을 가져와 포스팅합니다.")
    async def get_today_algorithm(self, interaction: discord.Interaction):
        guild_id = int(interaction.guild_id)
        response = await api_service.get_today_algorithm(guild_id)
        print(response)
        response_dict = json.loads(response)
        algorithm_info = format_algorithm_info(response_dict)
        await create_forum_post(self, response_dict)
        await interaction.response.send_message(f"오늘의 알고리즘:\n{algorithm_info}")

async def setup(bot):
    await bot.add_cog(AlgorithmSetting(bot))
