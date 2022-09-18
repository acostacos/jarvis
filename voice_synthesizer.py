import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if ('en_US' in voice.languages):
        engine.setProperty('voice', voice.id)
        break

engine.setProperty(
    'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

# Handle throw exception if no available english voice

engine.say("Testing if speech works yay")
engine.runAndWait()
