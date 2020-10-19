from create_gif import CreateGif, Gifs
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
        helper = Helper(message.author)
        commands = message.content.split(' ', 2)
        del commands[0]
        if commands[0].lower() == 'execute':
            helper.increment_count()
            argument_data = commands[1]
            if message.mentions:
                mentioned_user = message.mentions[0]
                argument_data = mentioned_user.avatar_url

            CreateGif(argument_data).generate_gif(Gifs.AMONG_US_KILL)
            msg = f"Brady has executed {commands[1]}"
            await message.channel.send(msg, file=discord.File('output.gif'))
        elif commands[0].lower() in ['kd', 'kills', 'executions', 'kill-count']:
            kills = helper.get_count()
            msg = f"My current {commands[0]} is {kills} and I do not plan to stop. \n\"Ah, first blood.\" - 🅱"
            await message.channel.send(msg)
        elif commands[0].lower() in ['smash', 'challenger']:
            argument_data = commands[1]
            if message.mentions:
                mentioned_user = message.mentions[0]
                argument_data = mentioned_user.avatar_url

            CreateGif(argument_data).generate_gif(Gifs.CHALLENGER)
            msg = f"You dare to challenge me {commands[1]}?"
            await message.channel.send(msg, file=discord.File('output.gif'))
        elif commands[0].lower() == 'quote':
            del commands[0]
            if len(commands) > 0:
                line = int(commands[0])
                quotes = helper.get_quotes()
                if 0 < line <= len(quotes):
                    msg = quotes[line - 1]
                else:
                    msg = f"A quote at line {line} does not exist.\n“We're worried about the sad path, " \
                          f"we're not worried about the happy path...” - 🅱"
            else:
                msg = helper.random_quote()
            await message.channel.send(msg)
        elif commands[0].lower() == 'quote-all':
            msg = helper.show_all_quotes()
            # Messages can only be 2k in length. This will split the messages.
            while len(msg) > 0:
                await message.channel.send(msg[0:1999])
                msg = msg[1999:]
        elif commands[0].lower() == 'add':
            del commands[0]
            add_commands = commands[0].split(' ', 1)
            if add_commands[0].lower() == 'quote':
                argument_data = add_commands[1]
                line = helper.add_quote(argument_data)
                msg = f"The new quote was added at line {line}"
                await message.channel.send(msg)
        elif commands[0].lower() == 'remove-quote':
            del commands[0]
            if message.author.guild_permissions.administrator:
                line = int(commands[0])
                if 0 < line <= len(helper.get_quotes()):
                    helper.remove_quote(line)
                    msg = f"Successfully removed quote on line {line}."
                else:
                    msg = f"A quote at line {line} does not exist.\n“We're worried about the sad path, " \
                          f"we're not worried about the happy path...” - 🅱"
            else:
                msg = 'You do not have the permissions to delete a quote (Administrator permission needed).'
            await message.channel.send(msg)
        elif commands[0].lower() == 'markov':
            msg = helper.markov()
            await message.channel.send(msg)
        elif commands[0].lower() == 'new':
            msg = """ 
New features/improvements/commands:\n
• Added smash/challenger gif. Use command `BradyBot smash|challenger @UserName` to use it. Optionally type any text in 
for `@UserName` to search for an image.\n
• Added Markov chains created from the quotes added to the BradyBot. Use command `BradyBot markov`.
"""
            await message.channel.send(msg)
        elif commands[0].lower() == 'help':
            msg = """ 
The current available BradyBot commands are:\n
• `BradyBot execute @UserName`
    - Creates a gif of that user getting killed in Among Us
    - Use the users @ in the command to use their icon in the gif
    - Type any text after to search for an image\n
• `BradyBot kd|kills|executions|kill-count`
    - Tells you how many people Brady has executed\n
• `BradyBot smash|challenger @UserName`
    - Creates a gif of that user getting introduced in smash
    - Use the users @ in the command to use their icon in the gif
    - Type any text after to search for an image\n
• `BradyBot quote`
    - Sends a random quote from Brady
    - Optionally you can specify the line of the quote (e.g. `BradyBot quote 1`)\n
• `BradyBot quote-all`
    - Shows all the quotes\n
• `BradyBot add quote the_quote_you_would_like_to_add`
    - Adds a new quote into Brady's endless knowledge\n
• `BradyBot markov`
    - Creates a Markov chain using the quotes added to the BradyBot\n
• `BradyBot new`
    - Tells you about what is new, features, improvements, and/or commands for the most recent update\n
• `BradyBot remove-quote quote_line`
    - Removes a quote by the line. Requires Administrator permission to do so.\n
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
