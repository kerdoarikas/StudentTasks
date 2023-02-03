import tkinter as tk
import tkinter.font as tkfont
from PIL import ImageTk, Image


class View:
    def __init__(self, root, model, controller):
        self.root = root
        self.model = model
        self.controller = controller

        self.listlenght = 20

        # Save ikoon
        self.save_img = Image.open("save.png")
        self.resized_save = self.save_img.resize((25, 25), Image.ANTIALIAS)
        self.new_save = ImageTk.PhotoImage(self.resized_save)
        # Mix ikoon
        self.mix_img = Image.open("mix.png")
        self.resized_mix = self.mix_img.resize((25, 25), Image.ANTIALIAS)
        self.new_mix = ImageTk.PhotoImage(self.resized_mix)
        # Upload ikoon
        self.up_img = Image.open("upload.png")
        self.resized_up = self.up_img.resize((15, 15), Image.ANTIALIAS)
        self.new_up = ImageTk.PhotoImage(self.resized_up)
        # Delete ikoon
        self.del_img = Image.open("delete.png")
        self.resized_del = self.del_img.resize((15, 15), Image.ANTIALIAS)
        self.new_del = ImageTk.PhotoImage(self.resized_del)

        self.root.configure(background='#121212')

        self.big_font_style = tkfont.Font(family='Helvetica', size=18, weight='bold')
        self.default_style_bold = tkfont.Font(family='Helvetica', size=14, weight='bold')
        self.default_style = tkfont.Font(family='Helvetica', size=10)

        self.header_label = tk.Label(root, text='-ÜLESANNETE JAGAJA-', font=self.big_font_style,
                                     bg='#121212', fg='#0275d8')
        self.header_label.grid(row=0, column=0, columnspan=3, pady=20)

        self.delete_button = tk.Button(root, text='  Tühjenda kõik', image=self.new_del, compound='left',
                                      command=self.controller.delete_all,
                                      bg='#d9534f',
                                      fg='#ffffff',
                                      bd=0,
                                      font=self.default_style,
                                      height=20,
                                      width=130)

        self.delete_button.grid(row=0, column=2, padx=10, pady=10)

        self.names_button = tk.Button(root, text='  Vali nimede fail', image=self.new_up, compound='left',
                                      command=self.controller.load_names,
                                      bg='#0275d8',
                                      fg='#ffffff',
                                      bd=0,
                                      font=self.default_style,
                                      height=20,
                                      width=130)

        self.names_button.grid(row=1, column=0, padx=10, pady=10)

        self.names_listbox = tk.Listbox(root, height=self.listlenght, width=60, bd=0, bg='#292b2c', fg='white')
        self.names_listbox.grid(row=3, rowspan=5, column=0, padx=10, pady=10)

        self.tasks_button = tk.Button(root, text='  Vali ülesannete fail', image=self.new_up,
                                      compound='left',
                                      command=self.controller.load_tasks,
                                      bg='#0275d8',
                                      fg='#ffffff',
                                      bd=0,
                                      font=self.default_style,
                                      height=20,
                                      width=150)

        self.tasks_button.grid(row=1, column=1, padx=10, pady=10)

        self.tasks_listbox = tk.Listbox(root, height=self.listlenght, width=60, bd=0, bg='#292b2c', fg='white')
        self.tasks_listbox.grid(row=3, rowspan=5, column=1, padx=10, pady=10)

        self.mixmatch_button = tk.Button(root, text='   JAGA', image=self.new_mix, compound='left',
                                         command=self.controller.mixmatch,
                                         bg='#f0ad4e',
                                         fg='#ffffff',
                                         bd=0,
                                         font=self.default_style,
                                         height=40,
                                         width=150)

        self.mixmatch_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        # Salvestusnupp
        self.save_button = tk.Button(root, text='   SALVESTA', image=self.new_save, compound='left',
                                     command=self.controller.save,
                                     bg='#5cb85c',
                                     fg='#ffffff',
                                     bd=0,
                                     font=self.default_style,
                                     height=40,
                                     width=150)

        self.save_button.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

        # Segatud ülessanded
        self.output_label = tk.Label(root, text='Väljund', font=self.default_style_bold, bg='#121212', fg='#0275d8')
        self.output_label.grid(row=1, column=2, padx=10, pady=10)
        self.mixed_listbox = tk.Listbox(root, height=self.listlenght, width=60, bd=0, bg='#292b2c', fg='white')
        self.mixed_listbox.grid(row=3, rowspan=5, column=2, padx=10, pady=10)
