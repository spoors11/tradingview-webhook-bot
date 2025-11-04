from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert:", data)

    action = data.get("action")
    side = data.get("side")
    symbol = data.get("symbol")
    price = data.get("price")

    # TODO: Add your broker API order logic here
    if action == "enter":
        print(f"Place {'BUY' if side=='long' else 'SELL'} order for {symbol} at {price}")
    elif action == "exit":
        print(f"Close {side} position for {symbol}")

    return jsonify({"status": "success"})

@app.route('/')
def home():
    return "TradingView Webhook Bot is running."

if __name__ == '__main__':
    app.run()
