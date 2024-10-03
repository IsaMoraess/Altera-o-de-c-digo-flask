from flask_appbuilder import SQLA, Model
from sqlalchemy import Column, Integer, String

db = SQLA()

class Aluno(Model):
    __tablename__ = 'aluno'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)

class Escola(Model):
    __tablename__ = 'escola'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)



