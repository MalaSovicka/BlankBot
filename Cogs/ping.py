from discord.ext import commands
class PingCog(commands.Cog, name="ping command"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot     
	@commands.command(name = "ping",
					description = "Display the bot's ping.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def ping(self, ctx):
		await ctx.send(content=f"🏓 Pong !  `{round(self.bot.latency * 1000)} ms`")
def setup(bot:commands.Bot):
	bot.add_cog(PingCog(bot))