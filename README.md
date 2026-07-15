# 🤖 DevMate

<p align="center">
  <img src="assets/logo.png" alt="DevMate Logo" width="180"/>
</p>

<p align="center">
  <b>Your AI Developer Assistant on Telegram.</b><br>
  Build, debug, learn and code smarter—right from your chat.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge\&logo=docker)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge\&logo=telegram)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge\&logo=render)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Version](https://img.shields.io/badge/v0.2.0-Live-orange?style=for-the-badge)

</p>

---

## ✨ Overview

**DevMate** is an AI-powered Telegram bot designed to be your personal developer companion.

Instead of switching between websites, terminals, documentation, and AI chat applications, DevMate brings everything directly into Telegram.

Whether you're debugging code, asking programming questions, generating secure passwords, creating hashes, or simply learning a new technology, DevMate is always one message away.

It supports multiple AI providers through a clean abstraction layer, allowing seamless switching between **Google Gemini** and **Ollama** without changing the application logic.

---

# 🚀 Features

* 🤖 AI-powered developer assistant
* 💬 Natural conversational chat
* 🧠 Per-chat conversation memory
* 🔄 Multi-provider AI (Gemini & Ollama)
* 🎛️ Interactive Telegram UI
* 🧹 One-click conversation reset
* 🔐 Secure password generation
* 🔒 SHA-256 hashing
* 🆔 UUID generation
* 📝 Structured logging
* 🏗️ Modular architecture
* 🐳 Docker support
* ☁️ Production-ready deployment

---

# 🛠 Tech Stack

* Python 3.13
* python-telegram-bot
* Google Gemini API
* Ollama
* Docker
* Docker Compose
* Render
* Git & GitHub

---

# 🏗 Architecture

```text
                     Telegram

                         │

                         ▼

               python-telegram-bot

                         │

          ┌──────────────┴──────────────┐
          ▼                             ▼

      Command Handlers           Chat Handler

                         │

                         ▼

                Conversation Memory

                         │

                         ▼

                 AI Provider Layer

              ┌──────────┴──────────┐
              ▼                     ▼

        Gemini Provider      Ollama Provider

              │                     │

              ▼                     ▼

      Google Gemini API       Local LLM
```

DevMate follows a provider-based architecture where Telegram handlers remain completely independent of the underlying AI model. The AI provider layer routes requests to the configured backend, making it easy to add new providers in the future.

---

# 🧠 AI Providers

Switch between providers using environment variables.

### Gemini

```env
AI_PROVIDER=gemini
```

### Ollama

```env
AI_PROVIDER=ollama
OLLAMA_MODEL=llama3.2:3b
```

---

# 📂 Project Structure

```text
DevMate/
│
├── handlers/
├── services/
├── prompts/
├── utils/
├── config.py
├── logger.py
├── main.py
├── health_server.py
├── Dockerfile
├── compose.yaml
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## Clone

```bash
git clone https://github.com/dev-krish/DevMate.git

cd DevMate
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

```bash
cp .env.example .env
```

Example:

```env
BOT_TOKEN=your_bot_token

AI_PROVIDER=gemini

GEMINI_API_KEY=your_api_key

OLLAMA_MODEL=llama3.2:3b
```

---

## Run

```bash
python main.py
```

---

# 🐳 Docker

```bash
docker compose up --build
```

---

# ☁ Deployment

DevMate can be deployed using Docker on:

* Render
* Railway
* VPS
* AWS EC2
* Oracle Cloud

---

# 🛣 Roadmap

## ✅ v0.2

* AI Provider Abstraction
* Conversation Memory
* Interactive UI
* Gemini Support
* Ollama Support
* Docker Deployment
* Render Deployment

## 🚧 v0.3

* AI Developer Commands
* Code Review
* Debug Assistant
* Commit Message Generator
* GitHub Integration

## 🔮 Future

* QR Code Generator
* Base64 Utilities
* JSON Formatter
* Plugin System
* Conversation Persistence
* RAG Support

---

# 🤝 Contributing

Contributions, feature requests and bug reports are always welcome.

If you'd like to improve DevMate, feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

<p align="center">

Made with ❤️ by **Krishnendu Dutta**

If you found this project useful, consider giving it a ⭐ on GitHub!

</p>
