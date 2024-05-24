import tkinter as tk
import random

class CustomText(tk.Text):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.color_dict = {}

    def set_text(self, text):
        self.delete(1.0, tk.END)
        self.insert(tk.END, text)

    def get_text(self):
        return self.get(1.0, tk.END)

    def get_text_range(self, start, end):
        return self.get(start, end)

    def get_selection_range(self):
        try:
            return self.index(tk.SEL_FIRST), self.index(tk.SEL_LAST)
        except tk.TclError:
            return None

    def get_selection_text(self):
        try:
            return self.get(tk.SEL_FIRST, tk.SEL_LAST)
        except tk.TclError:
            return ""

    def color_map(self, annotation_class):
        if annotation_class not in self.color_dict:
            self.color_dict[annotation_class] = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        return self.color_dict[annotation_class]

    def annotate_text(self, start, end, annotation_class):
        self.tag_add(annotation_class, start, end)
        self.tag_config(annotation_class, background=self.color_map(annotation_class))