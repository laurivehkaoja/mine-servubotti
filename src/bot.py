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

# Minecraft-serverin tilaa kontrolloiva muuttuja
server_status = "online"

# Metodit
def get_ip():
    for item in site_data:
        raw_ip = {
            "tcp": item.text
        }
    return raw_ip

def format_ip():
    ip = get_ip()
    ip = str(ip["tcp"])
    return ip[6:38]

# Ladataan botin tokeni .env-tiedostosta
load_dotenv()

# Määritetään botin prefixiski huutomerkki
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print(f"Botti on onlinessa!")

@client.command()
async def set_status(ctx):
        pass

@client.command()
async def ip(ctx):
    ip = format_ip()
    await ctx.send(f"IP: {ip}")
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