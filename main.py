import tkinter as tk
import rungame as rg

def main():
    gameWin = tk.Tk()
    gameWin.title("Quiz Game (Application) ")
    gameWin.configure(bg = "purple")
    gameWin.wm_state("zoomed")
    runApp = rg.maingame(gameWin)
    gameWin.mainloop()

if __name__ == "__main__":
    main()
