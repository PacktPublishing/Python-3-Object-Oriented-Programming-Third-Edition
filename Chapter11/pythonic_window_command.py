import sys


class Window:
    def exit(self):
        sys.exit(0)


class MenuItem:
    def click(self):
        self.command()


window = Window()
menu_item = MenuItem()
menu_item.command = window.exit


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, "w") as file:
            file.write(self.contents)


class KeyboardShortcut:
    def keypress(self):
        self.command()


class SaveCommand:
    def __init__(self, document):
        self.document = document

    def __call__(self):
        self.document.save()


document = Document("a_file.txt")
shortcut = KeyboardShortcut()
save_command = SaveCommand(document)
shortcut.command = save_command
