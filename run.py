from create_gif import create_gif
import discord
import json

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
        if commands[0] == 'execute':
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
        elif commands[0] == 'quote':
            pass
        else:
            msg = """ 
The current available BradyBot commands are:\n
1) BradyBot execute @UserName
    - Creates a gif of that user getting killed in Among Us
    - Use the users @ in the command to use their icon in the gif\n
2) BradyBot quote
    - Sends a random quote from Brady (TODO)\n
3) BradyBot add-quote the_quote_you_would_like_to_add
    - Adds a new quote into Brady's endless knowledge (TODO)\n
"""
            await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
