from database.connection import get_connection


def check_database():

    try:
        conn = get_connection()
        conn.close()
        return "UP"

    except Exception:
        return "DOWN"