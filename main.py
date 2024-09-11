import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from config import PREFIX
from services.api_service import join_server

# .env 파일에서 환경 변수 로드
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Intents 설정
intents = discord.Intents.default()
intents.message_content = True

# 봇 객체 생성
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# 초기 확장 목록
initial_extensions = [
    'cogs.algorithm_setting',
    'cogs.algorithm_routes'
]

@bot.event
async def on_guild_join(guild):
    print("joint guild : ", guild.name, guild.id, )
    data = {
        "guildId": int(guild.id),
        "guildName": guild.name
    }
    await join_server(data)

@bot.event
async def on_ready():
    print('Login...')
    print(f'{bot.user}에 로그인하였습니다.')
    print(f'ID: {bot.user.name}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('VS Code로 개발'))

    # 봇이 참여한 서버 목록 출력
    print("\n참여 중인 서버:")
    for guild in bot.guilds:
        print(f"- {guild.name} (ID: {guild.id})")

    print(f"\n총 {len(bot.guilds)}개의 서버에 연결되어 있습니다.")

    # 슬래시 명령어 등록
    try:
        synced = await bot.tree.sync()  # 명령어 동기화
        print(f"Slash commands synced: {len(synced)} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

async def load_extensions():
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f'Loaded extension: {extension}')
        except Exception as e:
            print(f'Failed to load extension {extension}: {e}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
