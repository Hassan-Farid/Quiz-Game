import tkinter as tk
import startgame as sg
import instructgame as ig
import message as msg

class maingame():

    def __init__(self, master):
        self.master = master

        self.maingameLabel = tk.Label(self.master, bg='black', fg='yellow', text='QUIZ GAME',  font='Times 48 bold italic', borderwidth=20, relief=tk.RAISED)
        self.maingameLabel.place(x=400, y=40, width=500)

        self.startBtn = tk.Button(self.master, text='START GAME', bg='black', fg='yellow', font='Times 16 bold italic', borderwidth=8, command = self.runstart)
        self.startBtn.place(x=500, y=200, width=300)

        self.instructionsBtn = tk.Button(self.master,  text='INSTRUCTIONS',bg='black', fg='yellow', font='Times 16 bold italic', borderwidth=8, command = self.runinstruct)
        self.instructionsBtn.place(x=500, y=300, width=300)

        self.exitBtn = tk.Button(self.master, text='EXIT', bg='black', fg='yellow', font='Times 16 bold italic', borderwidth=8, command = self.confirm)
        self.exitBtn.place(x=500, y=400, width=300)


    def runstart(self):
        start = sg.start(self.master)

    def runinstruct(self):
        instruct = ig.instruct(self.master)

    def confirm(self):
        confirm_mes = msg.Message(self.master, "Are you sure you want to quit?")
        


    
