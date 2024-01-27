from dotenv import load_dotenv
load_dotenv()

from app import app, db

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)