import tkinter as tk
import playgame as pg

class start():

    def __init__(self, master):
        self.master = master
        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.username = tk.StringVar()

        self.score = 0

        self.startWin = tk.Toplevel(self.master)
        self.startWin.title("The Ultimate Quiz Game")
        self.startWin.configure(bg='purple')
        self.startWin.wm_state("zoomed")

        self.start_title_label = tk.Label(self.startWin, bg='black', fg='yellow', text='THE ULTIMATE QUIZ GAME', font='Times 16 bold italic', borderwidth=20, relief=tk.RAISED)
        self.start_title_label.place(x=400,y=0, width=500)

        self.fname_entry_label = tk.Label(self.startWin, bg='black', fg='yellow', text='Enter your first Name: ', font='Times 32 italic', relief=tk.RAISED)
        self.fname_entry_label.place(x=100,y=100, width=500)
        self.fname_entry = tk.Entry(self.startWin, bg='black', fg='yellow', font='Times 32 italic', textvariable=self.fname)
        self.fname_entry.place(x=700,y=100, width=500, height=50)
        
        self.lname_entry_label = tk.Label(self.startWin, bg='black', fg='yellow', text='Enter your last Name: ', font='Times 32 italic', relief=tk.RAISED)
        self.lname_entry_label.place(x=100,y=200, width=500)
        self.lname_entry = tk.Entry(self.startWin, bg='black', fg='yellow', font='Times 32 italic', textvariable=self.lname)
        self.lname_entry.place(x=700,y=200, width=500, height=50)

        self.OPTIONS = [
                    "Sports",
                    "History",
                    "Science",
                    "GeneralKnowledge",
                    "Geography",
                    "Maths"
                  ]

        self.choice = tk.StringVar(self.startWin)
        self.choice.set(self.OPTIONS[0])

        
        def play(opt):
            pg.Play(self.master, opt, self.username, self.score)

        self.option_label = tk.Label(self.startWin, bg='black', fg='yellow', text='Select your choice from the categories mentioned: ', font='Times 20 italic', relief=tk.RAISED)
        self.option_label.place(x=100, y=300, width=700)
        self.optionbar = tk.OptionMenu(self.startWin, self.choice, *self.OPTIONS, command = play)
        self.optionbar.place(x=900, y=300, width=200, height=35)

        self.name_button = tk.Button(self.startWin, bg='black', fg='yellow', text='Submit Name', font='Times 16 bold italic', borderwidth=8, command = self.get_name)
        self.name_button.place(x=400, y=600)

        self.exit_startWin = tk.Button(self.startWin, text='Exit to Menu', bg='black', fg='yellow', font='Times 16 bold italic', borderwidth=8, command= self.delete)
        self.exit_startWin.place(x=600, y=600)

        self.startWin.mainloop()

    def delete(self):
        self.startWin.destroy()

    def get_name(self):
        firstname = self.fname.get()
        lastname = self.lname.get()
        self.username.set('Your name: ' + firstname + '' + lastname)
