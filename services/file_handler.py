import json
from tkinter import filedialog

class FileHandler:
    def load_text_file(self):
        return filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    def save_text_file(self):
        return filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    def export_json(self):
        return filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(self, file_path, text):
        with open(file_path, 'w') as file:
            file.write(text)

    def write_json(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
