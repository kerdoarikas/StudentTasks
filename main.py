import tkinter as tk
from Controller import Controller

if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Ülesannete jagaja -> Kerdo Arikas-TAK22")
    photo = tk.PhotoImage(file='mix.png')
    root.wm_iconphoto(False, photo)

    Controller(root).run()
