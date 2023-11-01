class Note:
    def __init__(self, title, text, tags=[]):
        self.title = title
        self.text = text
        self.tags = tags

    def __str__(self):
        return f"Title: {self.title}\nText: {self.text}\nTags: {', '.join(self.tags)}"


class Notebook:
    def __init__(self):
        self.notes = []

    def add(self, title, text, tags=[]):
        note = Note(title, text, tags)
        self.notes.append(note)

    def search_by_title(self, query):
        return [note for note in self.notes if query in note.title]

    def search_by_tag(self, tag):
        return [note for note in self.notes if tag in note.tags]

    def edit(self, index, title=None, text=None, tags=None):
        if 0 <= index < len(self.notes):
            if title:
                self.notes[index].title = title
            if text:
                self.notes[index].text = text
            if tags:
                self.notes[index].tags = tags

    def delete(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]


class Bot:
    def __init__(self):
        self.notebook = Notebook()

    def handle_command(self, command):
        parts = command.split()
        action = parts[0]

        if action == "add-note":
            # Usage: add-note title text tag1 tag2 ...
            title = parts[1]
            text = parts[2]
            tags = parts[3:]
            self.notebook.add(title, text, tags)
            return "Note added!"

        elif action == "search-title":
            results = self.notebook.search_by_title(" ".join(parts[1:]))
            return "\n".join(str(note) for note in results)

        elif action == "search-tag":
            results = self.notebook.search_by_tag(" ".join(parts[1:]))
            return "\n".join(str(note) for note in results)

        elif action == "edit-note":
            # Usage: edit-note index title/new_text/tag ...
            index = int(parts[1])
            title = parts[2]
            text = parts[3]
            tags = parts[4:]
            self.notebook.edit(index, title, text, tags)
            return f"Note {index} edited!"

        elif action == "delete-note":
            index = int(parts[1])
            self.notebook.delete(index)
            return f"Note {index} deleted!"

        else:
            return "Invalid command."


def main():
    bot = Bot()
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ")
        if command in ["exit", "close"]:
            break
        response = bot.handle_command(command)
        print(response)


if __name__ == "__main__":
    main()
