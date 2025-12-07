import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="103023BCON1030",   # <-- CHANGE THIS TO YOUR PASSWORD
        database="quizbuddy"
    )

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # Users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE,
        password VARCHAR(50)
    )
    """)

    # Questions table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions(
        id INT AUTO_INCREMENT PRIMARY KEY,
        category VARCHAR(50),
        question TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        answer VARCHAR(5)
    )
    """)

    # Score history table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS scores(
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50),
        category VARCHAR(50),
        score INT,
        total INT,
        accuracy FLOAT,
        time_taken INT
    )
    """)

    conn.commit()
    conn.close()
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()
