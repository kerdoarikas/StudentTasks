import os
from Model import Model
from View import View
import tkinter as tk
from tkinter import filedialog, messagebox


class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self.model, self)
        self.root = root
        self.current_mixmatch = self.model.mixmatch()

        self.main_dir = os.path.dirname(p=os.path.abspath("~/"))

        self.open_filetype = [('Textfiles', '*.txt')]
        self.save_filetype = [('Textfiles', '*.txt')]

    def run(self):

        self.view.root.mainloop()

    def load_names(self):

        file_path = filedialog.askopenfilename(filetypes=self.open_filetype, initialdir=self.main_dir)
        if file_path:
            with open(file_path, encoding='utf-8') as f:
                self.model.names = [line.strip() for line in f]

            self.view.names_listbox.delete(0, tk.END)
            for name in self.model.names:
                self.view.names_listbox.insert(tk.END, name)
            print(len(self.model.names))

        if len(self.model.names) == 0 or len(self.model.names) > 20:
            self.view.listlenght = 20
            self.view.names_listbox.config(height=self.view.listlenght)
            self.view.tasks_listbox.config(height=self.view.listlenght)
            self.view.mixed_listbox.config(height=self.view.listlenght)
        elif len(self.model.names) < 20:
            self.view.listlenght = len(self.model.names)
            self.view.names_listbox.config(height=self.view.listlenght)
            self.view.tasks_listbox.config(height=self.view.listlenght)
            self.view.mixed_listbox.config(height=self.view.listlenght)

    def load_tasks(self):

        file_path = filedialog.askopenfilename(filetypes=self.open_filetype, initialdir=self.main_dir)
        if file_path:

            with open(file_path, encoding='utf-8') as f:
                self.model.tasks = [line.strip() for line in f]

            self.view.tasks_listbox.delete(0, tk.END)
            for task in self.model.tasks:
                self.view.tasks_listbox.insert(tk.END, task)


    def mixmatch(self):
        if len(self.model.names) == 0 or len(self.model.tasks) == 0:
            messagebox.showerror('Viga!', 'Pole midagi jagada !')
        else:
            self.view.mixed_listbox.delete(0, tk.END)
            self.current_mixmatch = list(self.model.mixmatch())
            for name, task in self.current_mixmatch:
                self.view.mixed_listbox.insert(tk.END, f'{name} - {task}')

    def save(self):
        if len(self.current_mixmatch) == 0:
            messagebox.showerror('Viga!', 'Pole midagi salvestada !')
        else:
            file_path = filedialog.asksaveasfilename(filetypes=self.save_filetype,
                                                     defaultextension='.txt', initialdir=self.main_dir)
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    for name, task in self.current_mixmatch:
                        f.write(f'{name} - {task}\n')

    def delete_all(self):
        self.view.names_listbox.delete(0, tk.END)
        self.view.tasks_listbox.delete(0, tk.END)
        self.view.mixed_listbox.delete(0, tk.END)
        self.current_mixmatch = []
        self.model.names = []
        self.model.tasks = []

