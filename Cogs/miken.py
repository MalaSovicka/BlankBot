from discord.ext import commands
import discord.ext
import discord
import time
class MikenCog(commands.Cog, name="miken command"):
  def __init__(self, bot:commands.Bot):
    self.bot = bot
  @commands.command(name = "miken",usage="",     description = "Joins voice channel you are currently in and plays 'Miken hejtí holky'.")
  @commands.cooldown(1, 2, commands.BucketType.member)
  async def miken(self, ctx):
    try:
      voice_channel = ctx.message.author.voice.channel
      vc = await voice_channel.connect()
      vc.play(discord.FFmpegPCMAudio(source="sounds/miken.mp3"))
      while vc.is_playing():
        time.sleep(1)
      await vc.disconnect()
    except:
        message = await ctx.send(f"You are not in the channel {ctx.author.name}")
        time.sleep(2)
        await message.delete()
    finally:
      await ctx.message.delete()
def setup(bot:commands.Bot):
  bot.add_cog(MikenCog(bot))