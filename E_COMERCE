import mysql.connector

# Definindo a classe Produto para representar os dados de um produto
class Produto:
    
    # Método de inicialização (construtor) para definir nome e descrição do produto
    def __init__(self, nome, descricao):
        self.nome = nome 
        self.descricao = descricao

# Definindo a classe Cliente para interagir com o banco de dados
class Cliente:
    
    # Método de inicialização (construtor) para estabelecer conexão com o banco de dados
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",      # Endereço do servidor MySQL
            user="root",           # Usuário do banco de dados
            password="he182555@",  # Senha do banco de dados
            database="e_comerce"   # Nome do banco de dados
        )
        self.cursor = self.conexao.cursor()  # Criando um cursor para executar comandos SQL
    
    # Método para inserir um produto na tabela 'produto' do banco de dados
    def inserir_produto(self, produto):
        sql = "INSERT INTO produto (nome, descricao) VALUES (%s, %s)"
        valores = (produto.nome, produto.descricao) 
        self.cursor.execute(sql, valores)  # Executando o comando SQL com os valores do produto
        self.conexao.commit()  # Confirmar a transação no banco de dados
        print('Produto adicionado com sucesso.')  # Mensagem de sucesso
    
    # Método para listar todos os produtos da tabela 'produto' do banco de dados
    def listar_produtos(self):
        self.cursor.execute("SELECT nome, descricao FROM produto")
        produtos = self.cursor.fetchall()  # Obtendo todos os produtos da consulta
        if produtos:
            print("Lista de produtos:")
            for produto in produtos:
                print(f"Nome: {produto[0]}, Descrição: {produto[1]}")  # Imprimindo nome e descrição do produto
        else:
            print("Não há produtos cadastrados.")
    
    # Método para fechar a conexão com o banco de dados
    def fechar_conexao(self):
        self.cursor.close()   # Fechando o cursor
        self.conexao.close()  # Fechando a conexão com o banco de dados

# Criando uma instância da classe Cliente para interagir com o banco de dados
sistema = Cliente()

# Solicitando ao usuário para inserir dados do produto
nome_produto = input("Digite o nome do produto: ")
descricao_produto = input("Digite a descrição do produto: ")

# Criando uma instância da classe Produto com os dados fornecidos pelo usuário
produto = Produto(nome_produto, descricao_produto)

# Inserindo o produto no banco de dados
sistema.inserir_produto(produto)

# Listando os produtos do banco de dados
sistema.listar_produtos()

# Fechando a conexão com o banco de dados
sistema.fechar_conexao()
