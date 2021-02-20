import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
import numpy as np
from tkinter import messagebox
import os


class CreateQuizGUI(tk.Tk):

    def __init__(self, questions, answers, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # Create frames
        page_name = StartPage.__name__
        frame = StartPage(parent=container, controller=self)
        self.frames[page_name] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        for i in np.arange(1, len(questions) + 1, 1):
            page_name = "Page_" + str(i)
            next_name = "Page_" + str(i + 1)
            if i - 1 == 0:
                back_name = "StartPage"
            else:
                back_name = "Page_" + str(i - 1)
            frame = QuestionPage(parent=container, controller=self, next_name=next_name, back_name=back_name,
                                 title="Question " + str(i) + " of " + str(len(questions)), question=questions[i - 1], answer=answers[i - 1])
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Quizzer!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Begin the quiz",
                            command=lambda: controller.show_frame("Page_1"))
        button1.pack()


class QuestionPage(tk.Frame):

    def __init__(self, parent, controller, back_name, next_name, title, question, answer):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = title
        self.question = question
        self.answer = answer
        title_label = tk.Label(self, text=title)
        title_label.pack(side="top", fill="both", expand=True, padx=0, pady=0)
        label = tk.Label(self, text=question, font=controller.title_font)
        label.pack(side="top", fill="both", expand=True, padx=0, pady=0)
        back_button = tk.Button(self, text="Go back",
                                command=lambda: controller.show_frame(back_name))
        next_button = tk.Button(self, text="Go Next Question",
                                command=lambda: controller.show_frame(next_name))

        def show_answer():
            tk.messagebox.showinfo(self.question, self.answer)

        answer_button = tk.Button(self, text="Show Answer", command=show_answer)
        answer_button.pack(side="top",fill='both', expand=True, padx=0, pady=0)
        back_button.pack(side="left", expand=True, padx=0, pady=0)
        next_button.pack(side="left", expand=True, padx=0, pady=0)

