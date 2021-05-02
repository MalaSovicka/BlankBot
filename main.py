import discord
from discord.ext import commands
import json
import os
from alive import keep_alive

class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None


async def get_prefix(ctx, message):
   if not message.guild:
     return ','
   else:
    with open('bot_config/prefixes.json', 'r') as f:
      prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = (get_prefix), case_insensitive=True,intents = intents, fetch_offline_members = True)


@bot.event
async def on_ready():
  print(f"We have logged in as {bot.user}")
  print(discord.__version__)

if __name__ == '__main__':
  for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
      bot.load_extension(f"Cogs.{filename[:-3]}")
  keep_alive()
  bot.run(os.environ['TOKEN'])