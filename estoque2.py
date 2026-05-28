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
 
dados = { "Bebidas": {

        "copo de café": (100, 3.00, "3 Corações"),
        "achocolatado": (30, 5.00, "Toddynho"),
        "refrigerante em lata": (120, 6.00, "Coca-Cola"),
        "refrigerante 2L": (50, 12.00, "Coca-Cola"),
        "energético": (40, 12.00, "Red Bull"),
        "isotônico": (35, 8.00, "Gatorade"),
        "água tônica": (30, 5.50, "Schweppes"),
        "água": (100, 3.00, "Crystal"),
        "água com gás": (60, 4.00, "Crystal"),
        "suco de laranja": (25, 7.00, "Del Valle"),
        "suco de uva": (25, 7.00, "Del Valle"),
        "suco de maçã": (20, 7.00, "Del Valle"),
        "suco de maracujá": (20, 7.00, "Del Valle"),
        "suco de manga": (20, 7.00, "Del Valle"),
        "suco de abacaxi": (20, 7.00, "Del Valle"),
        "leite desnatado": (25, 6.00, "Italac"),
        "leite integral": (40, 6.00, "Piracanjuba"),
        "leite de saco": (15, 5.00, "LeitBom"),
        "cerveja em lata": (100, 5.50, "Heineken"),
        "cerveja em garrafa": (60, 12.00, "Brahma")

    },

    "Frios e Laticínios": {

        "presunto": (20, 39.90, "Sadia"),
        "peito de peru": (15, 49.90, "Perdigão"),
        "queijo muçarela": (25, 54.90, "Tirolez"),
        "queijo prato": (20, 52.90, "Polenghi"),
        "queijo cheddar": (15, 59.90, "Polenghi"),
        "mortadela": (20, 29.90, "Perdigão"),
        "requeijão": (30, 9.00, "Catupiry"),
        "manteiga": (25, 11.00, "Aviação"),
        "margarina": (40, 8.00, "Qualy")

    },

    "Gelados": {

        "picolé de uva preta": (50, 4.00, "Kibon"),
        "picolé de uva verde": (50, 4.00, "Kibon"),
        "picolé de limão": (50, 4.00, "Kibon"),
        "picolé de manga": (40, 4.50, "Kibon"),
        "picolé de coco": (40, 4.50, "Kibon"),
        "picolé de morango": (50, 4.00, "Kibon"),
        "picolé de acerola": (30, 5.00, "Rochinha"),
        "picolé de goiaba": (30, 5.00, "Rochinha"),
        "picolé de kiwi": (25, 5.50, "Rochinha"),
        "picolé de cupuaçu": (20, 6.00, "Rochinha"),
        "picolé de açaí": (35, 6.00, "Rochinha"),
        "picolé de fini": (40, 7.00, "Fini"),
        "picolé de banana descascável": (30, 5.00, "Kibon"),
        "pote de açaí 300 ml": (40, 14.00, "Oakberry"),
        "sorvete de cone": (50, 3.50, "Kibon"),
        "sorvete de brigadeiro": (20, 18.00, "Nestlé"),
        "sorvete de chocolate": (20, 18.00, "Nestlé"),
        "sorvete napolitano": (20, 18.00, "Nestlé"),
        "sorvete de flocos": (20, 18.00, "Nestlé"),
        "sorvete de morango": (20, 18.00, "Nestlé"),
        "sorvete de creme": (20, 18.00, "Nestlé"),
        "sorvete de M&M": (15, 24.00, "M&M"),
        "sorvete de pistache": (10, 29.00, "Bacio di Latte"),
        "sorvete Magnum": (30, 12.00, "Kibon"),
        "sorvete Tablito": (35, 8.00, "Kibon"),
        "sorvete Eskibon": (35, 9.00, "Kibon"),
        "caixinha de Eskibon": (20, 22.00, "Kibon")

    }

}

