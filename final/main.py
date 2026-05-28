import sqlite3

# CONEXÃO
conexao = sqlite3.connect("padaria.db")
cursor = conexao.cursor()

# TABELA
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT UNIQUE,
    quantidade INTEGER,
    preco REAL,
    marca TEXT
)
""")

# LISTA (produto: quantidade, preço, marca)
produtos = {
    "pão francês": (300, 0.80, "Produção Própria"),
    "pão doce": (200, 1.50, "Produção Própria"),
    "pão sírio": (100, 6.90, "Produção Própria"),
    "brioche": (250, 4.50, "Produção Própria"),
    "baguete": (60, 7.00, "Produção Própria"),
    "pão de queijo": (2000, 0.50, "Forno de Minas"),
    "rosca": (18, 12.00, "Caseira"),
    "sonho": (25, 6.50, "Doce Sabor"),
    "enrolado de sarsicha": (35, 5.00, "Produção Própria"),
    "misto quente": (20, 8.50, "Produção Própria"),

    "copo de café": (100, 3.00, "3 Corações"),
    "refri em lata": (120, 6.00, "Coca-Cola"),
    "agua": (100, 3.00, "Crystal"),

    "presunto": (20, 39.90, "Sadia"),
    "queijo muçarela": (25, 54.90, "Tirolez"),

    "chocolate batom": (80, 2.50, "Garoto"),
    "doritos": (60, 10.00, "Elma Chips"),

    "picolé de uva": (50, 4.00, "Kibon"),
    "sorvete de chocolate": (20, 18.00, "Nestlé")
}

# INSERIR 
for produto, dados in produtos.items():
    quantidade, preco, marca = dados

    cursor.execute("""
    INSERT OR IGNORE INTO produtos (produto, quantidade, preco, marca)
    VALUES (?, ?, ?, ?)
    """, (produto, quantidade, preco, marca))

conexao.commit()



# DEF ADICIONAR

def adicionar_estoque():
    produto = input("Produto: ").lower()
    quantidade = int(input("Quantidade para adicionar: "))

    cursor.execute("SELECT quantidade FROM produtos WHERE produto = ?", (produto,))
    resultado = cursor.fetchone()

    if resultado is None:
        preco = float(input("Preço: "))
        marca = input("Marca: ")

        cursor.execute("""
        INSERT INTO produtos (produto, quantidade, preco, marca)
        VALUES (?, ?, ?, ?)
        """, (produto, quantidade, preco, marca))

    else:
        cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade + ?
        WHERE produto = ?
        """, (quantidade, produto))

    conexao.commit()
    print("✅ Estoque atualizado!")


# DEF RETIRAR

def retirar_estoque():
    produto = input("Produto: ").lower()
    quantidade = int(input("Quantidade para retirar: "))

    cursor.execute("SELECT quantidade FROM produtos WHERE produto = ?", (produto,))
    resultado = cursor.fetchone()

    if resultado is None:
        print(" Produto não encontrado!")
        return

    if resultado[0] < quantidade:
        print(" Estoque insuficiente!")
        return

    cursor.execute("""
    UPDATE produtos
    SET quantidade = quantidade - ?
    WHERE produto = ?
    """, (quantidade, produto))

    conexao.commit()
    print(" Retirada feita!")


# MENU
while True:
    print("\n1 - Ver estoque")
    print("2 - Adicionar")
    print("3 - Retirar")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cursor.execute("SELECT produto, quantidade, preco, marca FROM produtos")
        for item in cursor.fetchall():
            print(item)

    elif opcao == "2":
        adicionar_estoque()

    elif opcao == "3":
        retirar_estoque()

    elif opcao == "0":
        break

conexao.close()