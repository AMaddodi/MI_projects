from flask import Flask
from flask_sqlalchemy import SQLAlchemy


"""
Create DataBase
"""
db = SQLAlchemy()
DB_NAME = 'mi.database'

"""
Create Flask Application
"""
def creat_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dsfsfiukmndkjfiufoiwuf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .session import session
    # register the blueprint
    app.register_blueprint(session, url_prefix='/')

    from .models import SessionTable

    """
    Create the Table in database if not
    """
    with app.app_context():
        db.create_all()

    return app
