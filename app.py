from user_auth import signup, login
from quiz_engine import start_quiz

def main():
    print("--------------------------------")
    print("        QUIZ BUDDY")
    print("--------------------------------")

    print("1. Login")
    print("2. Signup")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")

        course = login(username, password)
        if course:
            print(f"Login Successful! Course: {course}")
            show_menu(username)
        else:
            print("Invalid credentials!")

    elif choice == "2":
        username = input("Create username: ")
        password = input("Create password: ")
        course   = input("Enter course: ")

        if signup(username, password, course):
            print("Account created!")
        else:
            print("Username already exists!")

def show_menu(username):
    while True:
        print("\n----- QUIZ MENU -----")
        print("1. Python")
        print("2. SQL")
        print("3. Aptitude")
        print("4. Logout")

        ch = input("Choose category: ")

        if ch == "1":
            start_quiz(username, "Python")
        elif ch == "2":
            start_quiz(username, "SQL")
        elif ch == "3":
            start_quiz(username, "Aptitude")
        elif ch == "4":
            break

if __name__ == "__main__":
    main()
