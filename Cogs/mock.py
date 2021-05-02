from discord.ext import commands
import discord
class MockCog(commands.Cog, name="mock command"):
  def __init__(self, bot:commands.Bot):
    self.bot = bot
  @commands.command(name = "mock",usage="user",description = "Moves the mentioned person 69 times.")
  @commands.cooldown(1, 2, commands.BucketType.member)
  async def mock(self, ctx, *, member: discord.Member=None):
    if member == None or member.bot: 
      return await ctx.send("Mention a user.")
    elif not member.voice:
      return await ctx.send("Mentioned user is currently not in a channel.")
    else:
      current_channel = member.voice.channel
      for x in range(2):
        for voice_channel in ctx.guild.voice_channels:
          if not voice_channel.members:
            await member.move_to(voice_channel)
    await member.move_to(current_channel)
def setup(bot:commands.Bot):
  bot.add_cog(MockCog(bot))