import mysql.connector #permite conectar e interagir com bancos de dados MySQL em Python de maneira simples e eficiente.

# Definindo a classe Aluno
class Aluno:
    
    # Método de inicialização (construtor)
    def __init__(self, nome, email, identificacao):
        self.nome = nome
        self.email = email
        self.identificacao = identificacao

# Definindo a classe Matricula
class Matricula:
    
    # Método de inicialização (construtor)
    def __init__(self):
        # Estabelecendo conexão com o banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host="localhost",      # Endereço do servidor MySQL
            user="root",           # Usuário do banco de dados
            password="he182555@",  # Senha do banco de dados
            database="escolar"     # Nome do banco de dados
        )
        # Criando um cursor para executar comandos SQL
        self.cursor = self.conexao.cursor()

    # Método para listar matrículas e dados dos alunos
    def listar_matriculas_alunos(self):
        # Consulta SQL para juntar dados das tabelas matricula e aluno
        sql = """
            SELECT m.nome as nome_aluno, m.idade, m.ano, a.nome as nome_aluno, a.email, a.identificacao
            FROM matricula m
            INNER JOIN aluno a ON m.nome = a.nome 
        """
        # Executando a consulta SQL
        self.cursor.execute(sql)
        # Obtendo todos os resultados da consulta
        matriculas = self.cursor.fetchall()
        # Iterando sobre os resultados e imprimindo na tela
        for matricula in matriculas:
            print(f"Nome: {matricula[0]}, Idade: {matricula[1]}, Ano: {matricula[2]}")
            print(f"   Email: {matricula[4]}, Identificação: {matricula[5]}")
            print()  # linha em branco para separar os resultados

    # Método para fechar a conexão com o banco de dados
    def fechar_conexao(self):
        self.cursor.close()    # Fechando o cursor
        self.conexao.close()   # Fechando a conexão com o banco de dados

# Criando uma instância da classe Matricula
matricula = Matricula()

# Listando as matrículas e dados dos alunos
print("Lista de matrículas e dados dos alunos:")
matricula.listar_matriculas_alunos()

# Fechando a conexão com o banco de dados
matricula.fechar_conexao()

