import tkinter as tk
from tkinter import messagebox



def make_quiz_gui():
    window = tk.Tk()

    window.title("A Little Quiz")

    question = tk.Label(window, text="Here is where the question could go...:")
    question.grid(column=0, row=0)

    def show_answer():
        tk.messagebox.showinfo('Question Answer', 'This is where the answer will be')


    show_answer_button = tk.Button(window, text="Show Answer", command=show_answer)
    show_answer_button.grid(column=1, row=0)

    #def next_question():


    window.mainloop()

make_quiz_gui()