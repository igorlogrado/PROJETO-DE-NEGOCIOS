
import mysql.connector # Importar o módulo mysql.connector que fornece conectividade MySQL

class Contato: # Defina uma classe Contato para representar um contato com um nome e um número de contato
    
    def __init__(self, nome, contato): # Inicialize o objeto Contato com um nome e um número de contato
       
        self.nome = nome  # inicializar nome  
        
        self.contato = contato # inicializar contato

class SistemaDeContatos: # Defina uma classe SistemaDeContatos para gerenciar contatos em um banco de dados MySQL
    
    def __init__(self):  # Inicialização de atributos MySQL
       
        self.conexao = mysql.connector.connect( # Estabelecendo uma conexão com o banco de dados MySQL
            host="localhost", # Host do banco de dados

            user="root", # Nome de usuário do banco de dados

            password="he182555@", # Senha do banco de dados

            database="contatos_db" # Nome do banco de dados

        )
    
        self.cursor = self.conexao.cursor() # Cria um objeto cursor para executar consultas SQL

    def adicionar_contato (self, contato): # Defina um método para adicionar um contato ao banco de dados
        
        sql = "INSERT INTO  contatos (nome, contato) VALUES (%s, %s)" # Defina a consulta SQL para inserir um novo contato 
        
        valores = (contato.nome, contato.contato) # Defina os valores a serem inseridos na consulta SQL
       
        self.cursor.execute(sql, valores) #Executa a consulta SQL
        
        self.conexao.commit() # Confirme a transação para salvar as alterações no banco de dados
        
        print ('Contato adicionado com sucesso.')  # Imprima uma mensagem de sucesso
        
    def listar_contatos(self): # Defina um método para listar todos os contatos do banco de dados
       
        self.cursor.execute("SELECT nome, contato FROM contatos")  # Execute uma consulta SQL para selecionar todos os contatos do banco de dados
        #
        contatos = self.cursor.fetchall() # Busca todos os resultados da consulta executada
        
        for contato in contatos:
            print(f"Nome: {contato[0]}, Contato: {contato[1]}") #  Aqui, estamos utilizando uma f-string para formatar e imprimindo-os.

    def fechar_conexao (self): # fechar a coneção e salvar as alterações pre-definidas

        self.cursor.close() # Não se esqueça de fazer commit para salvar as alterações (se necessário)
        
        self.conexao.close() # fechar coneção 

# Instancia do sistema de contatos 
sistema =  SistemaDeContatos()

# Cria contatos
contato1 = Contato('patati', "25136546")
contato2 = Contato('patata', "365151651")

# Adicionar contatos 
sistema.adicionar_contato(contato1)
sistema.adicionar_contato(contato2)

# Adicionar contatos
print("Lista de contatos: ") # imprimir a lista de contatos

sistema.listar_contatos() # chamar alista de contatos para listalos

sistema.fechar_conexao() # Fecha a conexão