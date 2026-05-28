# Sistema de Estoque e Controle Financeiro para Padaria

## Desenvolvedores

* Pedro Henrique
* Davi
* Gustavo

---

## Descrição do Projeto

Este projeto consiste em um sistema de gerenciamento de estoque e controle financeiro para uma padaria, desenvolvido em Python utilizando SQLite como banco de dados.

O sistema foi criado com o objetivo de automatizar o cadastro de produtos, organizar o estoque da padaria e realizar operações financeiras básicas, permitindo maior controle administrativo e operacional.

---

## Tecnologias Utilizadas

* Python 3
* SQLite3
* Math
* Random

---

## Funcionalidades

### Controle de Estoque

* Criação automática do banco de dados
* Criação automática da tabela de produtos
* Cadastro automatizado de produtos
* Organização de produtos por categorias
* Controle de quantidade e preço
* Consulta de produtos cadastrados

### Controle Financeiro

* Registro de entradas financeiras
* Registro de saídas financeiras
* Cálculo de lucro
* Cálculo de prejuízo
* Menu interativo no terminal

---

## Estrutura do Projeto

```bash
sistema-padaria/
│
├── main.py
├── README.md
├── padaria.db
├── requirements.txt
└── .gitignore
```

---

## Estrutura da Tabela

A tabela `produtos` possui a seguinte estrutura:

| Campo      | Tipo    | Descrição                |
| ---------- | ------- | ------------------------ |
| id         | INTEGER | Identificador do produto |
| categoria  | TEXT    | Categoria do produto     |
| produto    | TEXT    | Nome do produto          |
| quantidade | INTEGER | Quantidade disponível    |
| preco      | REAL    | Preço do produto         |
| marca      | TEXT    | Marca do produto         |

---

## Funcionamento do Sistema

### Conexão com o Banco de Dados

```python
conexao = sqlite3.connect("padaria.db")
cursor = conexao.cursor()
```

---

### Criação da Tabela

```python
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
```

---

### Inserção dos Produtos

```python
cursor.execute("""
INSERT INTO produtos
(categoria, produto, quantidade, preco, marca)
VALUES (?, ?, ?, ?, ?)
""", (categoria, produto, quantidade, preco, marca))
```

---

## Calculadora Financeira

O sistema possui uma calculadora financeira integrada ao terminal.

### Menu Principal

```python
print("CALCULADORA FINANCEIRA DA PADARIA")

print("1. Entrada")
print("2. Saída")
print("3. Lucro")
print("4. Prejuízo")
print("0. Sair")
```

---

### Cálculo de Lucro

```python
lucro = vendas - gastos
```

---

### Cálculo de Prejuízo

```python
prejuizo = gastos - vendas
```

---

## Categorias do Sistema

### Padaria e Lanches

* pão francês
* brioche
* baguete
* pão de queijo
* coxinha
* empada
* sanduíches

### Bebidas

* refrigerantes
* energéticos
* sucos
* café
* água

### Frios e Laticínios

* presunto
* queijo
* requeijão
* manteiga

### Gelados

* picolés
* sorvetes
* açaí

---

## Como Executar o Projeto

### Clonar o Repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

### Acessar a Pasta do Projeto

```bash
cd sistema-padaria
```

---

### Executar o Sistema

```bash
python main.py
```

---

## Comandos Git Utilizados

### Inicializar Repositório

```bash
git init
```

### Adicionar Arquivos

```bash
git add .
```

### Criar Commit

```bash
git commit -m "Primeiro commit do projeto"
```

### Conectar ao GitHub

```bash
git remote add origin URL_DO_REPOSITORIO
```

### Enviar Projeto

```bash
git push -u origin main
```

---

## Objetivo Acadêmico

O projeto foi desenvolvido com finalidade educacional para aplicação prática dos seguintes conceitos:

* Banco de dados com SQLite
* Manipulação de dados em Python
* Estruturas de repetição
* Persistência de dados
* Organização de sistemas
* Controle financeiro básico

---

## Melhorias Futuras

* Interface gráfica
* Sistema de vendas integrado
* Relatórios financeiros
* Dashboard administrativo
* Controle de usuários
* Integração com sistemas web

---

## Considerações Finais

Este projeto demonstra a integração entre Python e SQLite na construção de um sistema simples de gerenciamento de estoque e controle financeiro para uma padaria.

A aplicação apresenta uma estrutura organizada e pode servir como base para futuras melhorias e expansões.

---
