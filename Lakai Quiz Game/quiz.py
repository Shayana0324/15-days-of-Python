from tkinter import *

# Display questions and answers
def display_questions():
    question_label = Label(window, text="Question", font=("Arial", 16))
    question_label.pack(pady = 10)
    for i in range(4):
        answer_button = Button(window, text = "Answer", width=25, font=("Arial", 11))
        # answer_button = Button(window, text = "Answer", width=25, font=3)
        answer_button.pack(pady = 10)

    # Creating a list that contains a dictionary of questions, choices and answers
    questions = [
        {
            "question": "What is the product of 8 and 97", "choices": ["776", "784", "786", "792"], "answer": "776"
        },
        {   "question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"
        },
        {
            "question": "What is the largest planet in our solar system?", "choices": ["Earth", "Jupiter", "Saturn", "Mars"], "answer": "Jupiter"
        },
        {
            "question": "What is the smallest prime number?", "choices": ["0", "1", "2", "3"], "answer": "2"
        },
        {
            "question": "What is the largest ocean on Earth?", "choices": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"
        }, 
        {
            "question": "What is the chemical symbol for gold?", "choices": ["Au", "Ag", "Fe", "Hg"], "answer": "Au"
        }, 
        {
            "question": "What is the largest desert in the world?", "choices": ["Sahara Desert", "Gobi Desert", "Kalahari Desert", "Arabian Desert"], "answer": "Sahara Desert"
        },
        {
            "question": "What is the currency of Japan?", "choices": ["Yen", "Dollar", "Euro", "Pound"], "answer": "Yen"
        }
    ]

window = Tk()
window.title("Quiz Game")
window.geometry("500x500")

display_questions()
window.mainloop()
