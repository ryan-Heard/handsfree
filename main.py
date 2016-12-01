import speech_recognition as sr
import oscommands
# obtain audio from the microphone


def main():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        translated = r.recognize_google(audio).lower()
        if "jarvis" in translated:
            print("Hello Father")

            if 'terminal' in translated:
                oscommands.open_terminal()

        print("Google Speech Recognition thinks you said " + translated)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

main()
