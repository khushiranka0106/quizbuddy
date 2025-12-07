# Quiz Buddy 🎯  
A Python + MySQL based quiz application with login/signup, course selection, score tracking, and category-wise quizzes.

## 📌 Overview
**Quiz Buddy** is a simple yet functional command-line quiz application built using **Python** and **MySQL**.  
It allows users to create accounts, log in, take quizzes from different categories, and track their performance with score, accuracy, and time taken.

This project helped me understand:
- Backend logic using Python  
- Database integration using MySQL  
- User authentication  
- Fetching and storing data  
- Clean modular project structure  


## 🚀 Features
- 🔐 **User Signup & Login** (stored in MySQL)
- 🎓 **Course selection**
- 📚 **Multiple quiz categories** (Python, SQL, Aptitude)
- 🔄 **Randomized question selection**
- 🧮 **Score + Accuracy + Time tracking**
- 🗂 **MySQL database with three tables:** users, questions, scores
- 🔧 **Modular Python code** (easy to maintain and extend)


## 🛠 Tech Stack
- **Python**
- **MySQL**
- **mysql-connector-python**



## 📁 Project Structure
```plaintext
quiz_buddy/
│── app.py              # Main application flow
│── user_auth.py        # Handles login & signup
│── quiz_engine.py      # Quiz logic (questions, scoring)
│── database.py         # DB connection + table creation
│── requirements.txt    # Required Python packages
│── README.md
```


## 🗄 Database Schema

### users
| Column    | Type        |
|-----------|-------------|
| id        | INT (PK)    |
| username  | VARCHAR(50) |
| password  | VARCHAR(50) |
| course    | VARCHAR(50) |

---

### questions
Stores all quiz questions with 4 options and the correct answer.

---

### scores
Stores quiz results:
- username  
- category  
- score  
- accuracy  
- time_taken  


## ▶️ How to Run
1. Clone the repository:
git clone https://github.com/khushiranka0106/quizbuddy.git
cd quizbuddy

2. Install dependencies:
pip install -r requirements.txt

3. Create MySQL database:
CREATE DATABASE quizbuddy;

4. Run the project:
python app.py

# 📌 Future Improvements

📊 Score analytics using Pandas

🏆 Leaderboard

🧩 Difficulty levels

🎨 Improved UI (Rich library)

🌐 Web version using Flask

# 👩🏻‍💻 Author

Khushi Ranka
Feel free to connect or share feedback! 😊

# ⭐ Support

If you like this project, don't forget to ⭐ star the repository on GitHub!
