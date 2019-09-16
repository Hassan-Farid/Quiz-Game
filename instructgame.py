import tkinter as tk

class instruct():

    def __init__(self, master):
        self.master = master
        
        self.instructWin = tk.Toplevel(self.master)
        self.instructWin.title("Instructions")
        self.instructWin.configure(bg="purple")
        self.instructWin.wm_state("zoomed")

        instruct_label = tk.Label(self.instructWin, bg='black', fg='yellow', text='INSTRUCTIONS', font='Times 16 bold italic', borderwidth=20, relief=tk.RAISED)
        instruct_label.place(x=0,y=0, width=200)

        instructions = tk.Label(self.instructWin, bg = 'dark violet', fg='black', font='Times 14 italic', text=
        """ This is the instructions section.First Type your Name in the Given username entry
            Boxes and press Submit Name button to store your name alongwith progress for later.
            If you enter the name and dont press Submit Name, your name will not be displayed
            in the Score window. Select a category from the given Option Menu of Categories.
            There are overall 6 categories i.e. Sports, History, Science, GeneralKnowledge,
            Geography and Maths. The game will start as soon as you choose a certain category.
            For each category, you will be asked unlimited number of questions. The game will
            continue until you give a wrong answer to a question. Each question is worth 50
            points. If an answer given if wrong, the Score window will open with the username,
            score and reputation of the person as to how he performed in the Quiz. The
            reputation is based on the number of questions answered correctly. Best of Luck.""",borderwidth=10, relief=tk.RAISED)
        instructions.place(x = 50, y = 100, width= 750)
        
        exit_instruct_button = tk.Button(self.instructWin, text='Exit to Menu', bg = 'black', fg='yellow', font='Times 16 bold italic', borderwidth=8, command= self.delete)
        exit_instruct_button.place(x=600, y=650)
        
        self.instructWin.mainloop()
    
    def delete(self):
        self.instructWin.destroy()
