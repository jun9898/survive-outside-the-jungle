import discord
from discord.ext import commands
from discord import app_commands
from services.api_service import spring_request

class AutoScheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 슬래시 명령어 등록
    @app_commands.command(name="spring", description="Spring 서버에 요청을 보냅니다.")
    async def request_spring(self, interaction: discord.Interaction):
        response = await spring_request()
        await interaction.response.send_message(f"Spring 서버 응답: {response}")

async def setup(bot):
    await bot.add_cog(AutoScheduler(bot))
