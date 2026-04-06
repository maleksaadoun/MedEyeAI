from flask import Flask
from mongoengine import connect
from config import Config
from routes.images import images_bp
from routes.auth import auth_bp
from routes.client import client_bp
from routes.admin import admin_bp
from flask_cors import CORS
import os
from extensions import mail 

#pip install mongoengine
#pip install flask-bcrypt
#pip install flask-cors
#pip install -r requirements.txt
#pip freeze > requirements.txt
#pip install Flask-Mail
#python -m venv venv
#pip install -r requirements.txt
#To Run This Code => flask run --host=0.0.0.0 --port=5000

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"], supports_credentials=True)
    app.config.from_object(config_class)
    # Gmail SMTP configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'medeyeai@gmail.com'
    app.config['MAIL_PASSWORD'] = 'spblfmaklafjbdgb'  # use app password
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail.init_app(app)  # initialize mail with the Flask app

    # Connect to MongoDB using MongoEngine
    connect(
        db=app.config['MONGODB_SETTINGS']['db'],
        host=app.config['MONGODB_SETTINGS']['host'],
        port=app.config['MONGODB_SETTINGS']['port']
    )

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(images_bp, url_prefix='/api')
    app.register_blueprint(client_bp, url_prefix='/api')
    app.register_blueprint(admin_bp, url_prefix='/api')

    return app

# Create an application instance that can be used by Flask CLI
# This allows commands like "flask db migrate" to work
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
