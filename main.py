from flask import Flask, request  # noqa: E402
import sqlite3  # noqa: E402


app = Flask(__name__)


def saudacao(nome: str) -> str:
    """Retorna uma saudação segura."""
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string")
    return f"Olá, {nome}! Bem-vindo ao sistema."


def calcular_media(notas: list) -> float:
    """Calcula a média de uma lista de notas."""
    if not notas:
        raise ValueError("Lista de notas não pode ser vazia")
    return sum(notas) / len(notas)


@app.route('/user')
def buscar_usuario_seguro():
    user_id = request.args.get('id')
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    return str(cursor.fetchone())


if __name__ == "__main__":
    print(saudacao("Aluno FATEC"))
    print(f'Média: {calcular_media([8.5, 9.0, 7.5])}')
