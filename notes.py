class Note:
    def __init__(self, text):
        self.text = text

class Notebook:
    def __init__(self):
        self.notes = []

    def add(self, text):
        note = Note(text)
        self.notes.append(note)

    def search(self, query):
        return [note for note in self.notes if query in note.text]

    def edit(self, index, new_text):
        if 0 <= index < len(self.notes):
            self.notes[index].text = new_text

    def delete(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
