# Imports
import os
from requests_html import HTMLSession
import discord
from dotenv import load_dotenv
from discord import *
from discord.ext import commands, tasks
from discord.ext.commands import Bot

# IP-osoitteen hakemiseen vaadittavat valmistelut
session = HTMLSession()
url = "http://127.0.0.1:4040"
request = session.get(url)
request.html.render(sleep=1, keep_page=True, scrolldown=1)
site_data = request.html.find("a") # Etsitään se osa sivun lähdekoodista, jossa IP-osoite on

# Haetaan IP-osoite lähdekoodista
for item in site_data:
    ip = {
        "tcp": item.text
    }

# Muutetaan IP-osoite merkkijonoksi, jotta sitä voidaan käsitellä
ip = str(ip["tcp"])

# Minecraft-serverin tilaa kontrolloiva muuttuja
server_status = "online"

# Ladataan botin tokeni .env-tiedostosta
load_dotenv()

client = commands.Bot(command_prefix="!")

def get_ip():
    pass

@client.event
async def on_ready():
    print(f"Botti on onlinessa!")

@client.command()
async def set_status():
    pass

@client.command()
async def getip(ctx):
    await ctx.send(f"IP: {ip[6:38]}")
    return

@client.command()
async def apua(ctx):
    await ctx.send(f"Käytettävissä olevat komennot: `!getip`, `!tila`")
    return

@client.command()
async def tila(ctx):
    if server_status == "online":
        await ctx.send("Serveri on päällä.")
        return

    else:
        await ctx.send("Serveri on kiinni.")
        return
  
client.run(os.getenv("DISCORD_TOKEN"))