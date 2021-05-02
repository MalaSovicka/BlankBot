from discord.ext import commands
import discord
import youtube_dl
import os

class PlayCog(commands.Cog, name="play command"):
  def __init__(self, bot:commands.Bot):
    self.bot = bot
  @commands.command(name = "play",usage="url",     description = "Plays the music from your url link.")
  @commands.cooldown(1, 2, commands.BucketType.member)
  async def play(self, ctx, url : str):
    song_there = 
    channel = ctx.message.author.voice.voice_channel
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
      await voiceChannel.connect()

  @commands.command(name = "stop",usage="",description = "Stops the music.")
  @commands.cooldown(1, 2, commands.BucketType.member)
  async def stop(ctx,self):
    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    await voice.stop() if voice.is_playing() else await ctx.send("No audio currently playing.")
  @commands.command(name = "resume",usage="",description = "Resumes the music.")
  @commands.cooldown(1, 2, commands.BucketType.member)
  async def resume(ctx,self):
    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    await voice.resume() if voice.is_paused() else await ctx.send("The audio is not paused")
  @commands.command(name = "pause",usage="",description = "Pauses the music.")
  @commands.cooldown(1, 2, commands.BucketType.member)
  async def pause(ctx,self):
    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    await voice.pause() if voice.is_playing() else await ctx.send("Currently no audio playing.")
    @commands.command(name = "leave",usage="",description = "Leaves the voice channel.")
  @commands.cooldown(1, 2, commands.BucketType.member)
  async def leave(self,ctx):
    if (ctx.voice_client):
      await ctx.guild.voice_client.disconnect()
      message = await ctx.send('Sorry to bother you.')
      time.sleep(2)
      await message.delete()
    else:
       message = await ctx.send("I am not connected to the voice channel.")
       time.sleep(2)
       await message.delete()
    await ctx.message.delete()
      
        
def setup(bot:commands.Bot):
  bot.add_cog(StopCog(bot))
    
def setup(bot:commands.Bot):
  bot.add_cog(PlayCog(bot))