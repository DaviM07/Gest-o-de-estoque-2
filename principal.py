import sqlite3
import random


# CONEXÃO COM O BANCO


conexao = sqlite3.connect("padaria.db")
cursor = conexao.cursor()


# CRIA TABELA

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT NOT NULL,
    produto TEXT NOT NULL,
    quantidade INTEGER DEFAULT 0,
    preco REAL DEFAULT 0.00,
    marca TEXT
)
""")


# DADOS DO ESTOQUE
# produto : (quantidade, preco, marca)


