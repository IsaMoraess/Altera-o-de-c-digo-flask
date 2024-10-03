from flask import Flask 
from flask_appbuilder import AppBuilder, SQLA
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

from models import *

@app.route('/')
def home():
    return "Bem-vindo ao seu aplicativo Flask!"

if __name__ == "__main__":
    app.run(debug=True)
