<h1 align="center">🌿 Binary - Assistente de Voz da binary 🌿</h1>

<p align="center">
  Uma IA offline feita com Python, voz serena e comandos mágicos — inspirada na força de <strong>Otin</strong>, orixá caçadora e guardiã da mata.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/voz-feminina-%23a3d2ca" />
  <img src="https://img.shields.io/badge/comandos-por%20voz-%2386BBD8" />
  <img src="https://img.shields.io/badge/estilo-místico-%23b2f7ef" />
</p>

---

## ✨ Funcionalidades

- 🎙️ Reconhecimento de voz em português (pt-BR)
- 🗣️ Voz feminina e suave com personalidade própria
- 🌀 Comandos mágicos:
  - Abrir VS Code, navegador e Spotify
  - Falar a hora e a data
  - Previsão do tempo em Feira de Santana
  - Horóscopo diário de Áries ♈
  - Lembrar de beber água 💧
- 🌿 Frases afetuosas no estilo  — serena, firme e encantadora

---

## 🚀 Como usar

### 1. Clone o projeto

```
git clone https://github.com/seu-usuario/binary-assistente.git
cd binary-assistente
```
<h1 2. Instale as dependências </h1>

pip install -r requirements 

```
pip install -r requirements.txt
```
<h1 3. Configure sua chave da API do OpenWeather </h1>

Cadastre-se em openweathermap.org e cole sua chave no código: 

```
OPENWEATHER_API_KEY = "sua_chave_aqui
```
<h1 4. Execute a Binary </h1>

  ```
  python binary_assistente.py
```

🎨 Personalização

🔧 Altere a voz:

No código, use este trecho para listar vozes disponíveis:

import pyttsx3
voz = pyttsx3.init()
for i, v in enumerate(voz.getProperty('voices')):
    print(f"[{i}] {v.name} - {v.id}")

Depois, escolha uma e troque aqui:

voz.setProperty("voice", voz.getProperty('voices')[1].id)

🛠️ Adicione mais comandos no trecho responder_geral(comando)

🎵 Altere o caminho do Spotify no abrir_aplicativo(comando)


🌙 Sobre a Binary

    “Entre o silêncio e a coragem, encontro a minha força.”
    — Binary, a voz da Lory com alma de Otin

A Binary não é só uma assistente, é uma extensão da sua espiritualidade, da sua mente criativa e da sua presença como filha da floresta digital. 🌿✨
📁 Requisitos

    Python 3.8 ou superior

    Microfone funcionando

    Sistema: Windows 64 bits

    Internet (somente para clima)

📄 Licença

Este projeto é livre para uso pessoal e estudo.
Se usar ou modificar, dê os créditos à criadora e mantenha a essência viva. 🌿
💚 Criado por
<table> <tr> <td align="center"> <img src="https://avatars.githubusercontent.com/u/ramoslory" width="100px;" alt="lordev"/><br /> <sub><b>lorydev</b></sub><br /> 🧬 Programadora <br /> 🌐 Instagram: <a href="https://instagram.com/lorytyotin">@lorytyotin</a> </td> </tr> </table> ```





