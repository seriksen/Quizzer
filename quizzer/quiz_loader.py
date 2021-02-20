import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import pandas as pd
import numpy

def select_quiz():
    filename = filedialog.askopenfilename(initialdir=os.curdir,
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.xls"),
                                                     ("all files",
                                                      "*.*")))

    return filename


def load_questions_and_answers(filename):
    data = pd.read_excel(filename)

    # Info is in column 5 and 6 named 'Unnamed: 5' and 'Unnamed: 6'
    # Use arrays (Can impliment most of the above in array form which will be much faster)
    questions = data['Questions'].dropna().to_numpy()
    answers = data['Answers'].dropna().to_numpy()

    return questions, answers
