import asyncio
from telethon import TelegramClient
from telethon.errors import ChannelPrivateError, FloodWaitError
from dotenv import load_dotenv
import os
from termcolor import colored
from tqdm import tqdm


load_dotenv()
api_id = os.getenv("ID")
api_hash = os.getenv("HASH")
langs = os.getenv('LANG')
async def spam(username,text,num):
    bot = TelegramClient("bot", api_id, api_hash)
    num = int(num)
    async with bot as client:
        await client.connect()
        if not await client.is_user_authorized():
            await client.start()
        entity = await client.get_entity(username)
        for _ in tqdm(range(int(num))):
            try:
                await client.send_message(entity,text)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds)
                continue
async def read_messages():
    bot = TelegramClient("bot", api_id, api_hash)
    os.system("cls")
    async with bot as client:
        await client.connect()
        if not await client.is_user_authorized():
            await client.start()
        dialogs = [d for d in await client.get_dialogs() if d.unread_count > 0]

        for dialog in dialogs:
            try:
                if dialog.name in ['Replies', 'Telegram', 'Saved Messages']:
                    continue

                entity = await client.get_input_entity(dialog.entity)

                await client.send_read_acknowledge(entity)
                print(f"{lang["readed"]}: {dialog.name}")
            except Exception as e:
                print(f"{dialog.name}: {str(e)}")
                await asyncio.sleep(3)
            finally:
                await asyncio.sleep(0.3)
    await tg()

async def tg():
    os.system("cls")
    colored(lang['telegram'],"white","on_light_cyan")
    functions = [colored(lang['return'],"white"),colored(lang['spam'],"light_green"),colored(lang['readMessages'],"blue")]
    for i,func in enumerate(functions):
        print(f"{i}. {func}")
    voice = input(f"{lang["selectservice"]} ")
    if voice == "0":
        from main import main
        await main()
    if voice == "2":
        await read_messages()
    if voice == "1":
        os.system('cls')
        user = input(colored( lang["spamPrompt"],"cyan"))
        text = input(colored(f"{lang["spamText"]}\n","cyan"))
        num = input(colored(lang['spamCount'],"cyan"))
        await asyncio.gather(spam(user,text,num))
