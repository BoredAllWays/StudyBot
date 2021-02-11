import discord
from discord.ext import commands
import asyncio

questions = {
    "What is the area of a circle with a diameter of 16?\n (a)8pi\n (b)16pi\n (c)64pi\n (d)128pi\n (e)256pi\n": 'b',
    "In a 30-60-90 triangle, the length of the hypotenuse is 6. What is the length of the shortest side?\n (a)2\n (b)3\n (c)12\n (d)4\n": 'b'
}

isused = False


class Questions(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.group(help="<Gives questions for geometry to study>")
    async def geoquiz(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('<Error: No command after []geoquiz>')

    @geoquiz.command()
    async def question(self, ctx):
        for i in questions:
            await ctx.send(i)
            await asyncio.sleep(60)
            global isused
            isused = True

    @geoquiz.command()
    async def answer(self, ctx, arg):
        for i in questions:
            if arg == questions[i] and isused:
                await ctx.send('Correct')


def setup(bot): bot.add_cog(Questions(bot))
