# Text annotation tool
**DummyAnnotator** is a fun and interactive tool for Named Entity Recognition (NER) annotation. Using this tool, you can import text files, select entities, and tag them with different classes, each highlighted in a unique color for easy identification.

## Features

- Import and display text files for annotation.
- Annotate entities by selecting text and choosing a class.
- Highlight annotations with different colors for each class.
- Save annotations to a JSON file.
- Simple and intuitive graphical user interface (GUI) built with Tkinter.

## Installation

To use DummyAnnotator, you need Python 3.x and the Tkinter library. You can install Tkinter using the following command:

```bash
pip install tk
```

## Usage
- Clone the repository:
```bash
git clone https://github.com/mjiid/Dummy-Annotator
cd Dummy-Annotator
```
- Run the application:
```bash
python main.py
```

## How to Annotate
- **Load Text**: Click the "Load Text" button to import a text file.
- **Select Text**: Highlight the text you want to annotate.
- **Choose a Class**: Select the appropriate class from the list to annotate the selected text. The text will be highlighted in the color associated with the class.
- **Save Annotations**: Click the "Save Annotations" button to save your annotations to a JSON file.

## Classes and Colors
DummyAnnotator highlights each class with a different color. You can customize these colors in the 'class_color_mapping' dictionary in the 'CustomText' class.

## Example JSON Output
The saved annotations will be in the following format:

```json
{
    "text": "Your imported text goes here.",
    "annotations": [
        {
            "text": "selected text",
            "start": "1.0",
            "end": "1.5",
            "label": "Class1"
        },
        {
            "text": "another selection",
            "start": "2.0",
            "end": "2.3",
            "label": "Class2"
        }
    ]
}
```

## Features need to be added:
- GPT API for a pre-annotation phase.
- Better UI/UX.
- Enable modifying an annotated data in JSON format 