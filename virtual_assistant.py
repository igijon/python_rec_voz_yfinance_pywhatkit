import pyttsx3
import pyaudio
import speech_recognition as sr

def audio_to_text():
    
    # Recognizer
    r = sr.Recognizer()
    
    # Configuramos el micro
    with sr.Microphone() as origin:
        # Tiempo de espera desde que se activa el micro
        r.pause_threshold = 0.8
        
        # Informamos que comienza la grabación
        print('Puedes comenzar a hablar')
        
        # Guardar audio
        audio = r.listen(origin)
        
        try:
            # Buscar en google lo que hemos escuchado
            text = r.recognize_google(audio, language='es-es')
            return text
        except sr.UnknownValueError:
            print('Ups, no te entendí')
            return 'Esperando'
        except sr.RequestError:
            print('Ups, sin servicio')
            return 'Esperando'
        except:
            print('Ups, algo ha salido mal')
            return 'Esperando'