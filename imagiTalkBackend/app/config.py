import os

class Config:
    # ===== POSTGRES DB CONFIG =====
    POSTGRES_DB_USERNAME=os.environ.get('POSTGRES_DB_USERNAME') or None
    POSTGRES_DB_PASSWORD=os.environ.get('POSTGRES_DB_PASSWORD') or None
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_DB_USERNAME}:{POSTGRES_DB_PASSWORD}@kashin.db.elephantsql.com/cpvcyipo'

    # ===== AUTH0 CONFIG =====
    # SERVER_NAME = '2452-192-12-181-28.ngrok-free.app'
    # PREFERRED_URL_SCHEME = 'https'

    # Debug mode (set to True for development, False for production)
    DEBUG = True
