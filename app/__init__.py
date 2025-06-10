from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    @app.route("/")
    def home():
        return "Hello from factory-based app!"

    return app