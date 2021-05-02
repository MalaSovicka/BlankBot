from discord.ext import commands
import os
import sys
class RestartCog(commands.Cog, name="restart command"):
  def __init__(self, bot:commands.Bot):
    self.bot = bot
  @commands.command(hidden=True, name = 'restart')
  @commands.is_owner()
  async def restartBot(self, ctx):
    os.execl(sys.executable, sys.executable, * sys.argv)
def setup(bot:commands.Bot):
  bot.add_cog(RestartCog(bot))