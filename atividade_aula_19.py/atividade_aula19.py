import sqlite3

# Conectar ao banco de dados (cria se não existir)
conexao = sqlite3.connect("agencia_marketing.db")
cursor = conexao.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT,
    endereco TEXT,
    trabalho TEXT,
    graduacao TEXT
)
""")

# Função para inserir lead
def inserir_lead(nome, idade, email, endereco, trabalho, graduacao):
    cursor.execute("""
    INSERT INTO leads (nome, idade, email, endereco, trabalho, graduacao)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, idade, email, endereco, trabalho, graduacao))
    
    conexao.commit()
    print("Lead cadastrado com sucesso!")

# Função para listar leads
def listar_leads():
    cursor.execute("SELECT * FROM leads")
    leads = cursor.fetchall()

    print("\n===== LISTA DE LEADS =====")
    for lead in leads:
        print(f"ID: {lead[0]}")
        print(f"Nome: {lead[1]}")
        print(f"Idade: {lead[2]}")
        print(f"Email: {lead[3]}")
        print(f"Endereço: {lead[4]}")
        print(f"Trabalho: {lead[5]}")
        print(f"Graduação: {lead[6]}")
        print("-------------------------")

# Exemplo de uso
inserir_lead(
    "matheus gonzales",
    15,
    "matheusgaleite@gmail.com",
    "Rua consul orestes correa, 77",
    "nenhum",
    "nenhum"
)

listar_leads()

# Fechar conexão
conexao.close()
