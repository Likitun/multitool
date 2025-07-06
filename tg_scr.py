import asyncio
from telethon import TelegramClient
from telethon.errors import ChannelPrivateError, FloodWaitError
from dotenv import load_dotenv
import os
from termcolor import colored
from tqdm import tqdm

ru_lang = {
    "hi": "Привет! Это твой первый запуск? В таком случае нам потребуется задать парочку переменных для работы этого приложения",
    "qrdecode": "Код расшифрован:",
    "notqr": "QR-код не найден",
    "continue": "Нажмите Enter для продолжения",
    "first": "Исходный текст:",
    "qrcreate": "QR-код успешно создан!",
    "succesclipboard": "Успешно сохранено в буфер обмена!",
    "stopsound": "Для остановки нажмите Enter",
    "play": "Воспроизведение",
    "qrlogo": "Логотип не найден, добавьте его в qrcodes",
    "resultIN": "Результат в",
    "fileNotExist": "Входной файл не найден",
    "unsupportedconv": "Неподдерживаемая конвертация:",
    "successconv": "Конвертация завершена успешно",
    "VideoDonwloaded": "Видео успешно скачано",
    "noFiles": "Нет доступных файлов",
    "invalidNum": "Неверный номер файла",
    "invalidFormat": "Неверный номер формата",
    "canceled": "Конвертация отменена",
    "conversionTypes": "Доступные форматы для конвертации файла",
    "selectFormat": "Введите номер формата для конвертации",
    "confirmConvert": "Вы уверены, что хотите конвертировать",
    "welcome": "==== Мультитул ====",
    "telegram": "-----Телеграм-----",
    "spamPrompt": "Введите username пользователя: ",
    "spamText": "Введите текст для спама: ",
    "spamCount": "Введите кол-во сообщений: ",
    "readMessages": "Отметить все сообщения прочитанными",
    "selectservice":"Выберите нужный сервис:",
    "inputlink":"Введите ссылку на видео:",
    "selectfont":"Выберите номер нужного шрифта:",
    "selectedfont":"Выбраный шрифт",
    "inputtext":"Введите текст для текста:",
    "selectnumoffile":"Выберите номер файла:",
    "inputforqr":"Введите сообщение/ссылку для QR-кода:",
    "inputname": "Введите название QR-кода",
    "question":"Во сколько раз увеличить изображение?",
    "notsupportedsize":"Недопустимое увеличение, выставлено 2",
    "notsupportedconvetr":"Нет поддерживаемых вариантов конвертации для",
    "readed":"Прочитано",
    "spam":"Спам",
    "return":"Вернуться обратно",
    "quit":"Выход",
    "download":"Скачать видео",
    "convert":"Сменить расширение файла",
    "resize":"Увеличить изображение",
    "ASCII":"ASCII текст",
    "joke":"Случайная шутка",
    "qrcreatefunc":"Создать QR-код",
    "qrread":"Прочитать QR-код",
    "tg":"Телеграм"
}

en_lang = {
    "hi": "Hello! Is this your first launch? In that case, we need to set a couple of variables for this application to work",
    "qrdecode": "Code decrypted:",
    "notqr": "QR code not found",
    "continue": "Press Enter to continue",
    "first": "Original text:",
    "qrcreate": "QR code created successfully!",
    "succesclipboard": "Successfully saved to clipboard!",
    "stopsound": "Press Enter to stop",
    "play": "Playback",
    "qrlogo": "Logo not found, add it to qrcodes folder",
    "resultIN": "Result saved in",
    "fileNotExist": "Input file not found",
    "unsupportedconv": "Unsupported conversion:",
    "successconv": "Conversion completed successfully",
    "VideoDonwloaded": "Video downloaded successfully",
    "noFiles": "No available files",
    "invalidNum": "Invalid file number",
    "invalidFormat": "Invalid format number",
    "canceled": "Conversion canceled",
    "conversionTypes": "Available conversion formats for file",
    "selectFormat": "Enter format number for conversion",
    "confirmConvert": "Are you sure you want to convert",
    "welcome": "==== Multitool ====",
    "telegram": "----- Telegram -----",
    "spamPrompt": "Enter user's username: ",
    "spamText": "Enter spam text: ",
    "spamCount": "Enter number of messages: ",
    "readMessages": "Mark all messages as read",
    "selectservice": "Select service:",
    "inputlink": "Enter video URL:",
    "selectfont": "Select font number:",
    "selectedfont": "Selected font",
    "inputtext": "Enter text for ASCII art:",
    "selectnumoffile": "Select file number:",
    "inputforqr": "Enter message/link for QR code:",
    "inputname": "Enter QR code name:",
    "question": "How many times to enlarge the image? (2-4)",
    "notsupportedsize": "Invalid enlargement value, set to 2",
    "notsupportedconvetr": "No supported conversion options for",
    "readed": "Read",
    "spam": "Spam",
    "return": "Return back",
    "quit": "Exit",
    "download": "Download video",
    "convert": "Change file extension",
    "resize": "Resize image",
    "ASCII": "ASCII text",
    "joke": "Random joke",
    "qrcreatefunc": "Create QR code",
    "qrread": "Read QR code",
    "tg": "Telegram"
}

load_dotenv()
api_id = os.getenv("ID")
api_hash = os.getenv("HASH")
langs = os.getenv('LANG')
lang = ru_lang if langs == "ru" else en_lang
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
