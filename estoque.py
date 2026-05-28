import sqlite3
import random


# CONEXÃO COM O BANCO


conexao = sqlite3.connect("padaria.db")
cursor = conexao.cursor()


# CRIAR TABELA


cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT NOT NULL,
    produto TEXT NOT NULL,
    quantidade INTEGER,
    preco REAL,
    marca TEXT
)
""")

# DADOS DA PADARIA


estoque = {

    "Padaria e Lanches": {

        "pão francês": (300, 0.80, "Produção Própria"),
        "pão doce": (200, 1.50, "Produção Própria"),
        "pão sírio": (100, 6.90, "Produção Própria"),
        "brioche": (250, 4.50, "Produção Própria"),
        "baguete": (60, 7.00, "Produção Própria"),
        "pão de queijo": (2000, 0.50, "Forno de Minas"),
        "rosca": (18, 12.00, "Caseira"),
        "sonho": (25, 6.50, "Doce Sabor"),
        "enrolado de salsicha": (35, 5.00, "Produção Própria"),
        "misto quente": (20, 8.50, "Produção Própria"),
        "pão com ovo": (25, 7.00, "Produção Própria"),
        "pão pizza": (15, 9.50, "Produção Própria"),
        "sanduiche natural": (18, 10.00, "Produção Própria"),
        "bauru": (12, 11.00, "Produção Própria"),
        "coxinha grande": (40, 8.00, "Produção Própria"),
        "mini coxinha": (250, 2.00, "Produção Própria"),
        "bolinha de queijo": (100, 2.50, "Produção Própria"),
        "kibe": (40, 6.00, "Produção Própria"),
        "mini kibe": (70, 2.00, "Produção Própria"),
        "empada": (60, 7.50, "Produção Própria")
    },

   
}


# INSERIR DADOS


for categoria, produtos in estoque.items():

    for produto, dados in produtos.items():

        quantidade, preco, marca = dados

        cursor.execute("""
        INSERT INTO produtos
        (categoria, produto, quantidade, preco, marca)
        VALUES (?, ?, ?, ?, ?)
        """, (categoria, produto, quantidade, preco, marca))

# SALVAR DADOS


conexao.commit()


# MOSTRAR PRODUTOS


cursor.execute("SELECT * FROM produtos")

for item in cursor.fetchall():
    print(item)

# FECHAR CONEXÃO


conexao.close()