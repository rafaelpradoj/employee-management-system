import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = os.getenv("DB_CONFIG")

if not DB_CONFIG:
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASS", "")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    dbname = os.getenv("DB_NAME", "empresa")

    DB_CONFIG = f"postgres://{user}:{password}@{host}:{port}/{dbname}"

def criar_tabela_inicial():
    with psycopg.connect(DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS funcionarios(
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                departamento VARCHAR(50) NOT NULL)
            """)
            conn.commit()
def cadastrar_funcionario(nome, departamento):
    with psycopg.connect(DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO funcionarios (nome, departamento) VALUES (%s, %s)",
                (nome, departamento))
            conn.commit()
def listar_funcionario(id_funcionario):
    with psycopg.connect(DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM funcionarios WHERE id = %s",
                (id_funcionario,))
            resultado_busca = cur.fetchone()
            return resultado_busca
def atualizar_nome_funcionario(id, novo_nome):
    with psycopg.connect(DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE funcionarios SET nome = %s WHERE id = %s",
                (novo_nome, id))
            conn.commit()
def atualizar_departamento_funcionario(id, novo_departamento):
    with psycopg.connect(DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE funcionarios SET departamento = %s WHERE id = %s",
                (novo_departamento, id))
            conn.commit()
def deletar_funcionario(id):
    with psycopg.connect(DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM funcionarios WHERE id = %s",
                (id,))
            conn.commit()