# bot.py
from dwc_bot.connector import Connector
import os
import discord

class Discord(Connector):

    def __init__(self):
        super().__init__()
        self.client = self.connect()
        
    
    def connect(self):

        token = os.getenv(self.details['token'])

        client = discord.Client()
        @client.event
        async def on_ready():
            print(f'{client.user} has connected to Discord!')
        client.run(token)
        return client