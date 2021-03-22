import os
import discord
import asyncio
from urllib.request import urlopen
from bs4 import BeautifulSoup
from get_wotd import WOTD_English
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
wotd_dict = {}

async def check_wotd_update_background_task():
    await client.wait_until_ready()

    while not client.is_closed():
        try:
            await asyncio.sleep(60)
            print(datetime.utcnow())
            get_wotd_eng()
            print(wotd_dict['eng'])


        except Exception as e:
            pass

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'wotd!':
        response = get_wotd_eng()
        await message.channel.send(response)

def get_wotd_eng():
    url = 'https://www.dictionary.com/e/word-of-the-day/'
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html,features="html.parser")
    wotd = WOTD_English(soup)
    wotd_msg = wotd.wotd_msg()
    wotd_dict['eng'] = wotd.wotd_string
    return wotd_msg

if __name__ == "__main__":
    client.loop.create_task(check_wotd_update_background_task())
    client.run(TOKEN)
