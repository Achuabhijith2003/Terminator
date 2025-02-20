import pyttsx3

class Speaker:
    def __init__(self):
        # Initialize the text-to-speech engine here
        pass

    def speak(self, text, voice_id=None):
        engine = pyttsx3.init()
        if voice_id:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[voice_id].id)
        else:
            # Set a default robot-like voice if no voice_id is provided
            voices = engine.getProperty('voices')
            for voice in voices:
                if 'robot' in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break
        engine.say(text)
        engine.runAndWait()

    def stop_speaking(self):
        # Stop any ongoing speech
        pass