import discord
import os
from discord.ext import commands
from discord.ui import View, Button
from steamScrape import *
from lineups import *
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = int(os.environ.get('CHANNEL_ID'))

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hello! CS:GO Skins bot is ready!')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Hello! CS:GO Skins bot is ready!')

@bot.command()
async def info(ctx):
    await ctx.send('''```Stay up to date on all your skins!
Use the command "!skin *your skin name here*" to find the current market value
Use the command "!smoke *map* *ct or t* for line up videos (currently only mirage)```''')

@bot.command()
async def skin(ctx, *args):
    if len(args) == 1:
        search = args[0]
    else:
        search = ''
        for word in args:
            if word == args[-1]:
                search += word
            else:
                search += word + '+'
        
    query = itemSearch(search)
    link = itemURL(search)
    print(link)

    if len(query) < 1:
        await ctx.send(f'The skin, {search} was not found. Please try again.')
        return
    
    msg = createMsg(query)

    # initalize button interactions
    view = View()
    button_link = Button(label='Go to Marketplace', url=link)
    view.add_item(button_link)
    await ctx.send(msg, view = view)

@bot.command()
async def smoke(ctx, *args):
    search = map_search(args)
    view = search
    await ctx.send('Please choose a line up', view = view)


bot.run(BOT_TOKEN)
