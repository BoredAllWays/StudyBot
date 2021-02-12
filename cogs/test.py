import discord
from discord.ext import commands

class test(commands.Cog):
    def _init__(self, bot):
        self.bot = bot
    @commands.command()
    async def test(self, ctx, *, args):
        args = args.split(', ')
        v1, v2, v3 = args[0], args[1], args[2]
        await ctx.send(f"v1: {v1} v2: {v2}, v3: {v3}")
        a =  {
            'yes': {
                'no' : {
                    'bye' : 'lol'
                }
            }
        }
        await ctx.send(a[str(v1)][str(v2)][str(v3)])

def setup(bot): bot.add_cog(test(bot))