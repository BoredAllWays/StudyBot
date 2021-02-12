import discord
from discord.ext import commands
import os
import json
bot = commands.Bot(command_prefix="[]")

if __name__ == "__main__":
    for i in os.listdir("cogs"):
        if i.endswith(".py"):
            bot.load_extension(f"cogs.{i[:-3]}")
            print(str(i) + ' is ready')

    with open('./SecretStuff.json') as f:
        data = json.load(f)

    TOKEN = data['BOT TOKEN']

    bot.run(TOKEN)
import discord
from discord.ext import commands
import os
import json
bot = commands.Bot(command_prefix="[]")

if __name__ == "__main__":
    for i in os.listdir("cogs"):
        if i.endswith(".py"):
            bot.load_extension(f"cogs.{i[:-3]}")
            print(str(i) + ' is ready')

    with open('./SecretStuff.json') as f:
        data = json.load(f)

    TOKEN = data['BOT TOKEN']

    bot.run(TOKEN)
