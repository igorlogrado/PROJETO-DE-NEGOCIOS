import mysql.connector

# Conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="seu_host",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

# Criação das tabelas
def criar_tabelas():
    try:
        cursor = conexao.cursor()

        # Tabela de Clientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes (
                ClienteID INT PRIMARY KEY AUTO_INCREMENT,
                Nome VARCHAR(100) NOT NULL,
                Email VARCHAR(100),
                Telefone VARCHAR(20),
                DataCadastro DATE
            )
        """)

        # Tabela de Contatos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Contatos (
                ContatoID INT PRIMARY KEY AUTO_INCREMENT,
                ClienteID INT,
                Nome VARCHAR(100) NOT NULL,
                Cargo VARCHAR(50),
                Email VARCHAR(100),
                Telefone VARCHAR(20),
                FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID) ON DELETE CASCADE
            )
        """)

        # Tabela de Atividades
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Atividades (
                AtividadeID INT PRIMARY KEY AUTO_INCREMENT,
                ClienteID INT,
                DataHora TIMESTAMP,
                TipoAtividade VARCHAR(50),
                Descricao TEXT,
                FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID) ON DELETE CASCADE
            )
        """)

        # Tabela de Produtos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Produtos (
                ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
                Nome VARCHAR(100) NOT NULL,
                Preco DECIMAL(10, 2),
                Descricao TEXT
            )
        """)

        conexao.commit()
        print("Tabelas criadas com sucesso.")

    except mysql.connector.Error as err:
        print(f"Erro ao criar tabelas: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()

# Executando a função para criar as tabelas
criar_tabelas()

# Fechando a conexão com o banco de dados
conexao.close()
