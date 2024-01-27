import os

class Config:
    # ===== POSTGRES DB CONFIG =====
    POSTGRES_DB_USERNAME=os.environ.get('POSTGRES_DB_USERNAME') or None
    POSTGRES_DB_PASSWORD=os.environ.get('POSTGRES_DB_PASSWORD') or None
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_DB_USERNAME}:{POSTGRES_DB_PASSWORD}@kashin.db.elephantsql.com/cpvcyipo'
    
    # ===== JWT and SESSION CONFIG =====
    # JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY') or None
    # SECRET_KEY=os.environ.get('SECRET_KEY') or None

    # Debug mode (set to True for development, False for production)
    DEBUG = True
