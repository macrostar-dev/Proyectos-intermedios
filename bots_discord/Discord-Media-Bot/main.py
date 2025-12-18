import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='°', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def mem(ctx):
    try:
            # Obtener la lista de nombres de archivos de imágenes disponibles en el directorio 'images'
        image_files = os.listdir('img')
                # Construir la ruta del archivo
        file_path = os.path.join('img', random.choice(image_files))
            # Abrir y enviar el archivo seleccionado
        with open(file_path, 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send("Lo siento, no se pudo encontrar el archivo.")

bot.run('token')

