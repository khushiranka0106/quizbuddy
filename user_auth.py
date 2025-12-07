from database import get_connection

def signup(username, password):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    data = cur.fetchone()

    conn.close()
    return data is not None
