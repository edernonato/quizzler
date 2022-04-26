from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.score = 0
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(
            text=f"Score: {self.score}",
            font=("Arial", 15, "normal"),
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.false_button = Button(image=false_img, command=self.wrong_button)
        self.false_button.grid(row=2, column=0)
        self.true_button = Button(image=true_img, command=self.right_button)
        self.true_button.grid(row=2, column=1)
        self.generate_question()

        self.window.mainloop()

    def generate_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Game Over. Your final score was:"
                                                            f" {self.score}/{self.quiz.question_number}")
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def right_button(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.update_score(is_right)

    def wrong_button(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.update_score(is_right)

    def update_score(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score = self.quiz.score
        self.score_label.config(text=f"Score: {self.score}")
        self.window.after(1000, self.generate_question)


