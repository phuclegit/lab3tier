import psycopg2
import os


def check_database():

    try:

        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            port=os.getenv("DB_PORT", 5432)
        )

        conn.close()

        return "UP"

    except Exception:

        return "DOWN"
