import discord
import config
import questions
import random
import pandas as pd

TOKEN = config.TOKEN

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('---------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('!deep'):
            
            num = random.randint(0,276)
            quest = questions.question_list.iloc[num,0]

            await message.reply(quest, mention_author=False)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
