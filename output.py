import pyttsx3

engine = pyttsx3.init()
# for voice in engine.getProperty("voices"):
#     print(voice.id, voice)
engine.setProperty('voice',
                   'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0 Microsoft David Desktop - English (United States)')


def say(text):
    engine.say(text)
