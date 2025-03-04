import discord
from bot_mantik import gen_pass
from discord.ext import commands
import os
import random

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
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