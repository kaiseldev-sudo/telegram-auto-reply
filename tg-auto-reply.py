import random
import asyncio
import os
from dotenv import load_dotenv  # Import dotenv
from telethon import TelegramClient

# Load environment variables from .env file
load_dotenv()

API_ID = int(os.getenv("API_ID"))  # Convert to int
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
GROUP_LINK = os.getenv("GROUP_LINK")

random_replies = [
    "Access a marketplace of AI models.",
    "Evaluate AI performance with standardized metrics.",
    "Stay updated with latest AI advancements.",
    "Ensure compliance with data privacy regulations.",
    "Utilize blockchain for verifiable AI inference.",
    "Enhancing AI capabilities in decentralized applications.",
    "Integrate AI models effortlessly into projects.",
    "Optimize AI performance within Web3 ecosystems.",
    "Collaborate with a community of AI enthusiasts.",
    "Access diverse datasets for model training.",
    "Inferium supports multi-chain blockchain interoperability.",
    "Experience low-cost, high-speed AI solutions.",
    "Monitor AI operations with real-time dashboards.",
    "Empowering developers with robust inference APIs.",
    "Facilitating secure AI computations on sensitive data.",
    "Inferium integrates with leading cloud infrastructures.",
    "Inferium simplifies AI model selection.",
    "Experience seamless AI inference deployment.",
    "Keep grinding, Inferium is the future! 🔥",
    "Don't fade Inferium, it's just getting started! 🚀",
    "AI + Blockchain = Inferium dominance! 💡",
    "Inferium fam, we moon soon! 🌕",
    "Only legends are early to Inferium! ⏳",
    "Betting big on Inferium's innovation! 📈",
    "AI-powered crypto? Inferium is leading the charge! 🚀",
    "We build, we innovate, we send! 💪",
    "Inferium is not a trend, it's the future! 🌍",
    "Early adopters win big! Don't sleep on Inferium! ⏳",
    "Bullish on Inferium, LFG! 🚀",
    "Smart money is moving into Inferium! 🧠💰",
    "Inferium is the alpha. Do your own research! 🔍"
]

client = TelegramClient("session_name", API_ID, API_HASH)

async def send_messages():
    await client.start(PHONE_NUMBER)
    print("Bot started. Waiting before sending the first message...")

    await asyncio.sleep(2)  # Wait before the first message

    message_count = 0  # Counter for the number of messages sent

    while message_count < 40:  # Stop after sending 40 messages
        message = random.choice(random_replies)  # Pick a random message
        print(f"Sending message: {message}")

        try:
            await client.send_message(GROUP_LINK, message)
            print("Message sent!")
            message_count += 1  # Increment the message count
        except Exception as e:
            print(f"Error sending message: {e}")

        if message_count < 40:  # Only wait if it's not the last message
            print("Waiting 5 minutes before the next message...")
            await asyncio.sleep(65)  # Wait 5 minutes before sending the next message

    print("Sent 40 messages. Stopping bot...")

if __name__ == "__main__":
    asyncio.run(send_messages())
