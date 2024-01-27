from app import app
import cohere
import os
from dotenv import load_dotenv
from flask import request, jsonify

# Configure environment variables
load_dotenv()

cohere_key = os.getenv("COHERE_KEY")
print("Key: ", cohere_key)
co = cohere.Client(cohere_key)

# ========== API ROUTE TO GET COHERE TEXT GENERATION (BETA) ==========
@app.route('/api/cohere/generate', methods=['POST'])
def generate_text():
    user_prompt = request.json

    # Generate text using cohere API
    response = co.generate(prompt=user_prompt["data"])

    generated_text = response.generations[0].text

    # Return the generated text in a JSON-serializable format
    return jsonify({"result": generated_text})

