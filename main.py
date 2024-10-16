from virtual_assistant import *

if __name__ == '__main__':
    msg = audio_to_text()
    talk('Has dicho '+msg)
    