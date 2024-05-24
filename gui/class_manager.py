import tkinter as tk
from tkinter import simpledialog

class ClassManager(tk.Frame):
    def __init__(self, root, text_area, annotate_callback):
        super().__init__(root)
        self.text_area = text_area
        self.annotate_callback = annotate_callback

        self.class_listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.class_listbox.pack(expand=True, fill=tk.BOTH)
        self.class_listbox.bind("<<ListboxSelect>>", self.on_class_select)

        self.classes = []

    def add_class_dialog(self):
        class_name = simpledialog.askstring("Input", "Enter class name:", parent=self)
        if class_name:
            return class_name.strip()
        return None

    def add_class(self, class_name):
        if class_name and class_name not in self.classes:
            self.classes.append(class_name)
            self.class_listbox.insert(tk.END, class_name)

    def on_class_select(self, event):
        selection = self.class_listbox.curselection()
        if selection:
            selected_class = self.classes[selection[0]]
            self.annotate_callback(selected_class)

    def get_selected_class(self):
        selection = self.class_listbox.curselection()
        if selection:
            return self.classes[selection[0]]
        return None
