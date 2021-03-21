import os
import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup
from get_wotd import WOTD
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'wotd!':
        response = get_wotd()
        await message.channel.send(response)

def get_wotd():
    url = 'https://www.dictionary.com/e/word-of-the-day/'
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html,features="html.parser")
    wotd = WOTD(soup)
    wotd_msg = wotd.print_wotd()
    return wotd_msg

client.run(TOKEN)
