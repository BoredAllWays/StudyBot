import discord
from discord.ext import commands
import random
import asyncio
import json

class Extras(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Gets the owners name")
    async def Get_Owner(self, ctx):
        await ctx.send(ctx.guild.owner)


def setup(bot): bot.add_cog(Extras(bot))