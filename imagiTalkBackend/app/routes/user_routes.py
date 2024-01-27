from app import app
from flask import request, jsonify, make_response
import cohere
import os

# ========== ROUTE TO CHECK API RUNS ==========
@app.route('/', methods=['GET'])
def check_for_run():
    return jsonify({'message': 'API runs successfully'}), 201