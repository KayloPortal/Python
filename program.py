import grabrecognize as fg
import extractions as ex

# View Functions
def dictToChart(dict):
    pass

# UI
class UiInfo:
    def __init__(self):
        self.url = ""
        self.text = ""
        self.wanted = ""
        self.words = {}
        self.letters = {}

#  UI Functions
info = UiInfo()
def FileUrl():
    info.url = input("Type the url of the file and press enter(wave file) \n")
    info.text = fg.mainGrab(info.url, file=True)

def recordMic():
    info.text = fg.mainGrab("", recordBin=True)

def showInfo():
    print(choicesInfo[state])

def extract():
    if extraction_method == 3:
        info.words, info.letters = ex.mainExtractor(info.text, both=True)
    elif extraction_method == 1:
        info.words, info.letters = ex.mainExtractor(info.text, words=True)
    elif extraction_method == 2:
        info.words, info.letters = ex.mainExtractor(info.text, letters=True)

# Informations Variubles, Linking and callbacks
state = -1
recognize_methods = {
    "1": FileUrl,
    "2": recordMic,
    "i": showInfo
}

extraction_methods = {
    "1" : extract,
    "2" : extract,
    "3" : extract,
    "i": showInfo
}

choicesInfo = {
    "Choose the source you want to recognize it, It can be an audio file(1) or real-time recording(2)",
    "What do you want to extract from the file? words(1), letters(2) or both(3)?"
}

# App start

print("""
- Hello, I can recognize any sound and convert it to text. Choose your methods and be ready.
- GUIDE: You should type your choice's number, and create a code with them. for example: 1 1 2. if you want information about the choice, leave "i" instead of the number.
""")

recognize_method = input("""
- Recognize
1. An Audio File
2. Real-Time Record
""").strip().lower()
state += 1
recognize_methods [ recognize_method ] ()

extraction_method = input("""- Extract:
1. Words
2. Letters
3. Both
""").strip().lower()
state += 1
extraction_methods [ extraction_method ] ()

print(info.words, "\n", info.letters)
