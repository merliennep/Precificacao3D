import psycopg2
import os

def conectar():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=os.environ["DB_PORT"]
    )

def criar_tabela():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pecas (
            id SERIAL PRIMARY KEY,
            nome TEXT,
            material TEXT,
            peso REAL,
            tempo REAL,
            custo_total REAL,
            preco_venda REAL,
            lucro REAL,
            markup REAL,
            data_criacao TIMESTAMP DEFAULT NOW()
        )
        """)
        conn.commit()

def salvar_peca(dados, resultado):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO pecas (
            nome, material, peso, tempo,
            custo_total, preco_venda, lucro, markup
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            dados["nome"],
            "PETG" if dados["petg"] else "PLA",
            dados["peso_g"],
            dados["tempo_h"],
            resultado["custo_total"],
            resultado["preco_venda"],
            resultado["lucro"],
            dados["markup"]
        ))
        conn.commit()

def listar_pecas():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id, nome, material, peso, tempo,
               custo_total, preco_venda, lucro, markup, data_criacao
        FROM pecas
        ORDER BY data_criacao DESC
        """)
        return cursor.fetchall()
