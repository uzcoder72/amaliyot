class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []

    def write(self, text):
        self.undo_stack.append(self.text)
        self.text += text

    def undo(self):
        if self.undo_stack:
            self.text = self.undo_stack.pop()
        else:
            print("Nothing to undo")

    def read(self):
        return self.text
    
editor = TextEditor()
editor.write("Hello")
editor.write(", World!")
print(f"Current text: {editor.read()}")

editor.undo()
print(f"Text after undo: {editor.read()}")

editor.undo()
print(f"Text after another undo: {editor.read()}")
