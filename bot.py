import discord
import responses
import config
from discord.ext import commands





async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = config.TOKEN
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix = '!')

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')



    @client.event
    async def on_message(message):
        # prevents bot from responding to itself
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

    @bot.event
    async def hello(ctx):
        msg = f'Hi {ctx.author.mention}'
        await ctx.send(msg)



    @client.event

    client.run(config.TOKEN)   

