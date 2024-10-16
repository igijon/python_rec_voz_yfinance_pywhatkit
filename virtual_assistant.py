import datetime
import pyttsx3
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
        
def talk(msg):
    # Encender motor pyttsx3
    engine = pyttsx3.init()
    
    engine.setProperty('voice', 'com.apple.eloquence.es-ES.Rocko')
    
    # Pronunciar mensjaje
    engine.say(msg)
    engine.runAndWait()
    
def get_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f"Voz {i}")
        print(f"Id {voice.id}")
        print(f"Nombre {voice.name}")
        print(f"Idioma {voice.languages}")
        print(f"Género {voice.gender}")
        print(f"Género {voice.age}")
        print(f"---------------------------")
        
def get_day():
    day = datetime.date.today()
    weekday = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }
    return weekday[day.weekday()]