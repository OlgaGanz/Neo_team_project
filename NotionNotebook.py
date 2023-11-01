from notion.client import NotionClient
from notion.block import PageBlock, TextBlock

class Note:
    def __init__(self, title, text, tags=[]):
        self.title = title
        self.text = text
        self.tags = tags

    def __str__(self):
        return f"Title: {self.title}\nText: {self.text}\nTags: {', '.join(self.tags)}"


class NotionNotebook:
    def __init__(self, token, page_url):
        self.client = NotionClient(token_v2=token)
        self.page = self.client.get_block(page_url)

    def add_note(self, title, content, tags=[]):
        new_note = self.page.children.add_new(PageBlock, title=title)
        new_content = new_note.children.add_new(TextBlock, title=content)
        if tags:
            new_tags = new_note.children.add_new(TextBlock, title=", ".join(tags))
        return new_note.id

    def get_note(self, note_id):
        return self.client.get_block(note_id)


class Bot:
    def __init__(self, token, page_url):
        self.notebook = NotionNotebook(token, page_url)

    def handle_command(self, command):
        parts = command.split()
        action = parts[0]

        if action == "add-note":
            title = input("Enter title: ")
            content = input("Enter content: ")
            tags = input("Enter tags separated by commas: ").split(",")
            self.notebook.add_note(title, content, tags)
            return "Note added to Notion!"

        # ... [Add other actions like search, edit, delete if needed]

        else:
            return "Invalid command."


def main():
    TOKEN = "YOUR_NOTION_TOKEN"
    PAGE_URL = "URL_OF_YOUR_NOTION_PAGE_WHERE_YOU_WANT_TO_SAVE_NOTES"
    bot = Bot(TOKEN, PAGE_URL)
    
    print("Welcome to the Notion assistant bot!")
    while True:
        command = input("Enter a command: ")
        if command in ["exit", "close"]:
            break
        response = bot.handle_command(command)
        print(response)


if __name__ == "__main__":
    main()
