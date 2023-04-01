from discord.ext import commands, tasks
import discord
from discord.ui import View, Button
from steamScrape import *

BOT_TOKEN = 'MTA5MDAzMDU0NDM4Mjg2MTM3Mw.GChRg4.9IdGWvX5kS7LZ0gpwps8R2yBC43GOg9dJUm_N0'
CHANNEL_ID = 1090032011311329414

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hello! CS:GO Skins bot is ready!')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Hello! CS:GO Skins bot is ready!')

@bot.command()
async def info(ctx):
    await ctx.send('''`Stay up to date on all your skins!
Use the command "!skin *your skin name here*" to find the current market value`''')

@bot.command()
async def skin(ctx, *args):
    search = ''
    for word in args:
        search += word.lower() + ' '
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


bot.run(BOT_TOKEN)