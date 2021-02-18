import quiz_loader
import quiz_gui

def main():

    file_name = quiz_loader.select_quiz()
    print('got')
    print(file_name) #print("Do things")
    questions, answers = quiz_loader.load_questions_and_answers(file_name)
    print(questions)
    print(answers)

    app = quiz_gui.CreateQuizGUI(questions, answers);
    app.mainloop()

if __name__ == "__main__":
    main()
