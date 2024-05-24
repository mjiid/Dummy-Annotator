import tkinter as tk
from tkinter import messagebox
from gui.text_area import CustomText
from gui.class_manager import ClassManager
from services.file_handler import FileHandler
from services.token_manager import TokenManager

class NERAnnotationTool:
    def __init__(self, root):
        self.root = root
        self.root.title("NER Annotation Tool")

        self.file_handler = FileHandler()
        self.token_manager = TokenManager()

        # Text area for displaying and editing the text
        self.text_area = CustomText(root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        # Frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X)

        # Buttons for loading and saving
        self.load_button = tk.Button(self.button_frame, text="Load Text", command=self.load_text)
        self.load_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Save Annotations", command=self.save_annotations)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_class_button = tk.Button(self.button_frame, text="Add Class", command=self.add_class)
        self.add_class_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Listbox for displaying available classes
        self.class_manager = ClassManager(root, self.text_area, self.annotate)
        self.class_manager.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)

        # Bind text selection event
        self.text_area.bind("<<Selection>>", self.on_selection)

    def load_text(self):
        file_path = self.file_handler.load_text_file()
        if file_path:
            text = self.file_handler.read_file(file_path)
            self.text_area.set_text(text)

    def save_annotations(self):
        file_path = self.file_handler.export_json()
        if file_path:
            annotations = self.token_manager.get_annotations()
            data = {
                "text": self.text_area.get_text(),
                "annotations": annotations
            }
            self.file_handler.write_json(file_path, data)

    def annotate(self, label):
        try:
            # Get the selected text
            selected_text = self.text_area.get_selection_text()  
            # Get the start index of the selection
            start_index = self.text_area.index(tk.SEL_FIRST)  
            # Get the end index of the selection
            end_index = self.text_area.index(tk.SEL_LAST)  

            if selected_text and label:
                # Create an annotation dictionary
                annotation = {
                    "text": selected_text,
                    "start": start_index,
                    "end": end_index,
                    "label": label
                }
                # Add the annotation to the TokenManager
                self.token_manager.add_annotation(annotation)
                # Highlight the annotated text in the text area
                self.text_area.annotate_text(start_index, end_index, label)
            else:
                messagebox.showwarning("Warning", "Please select text and choose a label.")
        except tk.TclError:
            messagebox.showwarning("Warning", "No text selected.")

    def on_selection(self, event):
        selection = self.text_area.get_selection_range()
        if selection:
            selected_text = self.text_area.get_text_range(*selection)
            print(f"Selected text: {selected_text}")

    def add_class(self):
        new_class = self.class_manager.add_class_dialog()
        if new_class:
            self.class_manager.add_class(new_class)

