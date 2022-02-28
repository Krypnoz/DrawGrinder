import pyfiglet
from discord.ext import commands
from discord.ext.commands import CommandNotFound

PREFIX = ";"
USERNAME = "Daniel" #Put your username here without the tag
CHANNEL_ID = 694294206969420420 #Channel ID you wanna grind in
ASCII_BANNER = pyfiglet.figlet_format("DrawGrinder")

print(f"{ASCII_BANNER}\nFrom the creator of PokeGrinder.")

client = commands.Bot(command_prefix=PREFIX, case_insensitive=True, help_command=None, self_bot = True)

def author(msg):
    embeds = msg.embeds
    for embed in embeds:
        author=str(embed.author)
        return author

@client.event
async def on_ready():
    print("DrawGrinder is ready!")

    channel = client.get_channel(CHANNEL_ID)

    #The Grinding starts here
    async for cmd in channel.slash_commands(query='draw'):
        await cmd()

@client.event
async def on_message_edit(before, after):
    if after.channel.id == CHANNEL_ID:
        if f'Congratulations, {USERNAME}!' in author(after) and after.components == []:
            channel = client.get_channel(CHANNEL_ID)

            async for cmd in channel.slash_commands(query='draw'):
                await cmd()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

client.run('') #Your token goes between the ''