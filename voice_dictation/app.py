from gtts import gTTS
import playsound

text_to_speech = "Hello, this is an example of using gTTS in Python."
tts = gTTS(text=text_to_speech, lang='en')
tts.save("example.mp3")

# Play the generated audio using playsound
playsound.playsound("example.mp3")
