import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random", timeout=10)
        data = res.json()[0]

        quote = data.get("q", "")
        author = data.get("a", "Unknown")

        return f'Daily Motivation:\n\n"{quote}"\n\n- {author}'

    except Exception as e:
        return f"Error fetching quote: {e}"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    res = requests.post(url, data=payload)

    # 🔥 IMPORTANT DEBUG
    print("Status Code:", res.status_code)
    print("Response:", res.text)

if __name__ == "__main__":
    print("TOKEN:", TOKEN)
    print("CHAT_ID:", CHAT_ID)

    msg = get_quote()
    send_to_telegram(msg)
