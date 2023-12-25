import os
from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, DirectoryTree, Label, Input
from textual.containers import Horizontal

STARTDIR = os.path.expanduser("~")

DIRS = [STARTDIR, STARTDIR]

class LeftPanel(Static):
    def compose(self) -> ComposeResult:
        yield Label("This is pre-release software; expect missing features and bugs.")
class FilterBox(Static):
    def compose(self) -> ComposeResult:
        yield Input("Filter...", id="filterBox")
        yield Button("Go", id="goButton")
class DirTrees(Static):
    def compose(self) -> ComposeResult:
        yield Horizontal(DirectoryTree(STARTDIR), DirectoryTree(STARTDIR))
class MainApp(App):
    TITLE = "File Browser"
    '''A file explorer written in Textual.'''
    CSS_PATH = "app.css"
    BINDINGS = [
            # ('/', 'filter', 'Filter'),
            ('?', 'help', 'Help'),
            ('q', 'quit', 'Quit'),
            ]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield LeftPanel()
        yield DirTrees()
    def action_quit(self) -> None:
        self.exit()
    
    def action_filter(self) -> None:
        self.mount(FilterBox())

    def action_help(self) -> None:
        pass

if __name__ == "__main__":
    app = MainApp()
    app.run()
