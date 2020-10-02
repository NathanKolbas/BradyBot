from create_gif import create_gif
import discord
import json
from run_helper import *

with open('config.json') as f:
    config = json.load(f)

TOKEN = config['BOT_TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.lower().startswith('bradybot '):
        commands = message.content.split(' ')
        commands.pop(0)
        if commands[0].lower() == 'execute':
            increment_count()
            if message.mentions:
                mentioned_user = message.mentions[0]
                profile_icon = mentioned_user.avatar_url
                gif = create_gif(profile_icon)
                msg = f"Brady has executed {commands[1]}"
                await message.channel.send(msg, file=discord.File(gif))
            else:
                # List is empty
                gif = create_gif(None)
                msg = f"Brady has executed {commands[1]}. (Note: Use their @ to get their profile icon)"
                await message.channel.send(msg, file=discord.File(gif))
        elif commands[0].lower() in ['kd', 'kills', 'executions', 'kill-count']:
            kills = get_count()
            msg = f"My current {commands[0]} is {kills} and I do not plan to stop. \n\"Ah, first blood.\" - 🅱"
            await message.channel.send(msg)
        elif commands[0].lower() == 'quote':
            pass
        else:
            msg = """ 
The current available BradyBot commands are:\n
• `BradyBot execute @UserName`
    - Creates a gif of that user getting killed in Among Us
    - Use the users @ in the command to use their icon in the gif\n
• `BradyBot [kd, kills, executions, kill-count]`
    - Tells you how many people Brady has executed\n
• `BradyBot quote`
    - Sends a random quote from Brady (TODO)\n
• `BradyBot add-quote the_quote_you_would_like_to_add`
    - Adds a new quote into Brady's endless knowledge (TODO)\n
Created by: Nathan Kolbas
"""
            await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
