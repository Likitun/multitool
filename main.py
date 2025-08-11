import sys
from time import sleep
from moviepy import *
from PIL import Image, ImageDraw
from pytubefix import YouTube
from pytubefix.cli import on_progress
from termcolor import colored
import msvcrt
import os
import librosa
import sounddevice as sd
import numpy as np
from tqdm import tqdm
import pyfiglet
import pyjokes
import qrcode
import asyncio
import cv2
import pyperclip
from dotenv import load_dotenv
from tg_scr import tg

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
    "selectservice": "Выберите нужный сервис:",
    "inputlink": "Введите ссылку на видео:",
    "selectfont": "Выберите номер нужного шрифта:",
    "selectedfont": "Выбраный шрифт",
    "inputtext": "Введите текст для текста:",
    "selectnumoffile": "Выберите номер файла:",
    "inputforqr": "Введите сообщение/ссылку для QR-кода:",
    "inputname": "Введите название QR-кода",
    "question": "Во сколько раз увеличить изображение?",
    "notsupportedsize": "Недопустимое увеличение, выставлено 2",
    "notsupportedconvetr": "Нет поддерживаемых вариантов конвертации для",
    "readed": "Прочитано",
    "spam": "Спам",
    "return": "Вернуться обратно",
    "quit": "Выход",
    "download": "Скачать видео",
    "convert": "Сменить расширение файла",
    "resize": "Увеличить изображение",
    "ASCII": "ASCII текст",
    "joke": "Случайная шутка",
    "qrcreatefunc": "Создать QR-код",
    "qrread": "Прочитать QR-код",
    "tg": "Телеграм",
    "installandsetting": "Установите VB-Cable и настройте систему",
    "notdefinecable": "Виртуальное устройство 'CABLE Input' не найдено!",
    "use": "Будете ли вы использовать функции Телеграм? (y/n)",
    "tutorial": """1. Перейдите на сайт: https://my.telegram.org

2. Авторизуйтесь через свой аккаунт Telegram

3. В разделе "App configuration" скопируйте значения api_id и api_hash

Не делитесь этими данными ни с кем, кроме этой программы!""",
    "sorry": "Если вы ввели данные неправильно, функции работы с Телеграмом не будут работать и будут выдавать ошибки. Для исправления измените значения в .env"

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
    "tg": "Telegram",
    "installandsetting": "Setup VB-Cable",
    "notdefinecable": "'CABLE Input' device missing",
    "use": "Will you use Telegram functionality? (y/n)",
    "tutorial": """1. Go to the site: https://my.telegram.org

2. Log in via your Telegram account

3. In the "App configuration" section, copy the api_id and api_hash values

Do not share this data with anyone outside this program!""",
    "sorry": "If you entered incorrect data, Telegram features will not work and will produce errors. To fix this, modify the values in the .env file"
}
if os.path.exists(".env"):
    load_dotenv()
    langs = os.getenv('LANG')
    API = os.getenv('ID')
    lang = ru_lang if langs == "ru" else en_lang
    def qrReader(file):
        os.system('cls')
        img = cv2.imread(file)
        detector = cv2.QRCodeDetector()
        data,box,stqrcode = detector.detectAndDecode(img)
        if box is not None:
            print(colored(f"{lang["qrdecode"]}\n{data}","green"))
        else:
            print(colored(lang['notqr'],"red"))
        input(f"\n{lang['continue']}")
        return
    def create_qr(inputa,outputa):
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4, )
        qr.add_data(inputa)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        try:
            logo = Image.open(r"D:\myModule\qrcodes\logo.jpg")
            logo = logo.resize((100, 100))
            mask = Image.new('L', (100, 100), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 100, 100), fill=255)
            pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            img.paste(logo, pos, mask)
        except:
            print(lang['qrlogo'])
        img.save(r"qrcodes\\"+outputa+".png")
        print(colored(f"\n{lang["qrcreate"]}", "green"))
        sleep(3)
        return

    def variations():
        variationes = ['3-d', '3d-ascii',"5x7","5x8","6x10","6x9","alligator2","alligator","amc_3_line","ansi_regular","ansi_shadow","banner3-D","big","bloody"]
        for i, var in enumerate(variationes, 1):
            print(f"{i}. {var}")
        return variationes
    def figlet(text,variation):
        os.system("cls")
        figletret=pyfiglet.figlet_format(text,variation)
        print(figletret)
        pyperclip.copy(figletret)
        print(f"\n{lang['succesclipboard']}")
        input(f"\n\n{lang['continue']}")
        return

    def sounds(sound):
        os.system('cls')
        audio_path = r"D:\myModule\sounds\\"+sound
        audio_data, sample_rate = librosa.load(audio_path, sr=None, mono=True)
        audio_data = audio_data / np.max(np.abs(audio_data))
        volume = 1
        device_id = None
        devices = sd.query_devices()
        for i, dev in enumerate(devices):
            if 'CABLE Input' in dev['name'] and dev['max_output_channels'] > 0:
                device_id = i
                break

        if device_id is None:
            print(colored(lang['notdefinecable'], "red"))
            print(lang['installandseting'])
            input(lang['continue'])
            return
        stream = sd.play(audio_data*volume, sample_rate, device=device_id)
        duration = len(audio_data) / sample_rate
        print(lang['stopsound'])
        with tqdm(total=round(duration, 2),
                     desc=lang['play'],
                     unit="s",
                     bar_format="{l_bar}{bar}| {n:.2f}/{total:.2f}s [{elapsed}<{remaining}]",
                     ncols=80) as pbar:
            for i in range(int(duration * 10)):
                sleep(0.1)
                pbar.update(0.1)
                if msvcrt.kbhit() and msvcrt.getch() == b'\r':
                    break
        sd.stop()

    def upscale_pil(input_path, output_path, scale_factor=2):
        with Image.open(input_path) as img:
            width, height = img.size
            new_size = (width * scale_factor, height * scale_factor)

            upscaled = img.resize(new_size, Image.Resampling.LANCZOS)
            upscaled.save(output_path)
            print(colored(f"{lang["resultIN"]} {output_path}","green"))
            sleep(3)
            return

    def convertation(file,ext):
        output_path = os.path.splitext(file)[0] + ext
        input_ext = os.path.splitext(file)[1]
        if not os.path.exists(file):
            print(colored(f"{lang['fileNotExist']}: {file}"),"red")
        if input_ext in ('.mp3', '.wav', '.ogg', '.flac') and ext in ('.mp3', '.wav', '.ogg', '.flac'):
            audio = AudioFileClip(file)
            audio.write_audiofile(output_path)
            audio.close()
        elif input_ext in ('.mp4', '.avi', '.mov',".mkv") and ext in ('.mp3', '.wav', '.ogg', '.flac'):
            video = VideoFileClip(file)
            video.audio.write_audiofile(output_path)
            video.close()
        elif input_ext in ('.mp4', '.avi', '.mov',".mkv") and ext == '.gif':
            video = VideoFileClip(file)
            video.write_gif(output_path)
            video.close()
        elif input_ext in ('.mp4', '.avi', '.mov',".mkv") and ext in ('.mp4', '.avi', '.mov',".mkv"):
            video = VideoFileClip(file)
            video.write_videofile(output_path)
            video.close()
        elif input_ext in ('.jpg', '.jpeg', '.png', '.gif', '.bmp') and ext in ('.jpg', '.jpeg', '.png', '.gif','.bmp'):
            img = Image.open(file)
            img.save(output_path)
        else:
            print(colored(f"{lang["unsupportedconv"]} {input_ext} -> {ext}","red"))
            sleep(3)
            return
        print(colored(f"\n{lang['successconv']}: {file} -> {output_path}",'green'))
        sleep(3)
        return

    def supported_extensions(ext):
        conversions = {
            '.mp3': ['.ogg', '.wav', '.flac'],
            '.wav': ['.mp3', '.ogg', '.flac'],
            '.ogg': ['.mp3', '.wav', '.flac'],
            '.flac': ['.mp3', '.wav', '.ogg'],
            '.mp4': ['.mp3', '.avi', '.mov', '.gif', '.mkv'],
            '.avi': ['.mp4', '.mov', '.mp3', '.gif', '.mkv'],
            '.mov': ['.mp4', '.avi', '.mp3', '.gif', '.mkv'],
            '.mkv': ['.mp4', '.avi', '.mov', '.mp3', '.gif'],
            '.jpg': ['.png', '.gif', '.bmp'],
            '.jpeg': ['.png', '.gif', '.bmp'],
            '.png': ['.jpg', '.jpeg', '.gif', '.bmp'],
            '.gif': ['.jpg', '.jpeg', '.png', '.bmp'],
            '.bmp': ['.jpg', '.jpeg', '.png', '.gif']
        }
        return conversions.get(ext)

    def download_youtube(ref):
        y = YouTube(ref)
        y.register_on_progress_callback(on_progress)
        y.streams.get_highest_resolution().download()
        print(colored(lang['VideoDonwloaded'],"green"))
        sleep(3)

    def fileslist() -> list:
        files = [f for f in os.listdir() if os.path.isfile(f) and f != os.path.basename(__file__) and os.path.splitext(f)[1] not in [".session",'.py'] and f != ".env"]
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
        return files

    def fileslistsounds():
        folder_path = os.path.join(os.path.dirname(__file__), "sounds")
        files = [f for f in os.listdir(folder_path)if os.path.isfile(os.path.join(folder_path, f)) and f != os.path.basename(__file__) and os.path.splitext(f)[1] not in [".session",".py"] and f != ".env"]
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
        return files
    def fileslistim() -> list:
        files = [f for f in os.listdir() if os.path.isfile(f) and f != os.path.basename(__file__) and os.path.splitext(f)[1] in [".png",".jpg"]]
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
        return files

    async def main():
        os.system("cls")
        print(colored("""██╗  ██╗██╗   ██╗██████╗ ██╗██╗  ██╗
██║ ██╔╝██║   ██║██╔══██╗██║██║ ██╔╝
█████╔╝ ██║   ██║██████╔╝██║█████╔╝ 
██╔═██╗ ██║   ██║██╔══██╗██║██╔═██╗ 
██║  ██╗╚██████╔╝██████╔╝██║██║  ██╗
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝\n\n\n""", "light_magenta"))
        print(colored(f"{lang["welcome"]}\n","green",attrs=['underline']))
        serveses = [colored(lang['quit'],"red"),colored(lang['download'],"white"),colored(lang["convert"],"cyan"),colored(lang['resize'],"light_green"),colored(lang['ASCII'],"light_blue"),colored(lang['joke'],"light_grey"),colored(lang['qrcreatefunc'],"green"),colored(lang['qrread'],"dark_grey")]
        if API != "-1":
            serveses.append(colored(lang['tg'],"white","on_light_cyan"))
        print("==================\n")
        for i,serve in enumerate(serveses):
            print(f"{i}. {serve}")
        input_user = input(f"{lang['selectservice']} ")
        if input_user == "1":
            os.system("cls")
            ref = input(f"{lang['inputlink']}\n")
            download_youtube(ref)
        if input_user == "5":
            os.system("cls")
            vars = variations()
            var_num = int(input(f"{lang['selectfont']} "))
            if 0 < var_num and var_num <= len(vars):
                selected_font = vars[int(var_num) - 1]
                os.system("cls")
                print(colored(f"{lang['selectedfont']} {selected_font}","green"))
                text = input(f"{lang["inputtext"]}:\n")
                figlet(text,selected_font)
        if input_user == "9" and API != "-1":
            await tg()
        if input_user == "8":
            os.system("cls")
            files = fileslist()
            if not files:
                print(colored(f"{lang["noFiles"]}\n\n","red"))
                sleep(3)
                return
            else:
                file_num = int(input(f"{lang['selectnumoffile']}: "))
                if 0 < file_num and file_num <= len(files):
                    selected_file = files[int(file_num)-1]
                    qrReader(selected_file)
        if input_user == "6":
            os.system('cls')
            print(pyjokes.get_joke('ru' if lang == ru_lang else "en"))
            input(f"\n\n{lang['continue']}")
            return
        if input_user == "7":
            os.system("cls")
            inputa = input(f"""{lang['inputforqr']} \n""")
            outputa = input(f"\n{lang['inputname']}: \n")
            create_qr(inputa,outputa)
        if input_user == "0":
            sys.exit()
        if input_user == "3":
            os.system("cls")
            files = fileslistim()
            if not files:
                print(colored(f"{lang["noFiles"]}\n\n","red"))
                sleep(3)
                return
            else:
                file_num = int(input(f"{lang["selectnumoffile"]}: "))
                if 0 < file_num and file_num <= len(files):
                    selected_file = files[int(file_num)-1]
                    end_name = input(f"{lang['inputname']}: ")
                    factor = int(input(f"{lang['question']} (2-4)\n"))
                    if factor > 4 or factor < 2:
                        print(colored(f"{lang['notsupportedsize']}",'red'))
                        factor=2
                    upscale_pil(selected_file,end_name+".png",factor)
        if input_user == "4":
            os.system('cls')
            files = fileslistsounds()
            if not files:
                print(colored(f"{lang['noFiles']}\n\n","red"))
                sleep(3)
                return
            else:
                file_num = int(input(f"{lang['selectnumoffile']}: "))
                if 0 < file_num and file_num <= len(files):
                    selected_file = files[int(file_num)-1]
                    sounds(selected_file)
        if input_user == "2":
            os.system("cls")
            files = fileslist()
            if not files:
                print(colored(f"{lang['noFiles']}\n\n","red"))
                sleep(3)
                return
            else:
                file_num = int(input(f"{lang['selectnumoffile']}: "))
                if 0 < file_num and file_num <= len(files):
                    selected_file = files[int(file_num)-1]
                    ext = os.path.splitext(selected_file)[1]
                    convertations = supported_extensions(ext)
                    if not convertations:
                        print(colored(f"\n{lang['notsupportedconvetr']} {ext}","red"))
                        sleep(3)
                        return
                    print(f"\n{lang["conversionTypes"]} {selected_file}:")
                    for i, ext in enumerate(convertations, 1):
                        print(f"{i}. {ext}")
                    ext_num = int(input(f"\n{lang["selectFormat"]}: ")) - 1
                    if ext_num < 0 or ext_num >= len(convertations):
                        print(colored(f"{lang["invalidFormat"]}","red"))
                        return
                    output_ext = convertations[ext_num]
                    output_file = os.path.splitext(selected_file)[0] + output_ext

                    confirm = input(f"\n{lang['confirmConvert']} {selected_file} -> {output_file}? (y/n): ").lower()
                    if confirm != 'y':
                        print(lang["canceled"])
                        return
                    convertation(selected_file,output_ext)
                else:
                    print(colored(lang["invalidNum"], "red"))
                    sleep(3)
                    return

    if __name__ == "__main__":
        while True:
            asyncio.run(main())
else:
    os.mkdir("qrcodes")
    os.mkdir("sounds")
    langs = input("Язык / Language? (ru / en) ")
    if langs == "ru" or langs == "en":
        lang = ru_lang if langs == "ru" else en_lang
        f = open('.env', "w")
        print(lang['hi'])
        use = input(lang['use'] )
        if use != 'y':
            f.write(f"ID = -1\nHASH = -1\nLANG = {langs}")
        else:
            print(lang['tutorial'])
            ID = input("API_ID: ")
            HASH = input("API_HASH: ")
            f.write(f"ID = {ID}\nHASH = {HASH}\nLANG = {langs}")
            print(lang['sorry'])
        f.close()
        print("Перезапустите программу / Restart programm")
        sleep(5)
    else:
        print("This language not supported")

