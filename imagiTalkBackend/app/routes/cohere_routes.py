# from app import app
# import cohere
# import os
# from dotenv import load_dotenv
# from flask import request, jsonify

# # Configure environment variables
# load_dotenv()

# cohere_key = os.getenv("COHERE_KEY")
# co = cohere.Client(cohere_key)

# # ========== API ROUTE TO GET COHERE TEXT GENERATION (BETA) ==========
# @app.route('/api/cohere/generate', methods=['POST'])
# def generate_text():
#     user_prompt = request.json

#     # Generate text using cohere API
#     response = co.generate(prompt=user_prompt["data"])
    
#     return jsonify({"result": response_str})

