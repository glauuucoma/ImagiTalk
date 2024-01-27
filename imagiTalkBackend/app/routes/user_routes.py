from app import app, db
from flask import request, jsonify, make_response
import cohere
import json
from os
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for
from app.models.user import User

# Locating and using env vars
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Initializing Auth0
app.secret_key = env.get("APP_SECRET_KEY")
oauth = OAuth(app)
oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

# ========== ROUTE TO CHECK API RUNS ==========
@app.route('/', methods=['GET'])
def check_for_run():
    return jsonify({'message': 'API runs successfully'}), 201

# ========== LOGIN ROUTE ==========
@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=env.get("REDIRECT_URI")
    )

# ========== CALLBACK FOR AUTH0 ==========
@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token

    user = session.get("user")
    username = user["userinfo"]["nickname"]
    email = user["userinfo"]["email"]
    profile_picture = user["userinfo"]["picture"]
    updated_at = user["userinfo"]["updated_at"]

    # Check if the user already exists
    existing_user = User.query.filter(User.username == username).first()
    if existing_user:
        return jsonify({'message': 'Username or email already exists'}), 400

    # Create a new user if the user doesn't exist already
    new_user = User(username=username, email=email, profile_picture=profile_picture, updated_at=updated_at)

    # Add the new user to DB
    try:
        db.session.add(new_user)
        db.session.commit()

        # Create a response object
        response = make_response(jsonify({"message": "User registered successfully"}), 201)
        return response

    except Exception as e:
        db.session.rollback()

        # Handle any exceptions, such as database errors
        return jsonify({'message': 'Failed to register user. Server Error.', 'error': str(e)}), 500

# ========== LOGOUT ROUTE ==========
@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": env.get("REDIRECT_URI_LOGOUT"),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )