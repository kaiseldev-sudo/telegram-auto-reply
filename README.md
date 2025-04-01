# Telegram Auto-Reply Bot

A Python bot that automatically sends messages to a Telegram group at regular intervals.

## Features
- Sends random messages from a predefined list.
- Runs continuously until manually stopped.
- Stops automatically after sending 40 messages.
- Uses `.env` file to store API credentials securely.

## Prerequisites
Ensure you have the following installed:
- Python 3.10+
- [Telethon](https://docs.telethon.dev/) library

## Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/tg-auto-reply.git
cd tg-auto-reply
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Create a `.env` File
Create a `.env` file in the project root and add your Telegram API credentials:
```
API_ID=your_api_id
API_HASH=your_api_hash
PHONE_NUMBER=your_phone_number
GROUP_LINK=t.me/yourgroup
```

### 4️⃣ Run the Bot
```bash
python tg-auto-reply.py
```

## Usage
- The bot sends a random message every **65 seconds**.
- It automatically stops after **40 messages**.
- To stop manually, use `CTRL + C`.

## Prevent `.env` from Being Pushed to GitHub
Ensure you have a `.gitignore` file with:
```
.env
__pycache__/
session_name.session
```

## License
MIT License

---
Feel free to contribute and improve this bot! 🚀

