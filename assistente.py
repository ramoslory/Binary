import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import requests

# === CONFIG ===
OPENWEATHER_API_KEY = "9ea5036f73f0dec376acbeb000c9ae31"  # Coloque sua chave da OpenWeather (opcional)

# === VOZ ===
voz = pyttsx3.init()
voz.setProperty("rate", 160)
voz.setProperty("voice", voz.getProperty('voices')[0].id)

def falar(texto):
    print("Binary 🌿:", texto)
    voz.say(texto)
    voz.runAndWait()

# === OUVIR COMANDO ===
def ouvir():
    ouvinte = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Ouvindo...")
        audio = ouvinte.listen(source)
        try:
            comando = ouvinte.recognize_google(audio, language='pt-BR')
            print("Você disse:", comando)
            return comando.lower()
        except sr.UnknownValueError:
            falar("Não entendi, minha caçadora de código. Pode repetir?")
        except sr.RequestError:
            falar("Problemas ao conectar com o reconhecimento de voz.")
        return ""

# === COMANDOS DE APPS ===
def abrir_aplicativo(comando):
    if "navegador" in comando:
        webbrowser.open("https://www.google.com")
        falar("Abrindo seu navegador de possibilidades.")
    elif "vs code" in comando or "visual studio" in comando:
        os.system("code")
        falar("VS Code na tela. Prepare o feitiço do código!")
    elif "spotify" in comando:
        caminho = r"C:\Users\SeuUsuario\AppData\Roaming\Spotify\Spotify.exe"  # Altere aqui
        os.startfile(caminho)
        falar("Tocando as vibrações do momento.")

# === COMANDO: CLIMA ===
def clima_feira():
    try:
        cidade = "Feira de Santana"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={OPENWEATHER_API_KEY}&lang=pt_br&units=metric"
        resposta = requests.get(url).json()

        temp = resposta['main']['temp']
        descricao = resposta['weather'][0]['description']
        falar(f"Em Feira de Santana agora está {temp:.1f} graus, com {descricao}. Leve sua coragem e talvez um casaquinho.")

    except:
        falar("Não consegui buscar o clima agora. Tente mais tarde.")

# === COMANDO: HORÓSCOPO ===
def horoscopo_aries():
    # Simples exemplo de horóscopo fixo
    mensagem = "Áries, sua força hoje está na coragem de começar. Entre o silêncio e a ação, você encontrará poder. 🌿✨"
    falar(mensagem)

# === COMANDO: LEMBRETE ÁGUA ===
def lembrar_agua():
    falar("Lory, que tal beber um pouco de água agora? A mente precisa de rios pra fluir bem.")

# === RESPOSTAS GERAIS ===
def responder_geral(comando):
    if "oi" in comando:
        falar("Oi minha estrela dos algoritmos! 🌟 Como posso iluminar seu dia?")
    elif "que horas são" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        falar(f"Agora são {hora}, tempo perfeito pra criar.")
    elif "data" in comando:
        data = datetime.datetime.now().strftime("%d/%m/%Y")
        falar(f"Hoje é {data}, dia de vitória.")
    elif "clima" in comando or "tempo" in comando:
        clima_feira()
    elif "horóscopo" in comando or "áries" in comando:
        horoscopo_aries()
    elif "beber água" in comando or "lembrar água" in comando:
        lembrar_agua()
    elif "sair" in comando or "fechar" in comando:
        falar("Desligando. Que Otin caminhe com você. 🌿")
        exit()
    else:
        falar("Ainda estou aprendendo isso. Em breve saberei mais.")

# === INICIAR ===
falar("Olá Lory, aqui é a Binary. Estou pronta para te servir com força e serenidade.")

while True:
    comando = ouvir()
    if comando:
        if any(palavra in comando for palavra in ["abrir", "executar"]):
            abrir_aplicativo(comando)
        else:
            responder_geral(comando)
