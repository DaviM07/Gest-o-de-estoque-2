import sqlite3

# =========================
# CONEXÃO
# =========================
def conectar():
    conexao = sqlite3.connect("padaria.db")
    cursor = conexao.cursor()
    return conexao, cursor



# CRIAR TABELA

def criar_tabela(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT NOT NULL,
        produto TEXT NOT NULL UNIQUE,
        quantidade INTEGER,
        preco REAL,
        marca TEXT
    )
    """)


# INSERIR DADOS INICIAIS 
def inserir_dados_iniciais(cursor, conexao):
    cursor.execute("SELECT COUNT(*) FROM produtos")

    if cursor.fetchone()[0] > 0:
        return  # Já tem dados, não insere novamente

    estoque = {
       
    }

    for categoria, produtos in estoque.items():
        for produto, dados in produtos.items():
            quantidade, preco, marca = dados

            cursor.execute("""
            INSERT INTO produtos
            (categoria, produto, quantidade, preco, marca)
            VALUES (?, ?, ?, ?, ?)
            """, (categoria, produto, quantidade, preco, marca))

    conexao.commit()



# MOSTRAR PRODUTOS

def mostrar_estoque(cursor):
    cursor.execute("SELECT produto, quantidade, preco FROM produtos")

    print("\n=== ESTOQUE ===")
    for produto, qtd, preco in cursor.fetchall():
        print(f"{produto} | Qtd: {qtd} | R$ {preco}")



# RETIRAR PRODUTO

def retirar_estoque(cursor, conexao):
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
    print(" Estoque atualizado!")



# MENU

def menu():
    conexao, cursor = conectar()

    criar_tabela(cursor)
    inserir_dados_iniciais(cursor, conexao)

    while True:
        print("\n===== PADARIA =====")
        print("1 - Ver estoque")
        print("2 - Retirar produto")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            mostrar_estoque(cursor)

        elif opcao == "2":
            retirar_estoque(cursor, conexao)

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")

    conexao.close()



# EXECUTAR

menu()