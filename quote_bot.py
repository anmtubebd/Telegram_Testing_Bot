import os
import requests

# GitHub Secrets থেকে Environment Variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=10)
        response.raise_for_status()
        data = response.json()[0]

        quote = data.get("q", "")
        author = data.get("a", "Unknown")

        return f"✨ Daily Motivation ✨\n\n\"{quote}\"\n\n— {author}"
    
    except Exception as e:
        return f"Error fetching quote 😢\n{e}"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()
        print("Message sent successfully ✅")
    except Exception as e:
        print("Failed to send message ❌", e)

if __name__ == "__main__":
    quote = get_quote()
    send_to_telegram(quote)
