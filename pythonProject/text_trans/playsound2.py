from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
text="워후 신기하구만"
tts = gTTS(text = text, lang="ko")
tts.save("hi.mp3")
playsound("hi.mp3")