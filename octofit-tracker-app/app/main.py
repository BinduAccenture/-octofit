from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .routes import init_routes
        init_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)