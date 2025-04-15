import google.generativeai as ai
import os
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

api_key = os.getenv("GEMINI_API_KEY")


ai.configure(api_key=api_key)
model = ai.GenerativeModel("gemini-1.5-pro")



@app.route('/chat', methods=['GET'])
def chat():
    msg = request.args.get("message")
    if not msg:
        return jsonify({'error' : 'Messsage text requires'}), 400

    chat = model.start_chat()
    result = chat.send_message(msg)
    answer = result.text

    return jsonify({'response': answer})


if __name__ == '__main__':
    app.run(debug=True)
