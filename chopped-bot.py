# Chopped-Bot.py
from curses.ascii import EM
import os
from queue import Empty

import discord
from discord.ext import commands
import dotenv

from listCreator import ListCreator

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

WeeklyBasket = []
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.command()
async def hello(ctx):
    await ctx.send("hey!")

@bot.command()
async def randombasket(ctx):
    choppedIngredients = ListCreator()
    await ctx.send(choppedIngredients)

@bot.command()
async def weeklybasket(ctx):
    if WeeklyBasket:
        await ctx.send(WeeklyBasket)
    else:
        await ctx.send("The Weekly Basket is currently empty, try a !randombasket or wait for next week!")        

bot.run(TOKEN)    

"""
#for date time maybe make a trigger at 6 pm every day to check the day of the week and then have a conditional where if it is sunday make a new chopped list

    if not WeeklyBasket:
        choppedBasket = ListCreator()
        for ingredients in choppedBasket:
            WeeklyBasket.append(ingredients)
"""