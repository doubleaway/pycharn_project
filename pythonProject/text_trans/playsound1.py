#글자를 음성으로 바꾸기
from gtts import gTTS
text = "안녕하세요. 파이썬과 40개의 작품들입니다."
tts = gTTS(text = text, lang='ko')
tts.save(r"hi.mp3")
