import psycopg2

def bd(clientes):

    conn = psycopg2.connect(
        dbname="nome_do_banco_de_dados",
        user="nome_de_usuario",
        password="senha_do_usuario",
        host="endereço_do_servidor",
        port="porta_do_servidor"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
