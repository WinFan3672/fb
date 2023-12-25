import os
from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, DirectoryTree, Label, Input
from textual.containers import Horizontal, Vertical, Middle
from textual.reactive import reactive
from textual.widget import Widget

STARTDIR = os.path.expanduser("~")
CLIPBD = None
DIRS = [STARTDIR, STARTDIR]


class MessageBox(Static):
    def __init__(self, message):
        super().__init__()
        self.message = message
    def compose(self):
        yield Middle(Label(self.message), Button("OK", variant="success"))
    def on_button_pressed(self, event):
        self.remove()  # Remove the Middle container (and its children)


class DirLabel(Label):
    pass
class LeftPanel(Static):
    pass
class WarningBox(Static):
    def compose(self) -> ComposeResult:
        yield Label("This is pre-release software; expect missing features and bugs.")
class FilterBox(Static):
    def compose(self) -> ComposeResult:
        yield Input("Filter...", id="filterBox")
        yield Button("Go", id="goButton")
class DirTree(DirectoryTree):
    id = "dirTree"
    show_root = reactive(False)
    show_guides = reactive(False)
    def __init__(self, dir, id):
        super().__init__(dir)
        self.id=id
    def handle_directory_selected(self, message):
        selected_path = message.directory
        print(f"Selected directory: {selected_path}")
class MainApp(App):
    TITLE = "File Browser"
    '''A file explorer written in Textual.'''
    CSS_PATH = "app.css"
    BINDINGS = [
            # ('/', 'filter', 'Filter'),
            ('o', 'open', 'Open File'),
            ('x', 'cut' , 'Cut'),
            ('c', 'copy' , 'Copy'),
            ('v', 'Paste' , 'Paste'),
            ('?', 'help', 'Help'),
            ('q', 'quit', 'Quit'),
            ]
    
    def compose(self):
        yield Header()
        yield Footer()
        yield WarningBox()
        # yield DirTrees()
        self.ltDir = DirTree(DIRS[0], "ltDir")
        self.rtDir = DirTree(DIRS[1], "rtDir")
        yield Horizontal(self.ltDir, self.rtDir)
    def action_quit(self) -> None:
        self.exit()
    
    def action_filter(self) -> None:
        self.mount(FilterBox())

    def action_help(self) -> None:
        msg = "\n".join([
            "TEST",
            ])
        self.mount(MessageBox(msg))

    def action_open(self) -> None:
        pass
if __name__ == "__main__":
    app = MainApp()
    app.run()
