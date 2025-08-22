import mysql.connector
from dotenv import load_dotenv
import os
def banco(nomedojogador, tempocorrido, ponto):
    try:
        load_dotenv()
        user = os.getenv("DB_USER")
        senha = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        db = os.getenv("DB_NAME")
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=senha,
            database=db
        )
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nome, tempo, pontuacao) VALUES (%s, %s, %s)"
        valores = (nomedojogador, tempocorrido, ponto)
        cursor.execute(sql, valores)
        conn.commit()
        print(cursor.rowcount, "registro inserido no banco de dados!")
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
    finally:
        # sempre fecha conexão e cursor
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


