import playsound
import speech_recognition as sr
from googletrans import Translator
import gtts
input_lang = "en"
output_lang = "hi"

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use a context manager for the microphone
with sr.Microphone() as source:
    print("Speak now")

    # Listen to the audio
    voice = recognizer.listen(source)

    # Recognize the speech using Google Web API and specify the language as French
    try:
        text = recognizer.recognize_google(voice, language=input_lang)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Google Web API could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web API; {e}")

# Initialize the translator
translator = Translator()

# Translate the recognized text to another language (e.g., English)
translated_text = translator.translate(text, dest=output_lang)

print("Translation to french:", translated_text.text)

converted_audio = gtts.gTTS(translated_text.text, lang=output_lang)

converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")


