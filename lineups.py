import discord
from discord.ui import Select, View
from discord.ext import commands

class Mirage_T(View):
    @discord.ui.select(
        placeholder='Mirage T side smokes',
        options=[
            discord.SelectOption(
                label='Ticket Booth',
                description='From T ramp',
                value = 'https://gfycat.com/elegantimportantcricket'
            ),
            discord.SelectOption(
                label='Stairs',
                description='From T Ramp',
                value = 'https://gfycat.com/frighteningneategret'
            ),
            discord.SelectOption(
                label='Jungle and Connector',
                description='From T Ramp',
                value = 'https://gfycat.com/youngpoisedcattle'
            ),
            discord.SelectOption(
                label='Jungle',
                description='From Tetris',
                value = 'https://gfycat.com/mammothimpressiveglobefish'
            ),
            discord.SelectOption(
                label='Top Mid',
                description='From T Spawn',
                value= 'https://gfycat.com/tastyinstructiveamoeba'
            ),
            discord.SelectOption(
                label='Mid Window',
                description='From T Spawn',
                value= 'https://gfycat.com/remoteneedygrasshopper'
            ),
            discord.SelectOption(
                label='Connector',
                description='From Apt Ramp',
                value= 'https://gfycat.com/blushingregalaffenpinscher'
            ),
            discord.SelectOption(
                label='Catwalk',
                description='From Top Mid',
                value= 'https://gfycat.com/aromaticaggressivekakapo'
            ),
            discord.SelectOption(
                label='Market Window',
                description='From Back Alley',
                value= 'https://gfycat.com/specificraredeviltasmanian'
            ),
            discord.SelectOption(
                label='Right Arches',
                description='From Back Alley',
                value= 'https://gfycat.com/shorttermsecondhandfly'
            ),
        ]
    )
    async def select_callback(self, interaction, select):
        # select.disabled = True
        # await interaction.response.edit_message(view=self)
        await interaction.followup.send(f'{select.values[0]}')

class Mirage_CT(View):
    @discord.ui.select(
        placeholder='Mirage CT side smokes',
        options=[
            discord.SelectOption(
                label='Palace',
                description='From CT Spawn',
                value = 'https://gfycat.com/defensivehandsomegordonsetter'
            ),
            discord.SelectOption(
                label='A Ramp',
                description='From Triple Box',
                value = 'https://gfycat.com/revolvingmarvelouseskimodog'
            ),
            discord.SelectOption(
                label='Top Mid',
                description='From CT Spawn',
                value = 'https://gfycat.com/grandiosebriskhawk'
            ),
            discord.SelectOption(
                label='A Site Retake',
                description='From Vents',
                value = 'https://gfycat.com/firstregularguillemot'
            ),
            discord.SelectOption(
                label='B Apts',
                description='From Market',
                value= 'https://gfycat.com/helplesswaterloggedhydra'
            ),
            discord.SelectOption(
                label='Deep Apps Smoke',
                description='From CT Spawn',
                value= 'https://gfycat.com/basicbighummingbird'
            ),
            discord.SelectOption(
                label='Connector Smoke',
                description='From Ticket Booth',
                value= 'https://gfycat.com/perfectwigglyaxisdeer'
            ),
        ]
    )
    async def select_callback(self, interaction, select):
        # select.disabled = True
        # await interaction.response.edit_message(view=self)
        await interaction.followup.send(f'{select.values[0]}')

def map_search(args):
    maps = ['mirage', 'inferno', 'dust2']
    print(f'{args[0]} ==== {args[1]}')
    if args[0].lower() not in maps:
        return 'Your search is not in our current maps database'
    elif args[1].lower() != 't' and args[1].lower() != 'ct':
        return 'Please choose T or CT side as the second statement'

    map_lineups = {
        'mirage_ct': Mirage_CT(),
        'mirage_t': Mirage_T(),
    }
    search = args[0].lower() + '_' + args[1].lower()

    return map_lineups[search]
