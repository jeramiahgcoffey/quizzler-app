from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=350, height=530)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.get_next_question()

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.answer_true)
        self.true_button.config(bd=0, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.answer_false)
        self.false_button.config(bd=0, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        self.window.after_cancel(self.continue_game)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.continue_game)

    def continue_game(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.score_label.config(text=f"Quiz Complete")
            self.canvas.itemconfig(self.question_text, text=f"Your final score is "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
