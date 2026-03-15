from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8713407324:AAEoTjqeHkV9zIYzDg7B7Brl0M1mM3mtp1Q"
CHAT_ID = "-1001234567890"  # sem dej ID supergroup

@app.route("/report", methods=["POST"])
def report():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    expected = data.get("expected")
    priority = data.get("priority")

    message = f"🐞 *Ladíme to - Sweetcafe admin*\n\n*Title:* {title}\n*Description:* {description}\n*Expected:* {expected}\n*Priority:* {priority}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=5000)
