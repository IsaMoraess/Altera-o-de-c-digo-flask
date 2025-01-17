import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' 
    + os.path.join(os.path.dirname(__file__), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sua_chave_secreta_aqui')
