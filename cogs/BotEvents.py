import discord
from discord.ext import commands


class BotEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.voice is None:
            channel = self.bot.get_channel(808464495802056794)
            await channel.send(f"{member.name} is finally done talking,  hopefully they'll study now")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} is online")
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="AniistheGOAT procrastinate"))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return


def setup(bot): bot.add_cog(BotEvents(bot))
