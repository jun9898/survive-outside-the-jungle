import discord
from discord.ext import commands
from discord import app_commands
from services import api_service


class ServerRequests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 슬래시 명령어 등록
    @app_commands.command(name="spring", description="Spring 서버에 요청을 보냅니다.")
    async def request_spring(self, interaction: discord.Interaction):
        response = await api_service.spring_request()
        await interaction.response.send_message(f"Spring 서버 응답: {response}")

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
        if not any(role.permissions.administrator for role in interaction.user.roles):
            await interaction.response.send_message("이 명령어를 사용하려면 관리자 권한이 필요합니다.", ephemeral=True)
            return
        data = {
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
        await interaction.response.send_message(f"Spring 서버 응답: {response}")

async def setup(bot):
    await bot.add_cog(ServerRequests(bot))
