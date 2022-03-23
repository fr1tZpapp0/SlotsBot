import discord
from discord.ext import commands
import os
import random

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.read()


client = discord.Client()
bot = commands.Bot(command_prefix='?')

randolist = ["CHERRY", "7", "BAR"]
cardslist = ["ACE", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"]


@client.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='slots')
async def slots(ctx):
    embedslot = discord.Embed(title="SLOTS", description="ROLLING FOR SLOTS!", color=0x00ff00, type="rich")
    embedslot.add_field(name="SLOTOMATIC", value=":slot_machine:" + " " + random.choice(randolist) + " "
    + random.choice(randolist) + " " +random.choice(randolist) + " " + ":slot_machine:", inline=False)
    await ctx.send(embed=embedslot)

@bot.command(name="blackjack")
async def blackjack(ctx):
    embedbjd = discord.Embed(title="BLACK JACK", description="DEALER'S HAND", color=0x00ff00, type="rich")
    embedbjd.add_field(name="CARDS", value=random.choice(cardslist) + " " + random.choice(cardslist) , inline=False)
    await ctx.send(embed=embedbjd)

    embedyourhand = discord.Embed(title="BLACK JACK", description="YOUR HAND", color=0x00ff00, type="rich")
    embedyourhand.add_field(name="CARDS", value=random.choice(cardslist) + " " + random.choice(cardslist), inline=False)
    await ctx.send(embed=embedyourhand)

async def hit(ctx):
    #embedhit = discord.Embed(title=)
    print("HELLO")

bot.run(TOKEN)
