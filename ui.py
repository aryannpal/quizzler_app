from quiz_brain import QuizBrain
from tkinter import  *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        self.score_label=Label(text=f"Score:{0}", fg="white",highlightthickness=0,bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas=Canvas(width=300,height=250,highlightthickness=0,bg="white")
        self.question_text=self.canvas.create_text(
            150,
            126,
            width=280,
            text=f"question will be here",
            font=("Arial",20,"italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        img1=PhotoImage(file="images/true.png")
        self.right_button=Button(image=img1,highlightthickness=0,command=self.true_pressed)
        self.right_button.grid(row=2,column=0)

        img2 = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=img2,highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You've Reached End OF the QUIZ")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedbacks(self.quiz.check_answer(user_answer='True'))

    def false_pressed(self):
        is_true=self.quiz.check_answer(user_answer='False')
        self.give_feedbacks(is_true)

    def give_feedbacks(self,is_true):
        if is_true:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)

