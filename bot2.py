import discord
from discord.ext import commands
from main import pswd

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

bot.run("")