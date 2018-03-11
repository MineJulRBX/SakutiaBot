import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os 

Client = discord.Client()
client = commands.Bot(command_prefix = "=")

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    if message.server.id == "409009938698993664":
        if message.channel.id == "421935707138031622":
            if message.content.upper().startswith('=PARTNER'):
                await client.send_message(message.channel, "Is it a good server? \n What is the server member count? Don't include bots! \n What is the server name? Exact name. \n Who's the owner? Give exact Owner#1234 with tag. \n What kind of server is it? Community, Gaming, Dating, Adult, Bot, ect. \n What is the invite link? It must be a discord .gg/INVITE type of link. Be sure to set to never expire \n Start your applyment with `=applyment`!")
                await client.send_message(message.channel, "Keep you answers in **one line** like this: `=applyment Yes, 28, Sakutia Studios, Ckent1938#7053, Community Gaming, discord. gg/INVITE`")
            if message.content.upper().startswith('=APPLYMENT'):
                args = message.content.split(" ")
                await client.send_message(client.get_server("420470593184333834") and client.get_channel("422084206752038914"), "%s" % (" ".join(args[1:])))
                await client.delete_message(message)
                UserID = message.author.id
                await client.send_message(message.channel, f"{message.author.mention} Your Patners Application has ben sent to the queue. It will take 12-72 hours for respond.")


client.run(os.getnenv('TOKEN'))
