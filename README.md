# 🤖 DevMate

> A developer-focused Telegram bot built with Python to make everyday development tasks faster and easier.

## ✨ Features

- 🔐 Secure Password Generator
- 🔑 SHA-256 Hash Generator
- 🆔 UUID Generator
- 🏓 Ping Command
- 📖 Help Command
- 💬 Echo Messages

## 🛠️ Tech Stack

- Python 3.13
- python-telegram-bot
- Docker
- Docker Compose
- Render
- Git & GitHub

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

## 🤝 Contributing

Contributions, suggestions and feature requests are welcome.

## 📄 License

This project is licensed under the MIT License.