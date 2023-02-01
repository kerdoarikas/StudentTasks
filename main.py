import tkinter as tk
from Model import Model
from View import View
from Controller import Controller

if __name__ == '__main__':
    root = tk.Tk()
    model = Model([], [])
    view = View(root, model)
    Controller(root, model, view).run()
