class Controller:

    def __init__(self, root, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.root.mainloop()
