from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from gtts import gTTS
import sys

uri = "mongodb+srv://<accountname>:<password>@test.gdq2ua6.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

def textToVoice(text):
    text = text
    tts = gTTS(text, lang="en")
    tts.save("tov.mp3")
    return print("Done.. Please check the saved file in you directory.")


def keywordFinder(data, keyword):
    data = data
    keyword = keyword
    filtered = []
    for book in data:
        if str(book).__contains__(keyword):
            filtered.append(book)
    return print(filtered)


def __name__():
    print("Press 0: to find book by keyword.")
    print("Press 1: to convert text in voice.")
    Number = int(input("Enter your no: "))
    if Number == 0:
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            keyword = str(input("Enter your keyword: "))
            db = client.get_database(client.list_database_names()[0])
            collects = db[db.list_collection_names()[0]]
            books = []
            for data in collects.find():
                books.append(data)
            keywordFinder(books, keyword)
        except Exception as e:
            print(e)
    else:
        input("Enter your text: ")
        user_input = sys.stdin.readlines()
        text = ''.join(user_input)
        textToVoice(text)


def __init__():
    __name__()


__init__()

client.close()