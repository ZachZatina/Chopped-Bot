# Chopped-Bot.py
from curses.ascii import EM
import os
from queue import Empty

import discord
from dotenv import load_dotenv
from listCreator import ListCreator

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

WeeklyBasket = []

client = discord.Client()

#for date time maybe make a trigger at 6 pm every day to check the day of the week and then have a conditional where if it is sunday make a new chopped list

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    textChannelList = []
    for server in client.servers:
        for channel in server.channels:
            if channel.type == 'Text':
                textChannelList.append(channel)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'(id: {guild.id})'
        #checking for the id value of the anyone can cook channel, or make a way so that the id can be dynamic based on what channel it recieves a message from?
        f'{textChannelList}'
    )

    if not WeeklyBasket:
        choppedBasket = ListCreator()
        for ingredients in choppedBasket:
            WeeklyBasket.append(ingredients)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!randombasket'):
        choppedIngredients = ListCreator()
        await message.channel.send(choppedIngredients)

    if message.content.startswith('!weeklybasket') and WeeklyBasket:
        await message.channel.send(WeeklyBasket)

    if message.content.startswith('!weeklybasket') and not WeeklyBasket:
        await message.channel.send('The Weekly Basket is currently empty, try a !randombasket or wait for next week!')
        
    

client.run(TOKEN)
