from discord.ext import commands
import json
class PrefixCog(commands.Cog, name="prefix command"):
  def __init__(self, bot:commands.Bot):
    self.bot = bot
  @commands.command(pass_content=True,name = "prefix",usage="new_prefix",description = "Changes the prefix.")
  @commands.cooldown(1, 2, commands.BucketType.member)
  @commands.has_permissions(administrator=True)
  async def prefix(self, ctx, prefix: str=None):
    if not prefix:
      await ctx.send(f"Current prefix is {ctx.prefix}")
    else:
      with open('bot_config/prefixes.json', 'r') as f:
        prefixes = json.load(f)
      prefixes[str(ctx.guild.id)] = prefix
      with open('bot_config/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
      await ctx.send(f'Prefix changed to: {prefix}')
def setup(bot:commands.Bot):
  bot.add_cog(PrefixCog(bot))