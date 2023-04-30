import speech_recognition as srg
import pyaudio
import wave

class GrabInfo():
    def __init__(self):
        self.audio = None

info = ""
def start():
   global info
   info = GrabInfo() 

def recordLive():
   recog = srg.Recognizer()
   while True:
        
        try:
            with srg.Microphone() as mic:
                recog.adjust_for_ambient_noise(mic, duration=0.2)
                info.audio = recog.listen(mic)
                print("listened")
                break
        except:
            recog = srg.Recognizer()
            continue
        
def recordFile(url):
    recog = srg.Recognizer()
    # source = wave.open(f"{url}", "rb")
    with srg.AudioFile(url) as source:
        info.audio = recog.record(source)
    # source.close()

def recognite(lan="en-US"):
    print(f"\n\n{info.audio}\n\n")
    info.audio = print(srg.Recognizer().recognize_google(info.audio))

#-----------------
#-----------------
#-----------------
# API
def mainGrab(url, file=False, recordBin=False,):
    start()
    if file: 
        recordFile(url)
    if recordBin:
        recordLive()
    recognite()
    return info.audio
    

