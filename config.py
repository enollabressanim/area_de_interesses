#importa todas as bibliotecas utilizadas
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

from flask_cors import CORS
import os

# define o nome do aplicativo
app = Flask(__name__)
CORS(app)
# caminho raiz do aplicavo
caminho =  os.path.dirname(os.path.abspath(__file__))
# define o caminho completo e o nome do arquivo do banco de dados
arquivobd = os.path.join(caminho, "aprovei.db")
# define configurações do bando e dados no aplicativo
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICTIONS'] = False
#inicia o banco de dados
db = SQLAlchemy(app)
