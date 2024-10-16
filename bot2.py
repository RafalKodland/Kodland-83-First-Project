import discord
from discord.ext import commands
from main import pswd
import os
import random

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Cześć")

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def haha(ctx, num=2):
    await ctx.send("ha" * num)

@bot.command()
async def password(ctx, len=10):
    await ctx.send(pswd(len))

@bot.command()
async def mem(ctx):
    file = random.choice(os.listdir("memy"))
    with open("memy\\" + file, "rb") as f:
        obrazek = discord.File(f)
    await ctx.send(file=obrazek)


bot.run("")
