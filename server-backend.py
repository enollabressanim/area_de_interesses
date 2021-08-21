# importa todos os metodos e variáveis do arquivo 'config'
from config import *
# importa todos as classes do arquivo 'area_interesses'
from area_interesses import *

# define a rota padrão do acesso web
@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/listar_pessoas">Operação listar</a>'+\
            '<br>Sistema de cadastro de area de interesses. '+\
        '<a href="/listar_interesses">Operação listar</a>'

# define a rota de acesso web para listagem de pessoas
@app.route("/listar_pessoas")
def listar_pessoas():
    # obter as pessoas do cadastro
    pessoas = db.session.query(Pessoa).all()
    # aplicar o método json que a classe Pessoa possui a cada elemento da lista
    pessoas_em_json = [ x.json() for x in pessoas ]
    # fornecer a lista de pessoas em formato json
    return jsonify(pessoas_em_json)

# define a rota de acesso web para listagem de interesses
@app.route("/listar_interesses")
def listar_interesses():
    # obter os interesses do cadastro
    interesses = db.session.query(AreaInteresse).all()
    # aplicar o método json que a classe AreaInteresses possui a cada elemento da lista
    interesses_em_json = [ x.json() for x in interesses ]
    # fornecer a lista de interesses em formato json
    return jsonify(interesses_em_json)

# roda o aplicativo com debug ativado
app.run(debug=True)