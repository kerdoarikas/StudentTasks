import random
import tkinter.messagebox


class Model:

    def __init__(self, names, tasks):
        self.names = names
        self.tasks = tasks

    def mixmatch(self):
        if len(self.names) > len(self.tasks):
            tkinter.messagebox.showerror("Error", "Failis pole piisavalt ülesandeid !")
            return []

        else:
            random.shuffle(self.tasks)
            output = [(name, task) for name, task in zip(self.names, self.tasks)]
            return output
