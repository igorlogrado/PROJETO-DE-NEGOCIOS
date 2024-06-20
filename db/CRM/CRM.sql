   -- Tabela de Clientes
CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    Telefone VARCHAR(20),
    DataCadastro DATE
);

-- Tabela de Contatos
CREATE TABLE Contatos (
    ContatoID INT PRIMARY KEY AUTO_INCREMENT,
    ClienteID INT,
    Nome VARCHAR(100) NOT NULL,
    Cargo VARCHAR(50),
    Email VARCHAR(100),
    Telefone VARCHAR(20),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID) ON DELETE CASCADE
);

-- Tabela de Atividades
CREATE TABLE Atividades (
    AtividadeID INT PRIMARY KEY AUTO_INCREMENT,
    ClienteID INT,
    DataHora TIMESTAMP,
    TipoAtividade VARCHAR(50),
    Descricao TEXT,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID) ON DELETE CASCADE
);

-- Tabela de Produtos (se necessário para vendas ou relacionamento com produtos)
CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Preco DECIMAL(10, 2),
    Descricao TEXT
);

-- Tabela de Vendas (se necessário para rastrear vendas e transações)
CREATE TABLE Vendas (
    VendaID INT PRIMARY KEY AUTO_INCREMENT,
    ClienteID INT,
    ProdutoID INT,
    DataVenda DATE,
    Quantidade INT,
    ValorTotal DECIMAL(10, 2),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID) ON DELETE CASCADE,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID) ON DELETE CASCADE
);

-- Exemplo de como adicionar um cliente
INSERT INTO Clientes (Nome, Email, Telefone, DataCadastro)
VALUES ('Cliente Teste', 'cliente@teste.com', '(00) 1234-5678', CURDATE());

