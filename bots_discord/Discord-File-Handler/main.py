import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='+', intents=intents)
    
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()

async def mem(ctx):
    
    try:
        with open('xrl/img/a.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send("Lo siento, no se pudo encontrar el archivo.")

bot.run('token')


