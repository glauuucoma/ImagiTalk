from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_cors import CORS

# Initialize Flask App
app = Flask(__name__)
# This will enable CORS for all routes and domains
CORS(app, supports_credentials=True)  

# Setup Config
app.config.from_object(Config)

# Setup Database
db = SQLAlchemy(app)

# from app.routes import user_routes, cohere_routes
from app.routes import user_routes, character_routes, cohere_routes