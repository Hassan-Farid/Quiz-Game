import tkinter as tk
import random as random
import message as msg

class Play():

    def __init__(self, master, value, user, score):
        self.master = master
        self.value = value
        self.user = str(user)
        self.score = score
        
        self.quesWin = tk.Toplevel(self.master)
        self.quesWin.title("Questions")
        self.quesWin.configure(bg="purple")
        self.quesWin.wm_state("zoomed")

        self.ques = tk.StringVar()
        self.ans1 = tk.StringVar()
        self.ans2 = tk.StringVar()
        self.ans3 = tk.StringVar()
        self.ans4 = tk.StringVar()
        self.ans = tk.StringVar()
        self.scorevalue = tk.StringVar()
        self.repo = tk.StringVar()

        self.num = random.randint(0, 74)
                    
        self.file = self.check_file().readlines()
        self.create_ques()

             
        self.ques_label =  tk.Label(self.quesWin,bg='black', fg='yellow' ,font='Times 16 italic', textvariable=self.ques, borderwidth=10, relief=tk.RAISED)
        self.ques_label.place(x=0,y=0, width=1368, height=200)

        self.opt1_button =  tk.Button(self.quesWin,  bg='black', fg='yellow', font='Times 16 italic', textvariable=self.ans1, borderwidth=8, relief=tk.RAISED, command= lambda: self.check_ans(self.ans1_string))
        self.opt1_button.place(x=20,y=300, width=500, height=100)

        self.opt2_button =  tk.Button(self.quesWin,  bg='black', fg='yellow', font='Times 16 italic', textvariable=self.ans2, borderwidth=8, relief=tk.RAISED, command= lambda: self.check_ans(self.ans2_string))
        self.opt2_button.place(x=600,y=300, width=500, height=100)

        self.opt3_button =  tk.Button(self.quesWin,  bg='black', fg='yellow', font='Times 16 italic', textvariable=self.ans3, borderwidth=8, relief=tk.RAISED, command= lambda: self.check_ans(self.ans3_string))
        self.opt3_button.place(x=20,y=450, width=500, height=100)

        self.opt4_button =tk.Button(self.quesWin,  bg='black', fg='yellow', font='Times 16 italic', textvariable=self.ans4, borderwidth=8, relief=tk.RAISED, command= lambda: self.check_ans(self.ans4_string))
        self.opt4_button.place(x=600,y=450, width=500, height=100)

        self.exit_ques_button = tk.Button(self.quesWin, text='FORFEIT', bg='black', fg='yellow', font='Times 16 bold italic', borderwidth=8, relief=tk.RAISED, command=lambda: msg.Message(self.quesWin, "Are you sure you want to quit?"))
        self.exit_ques_button.place(x=450, y=600, width=200)
        
        self.quesWin.mainloop()


    def check_file(self):
        if self.value == "Sports":
            f = open(r"text files/sprt_py.txt","r")

        elif self.value == "History":
            f = open(r"text files/his_py.txt","r")

        elif self.value == "Science":
            f = open(r"text files/sci_py.txt","r")

        elif self.value == "GeneralKnowledge":
            f = open(r"text files/gk_py.txt","r")

        elif self.value == "Geography":
            f = open(r"text files/geo_py.txt","r")

        elif self.value == "Maths":
            f = open(r"text files/maths_py.txt","r")

        return f

    def create_ques(self):
        self.ques_string = str(self.file[(self.num*7)]).rstrip('\n')
        self.ques.set(self.ques_string)

        self.ans1_string = (str(self.file[(self.num*7)+1]).rstrip('\n')).rstrip(' ')
        self.ans1.set(self.ans1_string)

        self.ans2_string = (str(self.file[(self.num*7)+2]).rstrip('\n')).rstrip(' ')
        self.ans2.set(self.ans2_string)
        
        self.ans3_string = (str(self.file[(self.num*7)+3]).rstrip('\n')).rstrip(' ')
        self.ans3.set(self.ans3_string)

        self.ans4_string = (str(self.file[(self.num*7)+4]).rstrip('\n')).rstrip(' ')
        self.ans4.set(self.ans4_string)

        self.ans_string = (str(self.file[(self.num*7)+6]).rstrip('\n')).rstrip(' ')
        self.ans.set(self.ans_string)


    def check_ans(self, choosen):
        self.choosen = choosen
        
        if self.choosen == self.ans_string:
            self.delete()
            self.score += 50
            self.__init__(self.master, self.value, self.user, self.score)
        else:
            self.check_score()                
            self.scorevalue.set('Your score: ' + str(self.score))
            self.delete()
            self.display_score()

    def check_score(self):
        if self.score == 0:
            self.repo.set('Repo: Poor Performance')
        elif self.score > 0 and self.score <= 250:
            self.repo.set('Repo: Bad Performance')
        elif self.score > 250 and self.score <= 500:
            self.repo.set('Repo: Nice Performance')
        elif self.score > 500 and self.score <= 750:
            self.repo.set('Repo: Good Performance')
        elif self.score > 750 and self.score <= 1000:
            self.repo.set('Repo: Excellent Performance')
        elif self.score > 1000 and self.score <= 2000:
            self.repo.set('Repo: Marvellous Performance')
        elif self.score > 2000:
            self.repo.set("Repo: Legendary Performance")

    def display_score(self):
        self.scoreWin = tk.Toplevel(self.master)
        self.scoreWin.title("Score")
        self.scoreWin.configure(bg = "purple")
        self.scoreWin.wm_state("zoomed")
                    
        self.score_title_label = tk.Label(self.scoreWin, bg='black', fg='yellow', text='SCORES',  font='Times 48 bold italic', borderwidth=20, relief=tk.RAISED)
        self.score_title_label.place(x=400, y=0, width=500)

        self.playername_label = tk.Label(self.scoreWin, bg='black' , fg='yellow', textvariable= self.user, font='Times 20 italic')
        self.playername_label.place(x=150, y=125, width=1000, height=50)

        self.score_label = tk.Label(self.scoreWin, bg='black' , fg='yellow', textvariable= self.scorevalue, font='Times 20 italic')
        self.score_label.place(x=150, y=275, width=1000, height=50)

        self.repo_label = tk.Label(self.scoreWin, bg='black' , fg='yellow', textvariable= self.repo, font='Times 20 italic')
        self.repo_label.place(x=150, y=435, width=1000, height=50)

        self.scoreWin.mainloop()

    def delete(self):
        self.quesWin.destroy()
