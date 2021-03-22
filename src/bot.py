import os
import discord
import asyncio
import pytz
from urllib.request import urlopen
from bs4 import BeautifulSoup
from get_wotd import WOTD_English, WOTD_Italian, WOTD_German, WOTD_French, WOTD_Russian
from dotenv import load_dotenv
from datetime import datetime, timedelta
from google_trans_new import google_translator

translator = google_translator()

POSTING_FREQUENCY = timedelta(hours=24)
REFRESH_RATE = 5

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
main_channel_id = 755393652791967855
test_channel_id = 496346061607010304
wotd_dict = {}


async def check_wotd_update_background_task():
    posting_time = datetime.now(pytz.timezone("Australia/Melbourne")).replace(hour=23, minute=0, second=0, microsecond=0)
    posted = False
    yesterday = (datetime.utcnow() - POSTING_FREQUENCY).date()

    await client.wait_until_ready()

    while not client.is_closed():
        try:
            await asyncio.sleep(REFRESH_RATE)
            #print(f'current time: {datetime.now()}')
            #print(f'posting time: {posting_time}')
            time = datetime.now(pytz.timezone("Australia/Melbourne"))

            if time.date() != yesterday:
                print(f"ALERT: New day! {time.date()}")
                posted = False
                yesterday = time.date()

            if time > posting_time and not posted:
                posted = True
                posting_time = posting_time + POSTING_FREQUENCY
                print(f"ALERT: Posted WotD for today at {time}!")
                print(f'New posting time: {posting_time}')

                response = get_all_wotd()
                channel = await client.fetch_channel(test_channel_id)
                await channel.send(response)

        except Exception as e:
            print(e)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'wotd-english!':
        response = get_wotd_en()
        await message.channel.send(response)

    if message.content == 'wotd-italian!':
        response = get_wotd_it()
        await message.channel.send(response)

    if message.content == 'wotd-german!':
        response = get_wotd_ge()
        await message.channel.send(response)

    if message.content == 'wotd!':
        response = get_all_wotd()
        await message.channel.send(response)

    if message.content.startswith('wotd!trans '):
        text = message.content[len('wotd!trans ')::]
        trans_text= translate(text)
        await message.channel.send(f"**\"{text}\"** is translated to:\n> {trans_text}")

    if message.content == 'wotd!set':
        main_channel = message.channel.id
        await message.channel.send("Set as main channel.")


def translate(text, src=None, dst='en'):
    print(f"Received text {text}")
    translation = translator.translate(text, lang_tgt=dst)
    return translation


def get_wotd_en():
    url = 'https://www.dictionary.com/e/word-of-the-day/'
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html,features="html.parser")
    wotd = WOTD_English(soup)
    wotd_msg = wotd.wotd_msg()
    wotd_dict['en'] = wotd_msg
    return wotd_msg


def get_wotd_it():
    url = 'https://www.italianpod101.com/italian-phrases/'
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html,features="html.parser")
    wotd = WOTD_Italian(soup)
    wotd_msg = wotd.wotd_msg()
    wotd_dict['it'] = wotd_msg
    return wotd_msg


def get_wotd_ge():
    url = 'https://www.germanpod101.com/german-phrases/'
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html,features="html.parser")
    wotd = WOTD_German(soup)
    wotd_msg = wotd.wotd_msg()
    wotd_dict['ge'] = wotd_msg
    return wotd_msg


def get_wotd_fr():
    url = 'https://www.frenchpod101.com/french-phrases/'
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html,features="html.parser")
    wotd = WOTD_French(soup)
    wotd_msg = wotd.wotd_msg()
    wotd_dict['fr'] = wotd_msg
    return wotd_msg


def get_wotd_ru():
    url = 'https://www.russianpod101.com/russian-phrases/'
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html,features="html.parser")
    wotd = WOTD_Russian(soup)
    wotd_msg = wotd.wotd_msg()
    wotd_dict['ru'] = wotd_msg
    return wotd_msg


def get_all_wotd():
    get_wotd_en()
    get_wotd_it()
    get_wotd_ge()
    get_wotd_fr()
    get_wotd_ru()
    print(wotd_dict)
    output = ""
    for wotd in wotd_dict.values():
        output += wotd + '\n\n'
    print(output)
    return output


if __name__ == "__main__":
    client.loop.create_task(check_wotd_update_background_task())
    client.run(TOKEN)
