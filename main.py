from gtts import gTTS
import os.path
import datetime

# The text file should be located in the project directory. Text encoding — ANSI.
filename = "article.txt"

# Checking the existence of the file in the folder and read it
if os.path.isfile(filename):
    with open(filename, "r") as file:
        text = file.read()
else:
    print(f"file {filename} doesn't exist. Check again, please.")

# Choosing the language for reading
lang = None
while (lang != "1") and (lang != "2") and (lang != "3"):
    lang = input("Choose the language (1/2/3 for ua/eng/ru): ")
    date_start = datetime.datetime.now().second
    if lang == "1":
        print("Добре. Конвертую для тебе книгу українською. Це займе трошки часу.")
        obj = gTTS(text, lang="uk")
        obj.save("audiobook_ua.mp3")
    elif lang == "2":
        print("Okay. I am converting a book for you in English. It will take some time.")
        obj = gTTS(text)
        obj.save("audiobook_eng.mp3")
    elif lang == "3":
        print("Хорошо. Конвертирую для тебя книгу на русском. Это займет немного времени.")
        obj = gTTS(text, lang="ru")
        obj.save("audiobook_ru.mp3")
    else:
        print("You must choose one of three languages.")

# Notification of readiness
date_end = datetime.datetime.now().second
if lang == "1":
    print(f"Готово. Насолоджуйся читанням. {date_end - date_start} сек.")
elif lang == "2":
    print(f"Done. Enjoy your reading. {date_end - date_start} sec.")
elif lang == "3":
    print(f"Есть. Наслаждайся чтением. {date_end - date_start} сек.")