import asyncio

import discord
from config import load_config
from http_handle.routes import app, client
from middleware.interceptor import Interceptor

intents = discord.Intents.all()
intents.messages = True

config = load_config()


async def run_quart_app():
    await app.run_task(host='0.0.0.0', port=5000)


async def run_discord_client():
    await client.start(config.coze_discord.bot_token)


async def main():
    quart_task = run_quart_app()
    discord_task = run_discord_client()
    await asyncio.gather(quart_task, discord_task)


if __name__ == '__main__':
    interceptor = Interceptor(app)
    interceptor.init_app()
    asyncio.run(main())
