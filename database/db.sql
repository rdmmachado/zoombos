CREATE TABLE if not exists usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    login VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE if not exists Clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    endereco VARCHAR(14) NOT NULL
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
);

CREATE TABLE if not exists  ordens_servico (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL
    servico VARCHAR(255) NOT NULL,
    posto_servico VARCHAR(255) NOT NULL,
    data DATE NOT NULL,
    assinatura VARCHAR(255) NOT NULL,
    observacao VARCHAR(255) NOT NULL,
    responsavel VARCHAR(100) NOT NULL,
    responsavel_type VARCHAR(100) NOT NULL
);
