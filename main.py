import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL,
    marca TEXT NOT NULL
)
""")
cursor.execute("""INSERT INTO produtos
               (produto, quantidade, preco, marca) VALUES
              ()
               """)

conexao.commit()