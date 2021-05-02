from discord.ext import commands
import json
import discord
from random import randint
class WhitelistCog(commands.Cog, name="whitelist"):
  def __init__(self, bot:commands.Bot):
    self.bot = bot
  @commands.cooldown(1, 2, commands.BucketType.member)
  @commands.command()
  @commands.is_owner()
  async def whitelist(self,ctx,member: discord.Member=None, rem: str=None):
    with open('bot_config/whitelist.json') as f:
        whitelist = json.load(f)
    users = whitelist["users"]
    allMemberIds = [mbr["id"] for mbr in users]
    if member and member.id not in allMemberIds and not rem:
      users.append({"name":member.name,"id":member.id})
      with open('bot_config/whitelist.json', 'w') as f: 
        json.dump(whitelist, f, indent=4)     
    elif not rem:
      embed = discord.Embed(title="**WHITELISTED USERS:**",description="All whitelisted users",color=randint(0, 0xffffff))
      value = ""
      for user in users:
        value += f"{user['name']}\n"
      embed.add_field(name="Names",value=value,inline=False)
      await ctx.send(embed=embed)
    elif rem == 'r' or 'rem' or 'remove':
      i=-1
      for id in allMemberIds:
        i+=1
        if member.id == id:
          users.pop(i)
          with open('bot_config/whitelist.json', 'w') as f: 
            json.dump(whitelist, f, indent=4) 
def setup(bot:commands.Bot):
  bot.add_cog(WhitelistCog(bot))