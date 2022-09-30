import os
import fetch_data
import discord
from dotenv import load_dotenv
from discord.ext import commands
import time
import chat

load_dotenv()


intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
#intents.message_content = True
allowed_mention = discord.AllowedMentions.all()
client = commands.Bot(command_prefix='$', intents=intents)

cycle = dict(loop=True)


@client.command()
async def test(ctx):
    await ctx.send("Testing works")


@client.command()
async def stop(ctx):
    cycle['loop'] = False
    await ctx.send("The alert is stopped")


@client.command()
async def start(ctx):
    cycle['loop'] = True
    symbol = fetch_data.fetch_data()
    mention = await ctx.send('None')
    new_msg = await ctx.send("test")
    while cycle['loop']:
        if len(symbol) > 0:
            trigger = symbol
            new_men = '@everyone'
            await mention.edit(content=new_men)
            coins =[]
            text = 'The Triggered Coins are:'
            coins.append(text)
            for item in trigger:
                coins.append(item)
            new_coin = coins
            await new_msg.edit(content=new_coin)
        else:
            new_con = 'sorry no triggered symbol found'
            await new_msg.edit(content=new_con)



@client.event
async def on_ready():
    print("I am ready as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)
    msg = message.content

    if any(word in msg.lower() for word in chat.trigger):
        await message.channel.send('Works')


token = os.environ.get('token')
client.run(token)
