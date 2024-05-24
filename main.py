from gui.annotation import NERAnnotationTool
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = NERAnnotationTool(root)
    root.mainloop()
