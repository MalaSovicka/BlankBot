from discord.ext import commands
import json

class HostCog(commands.Cog, name="on voice state update"):
  def __init__(self, bot:commands.Bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_voice_state_update(ctx, member, before, after):
    m = member.voice
    with open('bot_config/whitelist.json') as f:
      whitelist = json.load(f)
    if not member.voice:
      return
    elif m.deaf or m.mute or m.afk or m.requested_to_speak_at or m.self_deaf or m.self_mute or m.self_stream or m.self_video or m.suppress:
      return
    else:
      if member.voice.channel.id == 818118635548704769 and member.id in whitelist:
        for blank in ctx.message.guild.members:
            if blank.top_role.id == 780845111378182144:
              for channel in ctx.guild.voice_channels:
                  if blank in channel.members:
                        return await member.move_to(channel)
      elif member.id not in whitelist:
        return print(f'{member} not whitelisted.')
def setup(bot:commands.Bot):
  bot.add_cog(HostCog(bot))