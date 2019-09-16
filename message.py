import tkinter as tk

class Message():

    def center(self, root):
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def __init__(self, master, text):
        self.master = master
        self.text = text
        
        self.message = tk.Toplevel(self.master)
        self.message.title('Message')
        self.center(self.message)
        self.message.configure(bg = 'black')

        self.messageLabel = tk.Label(self.message, bg='black', fg='yellow', text=self.text , font='Times 10 italic')
        self.messageLabel.place(x = 0, y = 40, width = 200)

        self.yesBtn = tk.Button(self.message, bg='black', fg='yellow', text='YES', borderwidth=4, relief=tk.RAISED, command= self.delete)
        self.yesBtn.place(x = 25, y = 100, width = 50)

        self.noBtn = tk.Button(self.message, bg='black', fg='yellow', text='NO', borderwidth=4, relief=tk.RAISED, command= self.deleteMes)
        self.noBtn.place(x = 125, y = 100, width = 50)

    def deleteMes(self):
        self.message.destroy()

    def delete(self):
        self.master.destroy()
        
        

