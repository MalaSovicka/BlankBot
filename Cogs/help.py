import discord
from discord.ext import commands
from random import randint
class HelpCog(commands.Cog, name="help command"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name="help",usage="commandName",description="Display the help message.", aliases=["tasukete"])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def help(self, ctx, commandName: str = None):
        if commandName is not None:
          check = False
          stop = False
          for command in self.bot.commands:
            if commandName.lower() == command.name:
                commandName = command
                check = True
                break
            else:
              for aliase in command.aliases:
                if commandName.lower() == aliase:
                      commandName = command
                      check = True
                      stop = True
                      break
              if stop == True:
                break
          if check ==True:
            command = self.bot.commands
            embed = discord.Embed(title=f"**{commandName.name.upper()} COMMAND:**",    description=f"{commandName.description}",color=randint(0, 0xffffff))

            embed.set_thumbnail(url=f'{self.bot.user.avatar_url}')

            embed.add_field(name=f"**NAME :**",value=f"{commandName.name}",inline=False)

            aliases = f"{commandName.aliases}"

            embed.add_field(name=f"**ALIASES :**",
                          value=f"{aliases}",
                          inline=False)
            embed.add_field(
              name=f"**USAGE :**",
              value=
              f"{ctx.prefix}{commandName.name} {commandName.usage}",
              inline=False)

            embed.add_field(name=f"**DESCRIPTION :**",
                          value=f"{commandName.description}",
                          inline=False)
            await ctx.channel.send(embed=embed)
          else:
            await ctx.send("Tak seš úplnej čurák?!")
        else:
            embed = discord.Embed(
                title=f"__**Help page of {self.bot.user.name}**__",
                description=f"**{ctx.prefix}help (command)** : Display the help list or the help data for a specific command.",
                color=randint(0, 0xffffff))
            embed.set_thumbnail(url=f'{self.bot.user.avatar_url}')
            _value = ""
            for i in self.bot.commands:
              _value += f"**{ctx.prefix}{i} <{i.usage}>** : {i.description}\n"
            embed.add_field(
               name=f"__COMMANDS:__",
               value=_value,
                 inline=False)
            await ctx.channel.send(embed=embed)
def setup(bot: commands.Bot):
    bot.remove_command("help")
    bot.add_cog(HelpCog(bot))