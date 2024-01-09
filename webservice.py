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
    app.run(debug=True,host='::',port=5001)
    #http://[2001:ee0:50e8:b2b0:d4c:f0a2:bca1:b8b2]:5001
