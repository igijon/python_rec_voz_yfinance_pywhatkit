import datetime
import pyttsx3
import speech_recognition as sr
import yfinance as yf
import webbrowser

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
    newVoiceRate = 180
    
    # Encender motor pyttsx3
    engine = pyttsx3.init()
    
    engine.setProperty('voice', 'com.apple.eloquence.es-ES.Monica')
    engine.setProperty('rate', newVoiceRate)
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
        
def say_day():
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
    talk(f'Hoy es {weekday[day.weekday()]}')
    
def say_hour():
    hour = datetime.datetime.now()
    talk(f'En este momento son las {hour.hour} horas y {hour.minute} minutos')
    
def saludo():
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        momento = 'Buenas noches.'
    elif 6 <= hour.hour < 13:
        momento = 'Buenos días.'
    else:
        momento = 'Buenas tardes.'
    talk(f'{momento} Soy Lía, tu asistente personal. Por favor, dime en qué puedo ayudarte.')
    
def requests():
    saludo()
    stop = False
    while not stop:
        #Activar el micro y guardar la request en un string
        request = audio_to_text().lower()
        if 'abrir youtube' in request:
            talk('Abriendo youtube')
            webbrowser.open('https://www.youtube.com')
        elif 'abrir navegador' in request:
            talk('Abriendo navegador.')
            webbrowser.open('https://www.google.com')
        elif 'qué día es hoy' in request:
            say_day()
        elif 'qué hora es' in request:
            say_hour()
        elif 'precio de las acciones de' in request:
            company = request.split('precio de las acciones de').pop().strip()
            ticker = get_ticker(company)
            price = get_stock_price(ticker)
            msg = f'El precio de las acciones de {company} es {price} euros'
            talk(msg)
            
def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    # Obtener los datos históricos (último día disponible)
    history = stock.history(period="1d")
    closing_price = history['Close'].iloc[0] # Para acceder por posicón
    return closing_price

def get_ticker(msg):
    companies = {
        'AAPL': 'Apple Inc',
        'MSFT': 'Microsoft Corporation',
        'GOOGL': 'Alphabet Inc. Google',
        'AMZN': 'Amazon.com Inc',
        'META': 'Meta Plattforms, Inc (Facebook)',
        'TSLA': 'Tesla Inc.',
        'NVDA': 'NVIDIA Corporation',
        'INTC': 'Intel Corporation',
        'AMD': 'Advanced Micro Devices, Inc. (AMD)',
        'NFLX': 'Netflix, Inc',
        'CSCO': 'Cisco Systems, Inc',
        'PYPL': 'PayPal Holdings, Inc',
        'CRM': 'Salesforce, Inc',
        'ADBE': 'Adobe Inc',
        'SPOT': 'Spotify Technology S.A',
        'ZM': 'Zoom Video Comunications, Inc',
        'TWTR': 'Twitter, Inc',
    }
    
    for k,v in companies.items():
        if msg.lower() in v.lower():    
            return k
    return ''
