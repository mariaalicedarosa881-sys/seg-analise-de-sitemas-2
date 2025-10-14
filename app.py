from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

# Setup inicial do Flask e conexão com o banco de dados
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///centraltech_produtos.db' 

db = SQLAlchemy(app) 

# Modelo da Tabela PRODUTO no banco de dados
class PRODUTO(db.Model):
    id_produto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), unique=True, nullable=False) # Nome do produto é único e obrigatório
    descricao = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Float, nullable=False) # Preço de venda
    quantidade_estoque = db.Column(db.Integer, nullable=False) # Quantidade em estoque
    data_cadastro = db.Column(db.DateTime(), default=datetime.datetime.now)

    def __repr__(self):
        return f'<Produto {self.nome} | Estoque: {self.quantidade_estoque}>'

#CRUD READ = LER
@app.route('/')
def index():
    # Puxamos todos os produtos do banco de dados
    produtos = PRODUTO.query.all()
    return render_template('index.html', produtos=produtos)

# 2. CREATE (Criar) - (INSERIR)
@app.route('/create_produto', methods=['POST'])
def create_produto():
    try:
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = float(request.form['preco'])
        quantidade_estoque = int(request.form['quantidade_estoque'])

        # Checamos se o produto já existe pelo nome (que é único)
        existe_produto = PRODUTO.query.filter_by(nome=nome).first()

        if existe_produto:
            # Mensagem de erro mais direta
            return f'Opa! Já existe um produto chamado "{nome}" cadastrado. O nome precisa ser único.', 400

        # o objeto do novo produto
        novo_produto = PRODUTO(nome=nome, descricao=descricao, preco=preco, quantidade_estoque=quantidade_estoque)

        # Adicionamos e salvamos no banco
        db.session.add(novo_produto)
        db.session.commit()

        # Voltamos para a tela principal
        return redirect('/')
    except ValueError:
        # Erro se o preço ou a quantidade não forem números
        return 'Atenção: O Preço e a Quantidade devem ser números válidos!', 400
    except Exception as e:
        print(f"Erro ao criar produto: {e}")
        # Mensagem de erro mais amigável
        return 'Deu ruim no servidor ao tentar salvar o produto. Tente de novo!', 500


# 3. DELETE (Apagar) - Rota para remover um produto pelo ID
@app.route('/delete_produto/<int:id_produto>', methods=['POST'])
def delete_produto(id_produto):
    # Encontra o produto ou dá erro 404
    produto = PRODUTO.query.get_or_404(id_produto)
    
    try:
        # Excluímos e salvamos a mudança
        db.session.delete(produto)
        db.session.commit()
        
        # Volta para a tela principal
        return redirect('/')
    except Exception as e:
        print(f"Erro ao deletar produto: {e}")
        return 'Não foi possível remover o produto. Tente novamente!', 500


# 4. UPDATE (Atualizar) 
@app.route('/update_produto/<int:id_produto>', methods=['POST'])
def update_produto(id_produto):
    # Encontra o produto ou dá erro 404
    produto = PRODUTO.query.get_or_404(id_produto)
    
    try:
        novo_nome = request.form['nome']
        
        # Se o nome mudou, checamos por duplicidade (não queremos conflitos de nome)
        if produto.nome != novo_nome:
            existe_outro = PRODUTO.query.filter(PRODUTO.nome == novo_nome, PRODUTO.id_produto != id_produto).first()
            if existe_outro:
                return f'ERRO: O nome "{novo_nome}" já está sendo usado por outro item.', 400

        # Atualizamos os dados
        produto.nome = novo_nome
        produto.descricao = request.form['descricao']
        produto.preco = float(request.form['preco'])
        produto.quantidade_estoque = int(request.form['quantidade_estoque'])

        # Commit para salvar as alterações
        db.session.commit()
        
        return redirect('/')
    except ValueError:
        return 'Atenção: O Preço e a Quantidade devem ser números válidos!', 400
    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")
        return 'Não foi possível atualizar o produto. Verifique os dados e tente de novo.', 400


if __name__ == '__main__':
    # Bloco que roda quando iniciamos o app.py
    with app.app_context():
        # Cria as tabelas do banco de dados (só se não existirem)
        print("Preparando o banco de dados...")
        db.create_all()
    
    # Inicia a aplicação
    print("Iniciando a CentralTech App na porta 5153...")
    app.run(debug=True, port=5153)
