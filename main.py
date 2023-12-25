import os
from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, DirectoryTree, Label
from textual.containers import ScrollableContainer, Horizontal
import sys

STARTDIR = os.path.expanduser("~")

class LeftPanel(Static):
    def compose(self) -> ComposeResult:
        yield Label("This is pre-release software; missing features and bugs may occur.")

class MainApp(App):
    TITLE = "File Browser"
    '''A file explorer written in Textual.'''
    CSS_PATH = "app.css"
    BINDINGS = [
            ('/', 'filter', 'Filter'),
            ('d', 'toggle_dark', 'Dark Mode'),
            ('?', 'help', 'Help'),
            ('q', 'quit', 'Quit'),
            ]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield LeftPanel()
        yield Horizontal(DirectoryTree(STARTDIR), DirectoryTree(STARTDIR))
    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_quit(self) -> None:
        sys.exit()
    
    def action_filter(self) -> None:
        pass

    def action_help(self) -> None:
        pass

if __name__ == "__main__":
    app = MainApp()
    app.run()
