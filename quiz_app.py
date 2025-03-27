import streamlit as st
import sqlite3
import random

# Set Dark Theme
st.set_page_config(page_title="Python Quiz", page_icon="🧠", layout="wide")


# Custom CSS
st.markdown(
    """
    <style>
        .stApp {
            background-color: #222222;
        }
        .stButton>button {
            background-color: #6A0DAD !important;
            color: white;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Connect to Database
conn = sqlite3.connect("quiz.db", check_same_thread=False)
cursor = conn.cursor()

# Load Questions Into Session State
if "questions" not in st.session_state:
    cursor.execute("SELECT * FROM quiz_questions")
    all_questions = cursor.fetchall()
    st.session_state.questions = random.sample(all_questions, min(5, len(all_questions)))

# Define `questions` Always
questions = st.session_state.questions

# Initialize Quiz State
if "quiz_state" not in st.session_state:
    st.session_state.quiz_state = {
        "score": 0,
        "current_question": 0,
        "quiz_over": False,
        "submitted": False,
        "user_answer": None
    }

# Display Header
st.title("🐍 Python Quiz Game")
st.subheader("Test your Python knowledge! 🎯")

# 📌 Sidebar Instructions
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4494/4494703.png", width=100)
st.sidebar.header("📜 Instructions")
st.sidebar.info("""
- Choose the correct answer from the options.
- Each correct answer gives **1 point**.
- Click **Submit Answer** to proceed.
- Final score will be displayed at the end!
""")

# Display Questions
if not st.session_state.quiz_state["quiz_over"]:
    q_index = st.session_state.quiz_state["current_question"]
    question = questions[q_index]
    
    question_text, opt_a, opt_b, opt_c, opt_d, correct_ans = question[1], question[2], question[3], question[4], question[5], question[6]
    
    st.write(f"**Question {q_index + 1} of {len(questions)}:**")
    st.write(f"🧐 {question_text}")

    options = [opt_a, opt_b, opt_c, opt_d]

    user_answer = st.radio("Select your answer:", options, index=None, key=f"q_{q_index}")

    # Submit Answer
    if st.button("Submit Answer") and not st.session_state.quiz_state["submitted"]:
        if user_answer:
            correct_option = options[ord(correct_ans.upper()) - ord('A')]

            if user_answer == correct_option:
                st.session_state.quiz_state["score"] += 1
                st.success("✅ Correct Answer!")
            else:
                st.error(f"❌ Wrong! The correct answer was: {correct_option}")

            st.session_state.quiz_state["submitted"] = True
        else:
            st.warning("⚠️ Please select an answer before submitting.")

    # Next Question
    if st.session_state.quiz_state["submitted"]:
        if st.button("Next Question"):
            st.session_state.quiz_state["current_question"] += 1
            st.session_state.quiz_state["submitted"] = False

            if st.session_state.quiz_state["current_question"] >= len(questions):
                st.session_state.quiz_state["quiz_over"] = True

            st.rerun()
st.image(["Quiz.png"], caption=["A Cozy Library"], use_container_width=True)
# Display Final Score
if st.session_state.quiz_state["quiz_over"]:
    st.write("## 🎊 Quiz Completed!")
    st.write(f"📊 Your final score: **{st.session_state.quiz_state['score']} / {len(questions)}**")

    # Restart Quiz
    if st.button("🔄 Restart Quiz"):
        st.session_state.quiz_state = {
            "score": 0,
            "current_question": 0,
            "quiz_over": False,
            "submitted": False,
            "user_answer": None
        }
        st.rerun()


    # 🎯 Show Motivational Message
    if st.session_state.quiz_state["score"] == len(questions):

        st.success("🌟 Excellent! You're a Python expert! 🐍🔥")
    elif st.session_state.quiz_state["score"] >= len(questions) // 2:

        st.info("👍 Good job! Keep practicing!")
    else:
        st.warning("🔁 Keep learning! Python mastery takes time.")




# 🎯 Sidebar User Goal
st.sidebar.markdown("---")
user_goal = st.sidebar.selectbox("What's your learning goal?", 
                                 ["Become a Python Expert", "Improve Problem Solving", "Learn Web Development", "Master Data Science"])
st.sidebar.write(f"🎯 Your goal: {user_goal}")

# --- Contact Us Section ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")
