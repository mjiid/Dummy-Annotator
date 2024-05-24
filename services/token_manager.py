class TokenManager:
    def __init__(self):
        self.annotations = []

    def add_annotation(self, annotation):
        self.annotations.append(annotation)

    def get_annotations(self):
        return self.annotations

    def clear_annotations(self):
        self.annotations = []
