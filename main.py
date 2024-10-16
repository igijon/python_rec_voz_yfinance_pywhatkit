from virtual_assistant import *

if __name__ == '__main__':
    getVoices()
    talk('Mi nombre es Ian, puedes comenzar a hablar')
    msg = audio_to_text()
    talk('Has dicho '+msg)
    