import tkinter as tk
from tkinter import filedialog


class View:
    def __init__(self, root, model):
        self.root = root
        self.model = model

        self.open_filetype = ('Textfiles', '*.txt'), ('All files', '*.*')
        self.save_filetype = ('Textfiles', '*.txt'), ('CSV', '*.csv')

        self.names_label = tk.Label(root, text='Nimed')
        self.names_label.grid(row=0, column=0, padx=10, pady=10)
        self.names_entry = tk.Entry(root, width=30)
        self.names_entry.grid(row=1, column=0, padx=10, pady=10)
        self.names_button = tk.Button(root, text='Vali nimede fail', command=self.load_names)
        self.names_button.grid(row=2, column=0, padx=10, pady=10)

        self.names_listbox = tk.Listbox(root, width=60)
        self.names_listbox.grid(row=3, rowspan=4, column=0, padx=10, pady=10)

        self.tasks_label = tk.Label(root, text='Ülesanded')
        self.tasks_label.grid(row=0, column=1, padx=10, pady=10)
        self.tasks_entry = tk.Entry(root, width=30)
        self.tasks_entry.grid(row=1, column=1, padx=10, pady=10)
        self.tasks_button = tk.Button(root, text='Vali ülesannete fail', command=self.load_tasks)
        self.tasks_button.grid(row=2, column=1, padx=10, pady=10)

        self.tasks_listbox = tk.Listbox(root, width=60)
        self.tasks_listbox.grid(row=3, rowspan=4, column=1, padx=10, pady=10)

        self.mixmatch_button = tk.Button(root, text='Sega ülesanded', command=self.mixmatch)
        self.mixmatch_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Salvestusnupp
        self.save_button = tk.Button(root, text='Salvesta', command=self.save)
        self.save_button.grid(row=7, column=2, columnspan=2, padx=10, pady=10)

        # Segatud ülessanded
        self.output_label = tk.Label(root, text='Väljund')
        self.output_label.grid(row=0, column=2, rowspan=3, padx=10, pady=10)
        self.mixed_listbox = tk.Listbox(root, width=60)
        self.mixed_listbox.grid(row=3, rowspan=4, column=2, padx=10, pady=10)


    def load_names(self):
        file_path = filedialog.askopenfilename(filetypes=self.open_filetype)
        if file_path:
            self.names_entry.delete(0, tk.END)
            self.names_entry.insert(0, file_path)
            with open(file_path, encoding='utf-8') as f:
                self.model.names = [line.strip() for line in f]

            self.names_listbox.delete(0, tk.END)
            for name in self.model.names:
                self.names_listbox.insert(tk.END, name)

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=self.open_filetype)
        if file_path:
            self.tasks_entry.delete(0, tk.END)
            self.tasks_entry.insert(0, file_path)
            with open(file_path, encoding='utf-8') as f:
                self.model.tasks = [line.strip() for line in f]

            self.tasks_listbox.delete(0, tk.END)
            for task in self.model.tasks:
                self.tasks_listbox.insert(tk.END, task)

    def mixmatch(self):
        self.mixed_listbox.delete(0, tk.END)
        self.current_mixmatch = list(self.model.mixmatch())
        for name, task in self.current_mixmatch:
            self.mixed_listbox.insert(tk.END, f'{name} - {task}')

    def save(self):
        file_path = filedialog.asksaveasfilename(filetypes=self.save_filetype, defaultextension='.txt')
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                for name, task in self.current_mixmatch:
                    f.write(f'{name} - {task}\n')

