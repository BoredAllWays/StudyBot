import discord
from discord.ext import commands
import random
import asyncio
import json


def write_json(data, filename="ClassNotes.json"):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


class StudyCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="<Give the command with a subject and you'll get the links>")
    async def study(self, ctx, arg):
        arg = arg.lower()
        studysubjects = {
            'ela': {
                'common lit': 'https://clever.com/oauth/instant-login?client_id=4af59222fbe57cc6ab9d&district_id=527bac1858c5a34a0c0000d0',
                'myhrw': 'https://my.hrw.com/sp/access?sp=hrw&connection=FL-DCPSD-00188779',
                'khan academy-ela': 'https://www.khanacademy.org/ela',
                'MasterClass': 'https://www.masterclass.com/articles/third-person-omniscient-narration-guide',
                'Common Sense': 'https://www.commonsense.org/education/website/826-digital',
                'ELA+Lit youtube playlist': 'https://www.youtube.com/playlist?list=PL8dPuuaLjXtOeEc9ME62zTfqc0h6Pe8vb',
                'Utah Resources': 'https://www.uen.org/7-12interactives/lang_arts.shtml',
                'ELA TPT': 'https://teachingelawithjoy.com/',
                'Big Source': 'https://www.savvas.com/index.cfm?locator=PS2rBh&cmpid=7010W000002LAn1QAG&utm_source=Google&utm_medium=cpc&utm_campaign=7010W000002LAn1QAG&utm_content=myPerspectives&gclid=Cj0KCQiApY6BBhCsARIsAOI_GjY5JSD_s_r_2BjphESJ_2pnvQx76BsB6S1b42ko56JFWnhEXvCnI8IaAmdyEALw_wcB',
                'Poetry': 'https://www.poetryfoundation.org/'
            },
            'math': {
                'algebra nation': 'https://clever.com/oauth/instant-login?client_id=7271c1bc6f814e08724&district_id=527bac1858c5a34a0c0000d0',
                'delta math': 'https://www.deltamath.com/',
                'Geometry Practice': 'https://www.studyguidezone.com/geometry-help.htm',
                'Geometry course free': 'https://www.mathplanet.com/education/geometry',
                'khan academy-geometry': 'https://www.khanacademy.org/math/geometry',
                'geogbra': 'https://www.geogebra.org/',
                'VirtualNerd': 'https://www.virtualnerd.com/middle-math/geometry-measurement/rectangle-perimeter-area/rectangle-perimeter-example',
                'Formula CheetSheet': 'http://www.moomoomath.com/Geometry-Formulas.html',
                'Georgia Geometry': 'http://toolbox2.s3-website-us-west-2.amazonaws.com/accnt_42975/site_42976/Documents/Harrisonanalytgeomstudy070115.pdf',
                'Geometry Worksheets': 'http://www.letspracticegeometry.com/free-geometry-worksheets/'
            },
            'bio': {
                'penda': 'https://clever.com/oauth/instant-login?client_id=6a4a79f457ee2bf81ea3&district_id=527bac1858c5a34a0c0000d0',
                'brain pop': 'https://clever.com/oauth/instant-login?client_id=8bf685529a555fe6bb2e&district_id=527bac1858c5a34a0c0000d0',
                'wtamu.edu': 'https://wtamu.edu/~cbaird/sq/category/biology/',
                'bio interactive': 'https://www.biointeractive.org/',
                'BioJunction': 'http://www.biologyjunction.com/',
                'Bio Corner': 'https://www.biologycorner.com/',
                'Virtual Urchin': 'https://depts.washington.edu/vurchin/?view=main',
                'Nova Labs': 'https://www.pbs.org/wgbh/nova/labs/',
                'Bio Links and Facts': 'https://nabt.org/Resource-Links-General-Biology',
                'Khan Academy-Bio': 'https://www.khanacademy.org/science/biology'
            }
        }

        embedVar = discord.Embed(
            title=f"{arg} resources", description="Click links", color=0x00ff00)
        if arg not in studysubjects:
            return
        for i in studysubjects[arg]:
            embedVar.add_field(
                name=i, value=studysubjects[arg][i], inline=False)
        await ctx.send(embed=embedVar)

    @commands.command(help="<Give the command with a subject and you'll get the links>")
    async def s(self, ctx, arg):
        arg = arg.lower()
        studysubjects = {
            'ela': {
                'common lit': 'https://clever.com/oauth/instant-login?client_id=4af59222fbe57cc6ab9d&district_id=527bac1858c5a34a0c0000d0',
                'myhrw': 'https://my.hrw.com/sp/access?sp=hrw&connection=FL-DCPSD-00188779',
                'khan academy-ela': 'https://www.khanacademy.org/ela',
                'MasterClass': 'https://www.masterclass.com/articles/third-person-omniscient-narration-guide',
                'Common Sense': 'https://www.commonsense.org/education/website/826-digital',
                'ELA+Lit youtube playlist': 'https://www.youtube.com/playlist?list=PL8dPuuaLjXtOeEc9ME62zTfqc0h6Pe8vb',
                'Utah Resources': 'https://www.uen.org/7-12interactives/lang_arts.shtml',
                'ELA TPT': 'https://teachingelawithjoy.com/',
                'Big Source': 'https://www.savvas.com/index.cfm?locator=PS2rBh&cmpid=7010W000002LAn1QAG&utm_source=Google&utm_medium=cpc&utm_campaign=7010W000002LAn1QAG&utm_content=myPerspectives&gclid=Cj0KCQiApY6BBhCsARIsAOI_GjY5JSD_s_r_2BjphESJ_2pnvQx76BsB6S1b42ko56JFWnhEXvCnI8IaAmdyEALw_wcB',
                'Poetry': 'https://www.poetryfoundation.org/'
            },
            'math': {
                'algebra nation': 'https://clever.com/oauth/instant-login?client_id=7271c1bc6f814e08724&district_id=527bac1858c5a34a0c0000d0',
                'delta math': 'https://www.deltamath.com/',
                'Geometry Practice': 'https://www.studyguidezone.com/geometry-help.htm',
                'Geometry course free': 'https://www.mathplanet.com/education/geometry',
                'khan academy-geometry': 'https://www.khanacademy.org/math/geometry',
                'geogbra': 'https://www.geogebra.org/',
                'VirtualNerd': 'https://www.virtualnerd.com/middle-math/geometry-measurement/rectangle-perimeter-area/rectangle-perimeter-example',
                'Formula CheetSheet': 'http://www.moomoomath.com/Geometry-Formulas.html',
                'Georgia Geometry': 'http://toolbox2.s3-website-us-west-2.amazonaws.com/accnt_42975/site_42976/Documents/Harrisonanalytgeomstudy070115.pdf',
                'Geometry Worksheets': 'http://www.letspracticegeometry.com/free-geometry-worksheets/'
            },
            'bio': {
                'penda': 'https://clever.com/oauth/instant-login?client_id=6a4a79f457ee2bf81ea3&district_id=527bac1858c5a34a0c0000d0',
                'brain pop': 'https://clever.com/oauth/instant-login?client_id=8bf685529a555fe6bb2e&district_id=527bac1858c5a34a0c0000d0',
                'wtamu.edu': 'https://wtamu.edu/~cbaird/sq/category/biology/',
                'bio interactive': 'https://www.biointeractive.org/',
                'BioJunction': 'http://www.biologyjunction.com/',
                'Bio Corner': 'https://www.biologycorner.com/',
                'Virtual Urchin': 'https://depts.washington.edu/vurchin/?view=main',
                'Nova Labs': 'https://www.pbs.org/wgbh/nova/labs/',
                'Bio Links and Facts': 'https://nabt.org/Resource-Links-General-Biology',
                'Khan Academy-Bio': 'https://www.khanacademy.org/science/biology'
            }
        }

        embedVar = discord.Embed(
            title=f"{arg} resources", description="Click links", color=0x00ff00)
        if arg not in studysubjects:
            await ctx.send("<NoParameterInDictionaryException: Please enter ela, bio, or math>")
            return
        for i in studysubjects[arg]:
            embedVar.add_field(
                name=i, value=studysubjects[arg][i], inline=False)
        await ctx.send(embed=embedVar)

    @study.error
    async def studyhandler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'arg':
                await ctx.send("<Error: Missing one required argument>")

    @s.error
    async def studyhandler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'arg':
                await ctx.send("<Error: Missing one required argument>")

    @commands.command()
    async def studytips(self, ctx):
        tips = ['take breaks', 'focus', 'dont procrastinate', 'get organized', 'make a study plan',
                'pay atention in class', 'ask questions', 'review notes', 'check resources with !s subject']
        await ctx.send(random.choice(tips))

    @commands.command(help="<Set a time to take breaks before you do an assignment>")
    async def timer(self, ctx, arg, studyafter):
        arg = int(arg)
        arg = arg * 60
        if arg <= 3600:
            await ctx.send(f"Your break starts now for {arg//60} minutes")
            await asyncio.sleep(arg)
            await ctx.send(f"Your break is over {ctx.author.mention}, time to study some {studyafter}")

    @commands.command(help="<please use []add [Ela/Math/Bio/History], [category], ['Term'], ['definition']>")
    async def add(self, ctx, *, args):
        if args.count(', ') != 3:
            await ctx.send("<Not enough commas in your argument>")
            return
        args = args.split(', ')
        classes, category, term, define = args[0], args[1], args[2], args[3]
        classes = classes.lower()
        if classes == 'ela' or classes == 'math' or classes == 'bio' or classes == 'history':
            with open("ClassNotes.json", "r") as json_stuff:
                data1 = json.load(json_stuff)
                temp = data1[classes]
                stuff = {"Term": term, "Definition": define}
                for i in range(0, len(temp)):
                    if category in [*temp][i]:
                        temp1 = temp[i][category]
                        temp1.append(stuff)
            write_json(data1)
            await ctx.send(f"{category} term is added!")
        else:
            await ctx.send("<NoSpecifiedClassException: please use [Ela/Math/Bio/History], [category], [Term], [definition]>")


    @commands.command(help="<Check your study terms for a class>")
    async def check(self, ctx, *, args):
        if args.count(', ') != 1:
            await ctx.send('Comma Error')
            return

        args = args.split(', ')
        subject, cat = args[0], args[1]
        subject = subject.lower()
        if subject == 'ela' or subject == 'math' or subject == 'bio' or subject == 'history':
            embedvar = discord.Embed(
                title=f"{subject} terms", description="Check out these terms and remember to study them", color=discord.Color.blue())
            with open("ClassNotes.json") as data:
                data = json.load(data)
                temp = data[subject]
                for i in range(len(temp)):
                    if cat in temp[i].keys():
                        temp1 = data[subject][i][cat]
                        for x in range(0, len(temp1)):
                            temp2 = temp1[x]
                            embedvar.add_field(name=temp2['Term'], value=temp2["Definition"], inline = False)
                await ctx.send(f"Fetching the terms for {subject}")
                await ctx.send(embed=embedvar)
        else:
            await ctx.send("<NoSpecifiedClassException: please use [Ela/Math/Bio/History], [category], [Term], [definition]>")

    @commands.command(help="<Owner Only Command>")
    async def addsubject(self, ctx, *, args):
        if args.count(', ') != 1:
            await ctx.send("<Comma Error>")
        args.split(', ')
        classes, category = args[0], args[1]
        classes = classes.lower()
        if ctx.message.author.id != 493414999218192386:
            await ctx.send("<NoPermissionError: You are not allowed to user this command>")
            return
        with open("ClassNotes.json") as data:
            data1 = json.load(data)
            temp = data1[classes]
            categorydictionary = {}
            categorydictionary[category] = []
            temp.append(categorydictionary)
        write_json(data1)
        await ctx.send(f"Category {category} is added for {classes}")

    @commands.command()
    async def categories(self, ctx, classes):
        score = 0
        with open("ClassNotes.json") as data:
            data = json.load(data)
            temp = data[classes]
            embedvar = discord.Embed(
                title=f"{classes} categories", description="Categories for stuff", color=discord.Color.blue())
            for i in range(len(data[classes])):
                score+=1
                embedvar.add_field(name = f"Category {score}", value = ''.join(temp[i].keys()), inline = False)
            await ctx.send(embed=embedvar)
            
def setup(bot): bot.add_cog(StudyCommands(bot))
