from flask import Flask, render_template, request, redirect, url_for
from services import Services

app = Flask(__name__)

chat_history = []


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", messages=chat_history, title="MIND MATE")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.form.get("message", "").strip()
        if user_message:
            chat_history.append({"sender": "user", "text": user_message})
            bot_response_raw = Services().chatbot_services(user_message)
            bot_response = bot_response_raw["response"]
            chat_history.append({"sender": "bot", "text": bot_response})
        return redirect(url_for("chat"))

    return render_template("chat.html", messages=chat_history, title="MIND MATE")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2025, debug=True)
