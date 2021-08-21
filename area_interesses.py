#importa todos os metodos e variáveis do arquivo 'config'
from config import *

# classe do projeto integrador onde adiciona os usuários do sistema ao bando de dados
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome_completo = db.Column (db.String(255))
    usuario = db.Column (db.String(255))
    senha = db.Column (db.String(255))
    email = db.Column (db.String(255))
    telefone = db.Column (db.String(20))
    
    # método json() retornando informações da classe Pessoa no formato json
    def json(self):
        return{
            "id": self.id,
            "nome_completo": self.nome_completo,
            "usuario": self.usuario,
            "senha": self.senha,
            "email": self.email,
            "telefone" : self.telefone
        }

# classe feita para a av3 onde ira ser adicionada no projeto integrador, 
# recebendo os dados da area de interesse do usuario
class AreaInteresse(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    vestibular = db.Column (db.String(255))
    data = db.Column (db.String(255))
    foco_materias = db.Column (db.String(255))

    # método json() retornando informações da classe Pessoa no formato json
    def json(self):
        return{
            "id": self.id,
            "vestibular": self.vestibular,
            "data": self.data,
            "materias_de_foco": self.foco_materias
        }

# apenas se o arquivo for chamado diretamente irá executar o código abaixo
if __name__ == "__main__":
    
    # se o arquivo de banco de dados existir, exclui 
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # cria o banco de dados 'aprovei.db' 
    db.create_all()
    
    #insere os dados do usuário na tabela 
    nova_pessoa = Pessoa(nome_completo = "Enolla Bressanim", usuario = "nolla",
        senha = "1234", email = "enolla@gmail.com", telefone = "(47) 9 1234-5678")
    # estabelece os dados com o banco de dados
    db.session.add(nova_pessoa)

    #insere os dados do usuário na tabela 
    novo_interesse = AreaInteresse(vestibular= "Enem", data = "21/11", foco_materias = "portugues e matematica")
    # estabelece os dados com o banco de dados
    db.session.add(novo_interesse)

    # salva os dados no banco de dados
    db.session.commit()

    #carrega os dados da tabela pessoas
    pessoas = db.session.query(Pessoa).all()
    #se haver informações na tabela, lista todos os dados
    for pessoa in pessoas:
        print(pessoa)
        print(pessoa.json())

    #carrega os dados da tabela interesses
    interesses = db.session.query(AreaInteresse).all()
    #se haver informações na tabela, lista todos os dados
    for interesse in interesses:
        print(interesse)
        print(interesse.json())