from database import get_connection
import random
import time

def fetch_questions(category, limit=5):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM questions WHERE category=%s", (category,))
    data = cur.fetchall()

    conn.close()

    random.shuffle(data)
    return data[:limit]

def start_quiz(username, category):
    questions = fetch_questions(category)
    correct = 0
    total = len(questions)

    start_time = time.time()

    for q in questions:
        print("\n------------------------------------")
        print(q[2])  # question
        print("A.", q[3])
        print("B.", q[4])
        print("C.", q[5])
        print("D.", q[6])

        ans = input("Enter your answer (A/B/C/D): ").upper()

        if ans == q[7].upper():
            print("Correct!")
            correct += 1
        else:
            print("Wrong!")

    end_time = time.time()
    time_taken = int(end_time - start_time)
    accuracy = (correct / total) * 100

    save_score(username, category, correct, total, accuracy, time_taken)

    print("\n===== RESULT =====")
    print("Score:", correct, "/", total)
    print("Accuracy:", round(accuracy, 2), "%")
    print("Time Taken:", time_taken, "seconds")

def save_score(username, category, score, total, accuracy, time_taken):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO scores(username, category, score, total, accuracy, time_taken)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (username, category, score, total, accuracy, time_taken))

    conn.commit()
    conn.close()
