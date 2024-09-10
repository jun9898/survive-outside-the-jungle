from aiohttp import web
from discord.ext import commands
from config import DISCORD_SERVER_HOST, DISCORD_SERVER_PORT
from services.algorithm_service import create_forum_post


class AlgorithmRoutes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.app = web.Application()
        self.app.add_routes([web.post('/today-algorithm', self.handle_algorithm)])
        self.runner = web.AppRunner(self.app)

        # 백그라운드로 aiohttp 서버 실행
        self.bot.loop.create_task(self.start_server())

    async def start_server(self):
        await self.runner.setup()
        site = web.TCPSite(self.runner, DISCORD_SERVER_HOST, DISCORD_SERVER_PORT)
        await site.start()
        print(f'Server running on http://{DISCORD_SERVER_HOST}:{DISCORD_SERVER_PORT}')

    async def handle_algorithm(self, request):
        try:
            data = await request.json()
            if isinstance(data, list):
                for item in data:
                    await create_forum_post(self, item)
            elif isinstance(data, dict):
                await create_forum_post(self, data)
            else:
                raise ValueError("Invalid data format")
            return web.Response(status=200)
        except Exception as e:
            print(f"Error: {e}")
            return web.Response(status=500, text=f"Error processing data: {str(e)}")



async def setup(bot):
    await bot.add_cog(AlgorithmRoutes(bot))
