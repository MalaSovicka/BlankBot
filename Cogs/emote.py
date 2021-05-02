from discord.ext import commands
class EmoteCog(commands.Cog, name="emote command"):
  def __init__(self, bot:commands.Bot):
    self.bot = bot
  @commands.command(name = "emote",usage="emoji_name emoji_id animated(yes/no)",     description = "Sends the emote.")
  @commands.cooldown(1, 2, commands.BucketType.member)
  async def emote(self, ctx, name: str=None, id: str=None, ani: str=None):
    if ani is not None:
      if ani == "a":
        await ctx.send(f"<a:{name}:{id}>")
      else:
        await ctx.send("Wrong parameter!")
    else:
        await ctx.send(f"<:{name}:{id}>")
def setup(bot:commands.Bot):
  bot.add_cog(EmoteCog(bot))