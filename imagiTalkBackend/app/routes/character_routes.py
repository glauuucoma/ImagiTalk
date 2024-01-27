from flask import request, jsonify, make_response
from app import app, db
import json
import os
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for
from app.models.user import User
from app.models.character import Character

# Locating and using env vars
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# ========== GET ALL CHARACTERS ROUTE ==========
@app.route('/api/characters', methods=['GET'])
def get_all_characters():
    try:
        characters = Character.query.all()
        results = [
            {
                "id": character.id,
                "character_name": character.character_name,
                "character_picture": character.character_picture
            } for character in characters]

        return jsonify({"message": len(results), "characters": results}), 200
    except Exception as e:
        return jsonify({"message": "Error occurred while getting all characters", "error": str(e)}), 400

# ========== GET CHARACTER BY ID ROUTE ==========
@app.route('/api/characters/<id>', methods=['GET'])
def get_character_by_id(id):
    try:
        character = Character.query.get(id)
        return jsonify({"character": {
            "id": character.id,
            "character_name": character.character_name,
            "character_picture": character.character_picture
        }}), 200
    except Exception as e:
        return jsonify({"message": "Error occurred while getting character", "error": str(e)}), 400