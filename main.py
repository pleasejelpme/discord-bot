import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger('bot')

def run():
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

    @bot.event
    async def on_ready():
        print('Dundler Mifflin bot running!')
        logger.info(f'user: {bot.user} (ID: {bot.user.id})')

    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == '__main__':
    run()