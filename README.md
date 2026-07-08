# 🤖 DevMate

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render)
![Version](https://img.shields.io/badge/version-v0.1.0-orange?style=for-the-badge)

<div align="center">

An AI-powered developer assistant for Telegram.

Ask coding questions, generate passwords, create hashes, generate UUIDs, and chat with powerful AI models—all without leaving Telegram.

Supports Gemini ☁️ and Ollama 🖥️ through a clean provider abstraction layer.

</div>

✨ Features
🤖 AI-powered developer assistant
🧠 Natural language conversations
🔄 Switch between Gemini and Ollama
🔐 Secure password generation
🔒 SHA-256 hashing
🆔 UUID generation
🐳 Docker support
☁️ Render deployment
📝 Structured logging
🧩 Modular architecture
## 🛠️ Tech Stack

- Python 3.13
- python-telegram-bot
- Docker
- Docker Compose
- Render
- Git & GitHub

## 🏗️ Architecture

```text
                Telegram

                    │

                    ▼

           python-telegram-bot

                    │

                    ▼

             handlers/chat.py

                    │

                    ▼

          services/ai_service.py

           ┌────────┴────────┐
           │                 │
           ▼                 ▼

     Gemini Service     Ollama Service

           │                 │
           ▼                 ▼

      Google Gemini      Local Llama/Qwen
```

DevMate follows a modular architecture where Telegram handlers remain independent of the underlying AI provider. The `ai_service` routes requests to the configured provider, allowing seamless switching between Gemini and Ollama without changing application logic.

## 🧠 AI Providers

DevMate supports multiple AI providers through a unified service layer.

| Provider | Purpose                                                |
| -------- | ------------------------------------------------------ |
| Gemini   | Cloud AI with fast responses and strong reasoning      |
| Ollama   | Local AI for offline development and unlimited testing |

Switch providers by updating your environment configuration:

```env
AI_PROVIDER=gemini
```

or

```env
AI_PROVIDER=ollama
```

For Ollama:

```env
OLLAMA_MODEL=llama3.2:3b
```


## 📂 Project Structure

```text
DevMate/
├── handlers/
├── services/
├── utils/
├── config.py
├── logger.py
├── main.py
├── Dockerfile
├── compose.yaml
├── requirements.txt
└── README.md
```

## 🚀 Running Locally

### Clone the repository

```bash
git clone https://github.com/dev-krish/DevMate.git
cd DevMate
```

### Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

```bash
cp .env.example .env
```

Add your Telegram Bot Token to `.env`:

```env
BOT_TOKEN=your_bot_token_here
```

### Start the bot

```bash
python main.py
```

## 🐳 Running with Docker

```bash
docker compose up --build
```

## 📦 Deployment

DevMate is containerized with Docker and can be deployed on platforms such as:

- Render
- Railway
- VPS
- AWS EC2
- Oracle Cloud

## 🗺️ Roadmap

- [x] Docker Support
- [x] Cloud Deployment
- [x] Structured Logging
- [ ] QR Code Generator
- [ ] Base64 Encoder/Decoder
- [ ] JSON Formatter
- [ ] GitHub Integration
- [ ] AI Commands

## 🔮 Why DevMate ?

DevMate was built to provide developers with quick utilities directly inside Telegram. Instead of opening multiple websites or command-line tools, common development tasks can be completed with simple bot commands.

## 🤝 Contributing

Contributions, suggestions and feature requests are welcome.

## 📄 License

This project is licensed under the MIT License.

---

Made with ❤️ by Krishnendu Dutta.