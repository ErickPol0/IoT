from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    # Handle the GitHub webhook event data here
    # You can perform actions based on the event type and payload
    
    print("Received GitHub webhook event:")
    print(json.dumps(data, indent=4))

    return jsonify({'message': 'Webhook received successfully'}), 200

if __name__ == '__main__':
    app.run(port=5000)
