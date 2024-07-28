from flask import Flask, request, jsonify
import g4f
from g4f.client import Client

app = Flask(__name__)

@app.route('/')
def index():
    return "Server is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']
    
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_message}],
        provider=g4f.Provider.Chatgpt4o
    )
    
    return jsonify({'response': response.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True)
