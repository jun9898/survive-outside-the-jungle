from discord.ext import commands, tasks
from aiohttp import web

from config import DISCORD_SERVER_HOST, DISCORD_SERVER_PORT


class AlgorithmRoutes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.app = web.Application()
        self.app.add_routes([web.post('/algorithm', self.handle_algorithm)])
        self.runner = web.AppRunner(self.app)

        # 백그라운드로 aiohttp 서버 실행
        self.bot.loop.create_task(self.start_server())

    async def start_server(self):
        await self.runner.setup()
        site = web.TCPSite(self.runner, DISCORD_SERVER_HOST, DISCORD_SERVER_PORT)
        await site.start()

    async def handle_algorithm(self, request):
        try:
            data = await request.json()
            forum_id = data.get('forum_id')
            mon = data.get('mon')
            tue = data.get('tue')
            wed = data.get('wed')
            thu = data.get('thu')
            fri = data.get('fri')
            sat = data.get('sat')
            sun = data.get('sun')

            # 여기서 받은 데이터를 원하는 대로 처리할 수 있습니다.
            print(f"Received data for guild {forum_id}: {data}")

            # 데이터를 Discord에서 처리하고 응답을 보냅니다.
            # 필요한 경우 서버에서 특정 채널에 메시지를 보낼 수도 있습니다.

            return web.Response(text="Algorithm data received successfully.")
        except Exception as e:
            print(f"Error: {e}")
            return web.Response(status=500, text="Error processing data")

async def setup(bot):
    await bot.add_cog(AlgorithmRoutes(bot))

