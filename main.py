import tkinter as tk
import rungame as rg
from winsound import *

def playsound():
    PlaySound('music.wav', SND_FILENAME|SND_LOOP|SND_ASYNC)

def main():
    gameWin = tk.Tk()
    gameWin.title("Quiz Game (Application) ")
    gameWin.configure(bg = "purple")
    gameWin.wm_state("zoomed")
    playsound()
    runApp = rg.maingame(gameWin)
    gameWin.mainloop()

if __name__ == "__main__":
    main()
