from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.json  # Assuming incoming data is in JSON format

    # Process the webhook data as needed
    # You can perform any desired actions with the data received

    print("Received webhook:", data)

    return 'Webhook received successfully', 200

if __name__ == '__main__':
    app.run(debug=True,host='192.168.50.3')
