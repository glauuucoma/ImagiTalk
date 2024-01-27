from app import app
import cohere
import os

from dotenv import load_dotenv
from flask import request, jsonify

load_dotenv()

cohere_key = os.getenv("COHERE_KEY")
co = cohere.Client(cohere_key)

@app.route('/api/cohere/generate', methods=['POST'])
def generate_text():
    userPrompt = request.json
    response = co.generate(
        prompt=userPrompt["data"]
    )
    response_str = str(response)
    
    return jsonify({"result": response_str})

