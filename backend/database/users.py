from database.connection import get_connection


def get_users():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, email
        FROM users
        ORDER BY id;
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    users = []

    for row in rows:

        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })

    return users


def count_users():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total