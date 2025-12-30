
import sqlite3

DB_NAME = "pecas.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def criar_tabela():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pecas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            material TEXT,
            peso REAL,
            tempo REAL,
            custo_total REAL,
            preco_venda REAL,
            lucro REAL,
            markup REAL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
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
        cursor.execute("SELECT * FROM pecas ORDER BY data_criacao DESC")
        return cursor.fetchall()

import sqlite3

DB_NAME = "pecas.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def criar_tabela():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pecas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            material TEXT,
            peso REAL,
            tempo REAL,
            custo_total REAL,
            preco_venda REAL,
            lucro REAL,
            markup REAL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
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
        cursor.execute("SELECT * FROM pecas ORDER BY data_criacao DESC")
        return cursor.fetchall()

