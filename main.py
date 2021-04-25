from gtts import gTTS
import os.path

# The text file should be located in the project directory. Text encoding — ANSI.
filename = "article.txt"

# Checking the existence of the file in the folder and read it
if os.path.isfile(filename):
    with open(filename, "r") as file:
        text = file.read()
else:
    print(f"file {filename} doesn't exist")

# Choosing the language for reading
lang = None
while (lang != "1") and (lang != "2") and (lang != "3"):
    lang = input("Choose the language (1/2/3 for ua/eng/ru): ")
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
if lang == "1":
    print("Готово. Насолоджуйся читанням.")
elif lang == "2":
    print("Done. Enjoy your reading")
elif lang == "3":
    print("Есть. Наслаждайся чтением.")
