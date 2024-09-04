import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Intents 설정
intents = discord.Intents.default()
intents.message_content = True  # 메시지 콘텐츠에 접근하기 위해 이 옵션을 활성화

client = commands.Bot(command_prefix='./', intents=intents)

@client.event
async def on_ready():
    print('Login...')
    print(f'{client.user}에 로그인하였습니다.')
    print(f'ID: {client.user.name}')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('VS Code로 개발'))

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('태욱'):
        await message.channel.send("{} : 태욱이는 진짜 잘생김!".format(message.author))

    # "테스트"로 시작하는 메시지에 응답
    if message.content.startswith('테스트'):
        await message.channel.send("{} | {}, 안녕!".format(message.author, message.author.mention))

    # 메시지가 정확히 "테스트"인 경우 응답
    if message.content == '테스트':
        await message.channel.send("{} | {}, 어서오세요!".format(message.author, message.author.mention))

    # 명령어 핸들러가 제대로 동작하도록 메시지 처리
    await client.process_commands(message)

@client.command(aliases=['hi'])
async def hello(ctx):
    await ctx.send("안녕하세요!")

@client.command(aliases=['로그인', '접속하기'])
async def login(ctx):
    await ctx.channel.send("{} | {}님, 어서오세요!".format(ctx.author, ctx.author.mention))

client.run(DISCORD_TOKEN)
