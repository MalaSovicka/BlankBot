import json
from discord.ext import commands
class OnGuildJoinRemoveCog(commands.Cog, name="on guild join/remove"):
  def __init__(self, bot:commands.Bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_guild_join(guild):
      with open('bot_config/prefixes.json', 'r') as f:
          prefixes = json.load(f)
      prefixes[str(guild.id)] = ','
      with open('bot_config/prefixes.json', 'w') as f: 
          json.dump(prefixes, f, indent=4)     
  @commands.Cog.listener()
  async def on_guild_remove(guild): 
      with open('bot_config/prefixes.json', 'r') as f:
          prefixes = json.load(f)
      prefixes.pop(str(guild.id))
      with open('bot_config/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
def setup(bot):
	bot.add_cog(OnGuildJoinRemoveCog(bot))