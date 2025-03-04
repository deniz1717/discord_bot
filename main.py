import discord
from bot_mantik import gen_pass
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
gen_pass()

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('meme'))
    with open(f'meme/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("discord bot token")
