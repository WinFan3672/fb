import os
import subprocess
import platform
from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, DirectoryTree, Label, Input, Log, TextArea
from textual.containers import Horizontal, Vertical, Middle, Center
from textual.reactive import reactive
from textual.widget import Widget

global SELECTED, CLIPBD, CLIPBD_MODE, TODELETE
SELECTED = ""
STARTDIR = os.path.expanduser("~")
CLIPBD = ""
CLIPBD_MODE = "COPY"
TODELETE = ""
DIRS = [STARTDIR, STARTDIR]

def isUnix():
    return platform.uname()[0] == "Linux"
def find_widget_by_id(root_widget, target_id):
    if root_widget.id == target_id:
        return root_widget
    for child in root_widget.children:
        result = find_widget_by_id(child, target_id)
        if result:
            return result
    return None


class MessageBox(Static):
    def __init__(self, message):
        super().__init__()
        self.message = message
    def compose(self):
        yield Center(Label(self.message), Button("OK", variant="success"))
    def on_button_pressed(self, event):
        self.remove()

class DebugLog(Log):
    id = "debugLog"
    focusable = False
class DirLabel(Label):
    pass
class LeftPanel(Static):
    pass
class WarningBox(Static):
    id = "warnBox"
    def compose(self) -> ComposeResult:
        self.label = Label("This is pre-release software; expect missing features and bugs.")
        yield self.label
class FilterBox(Static):
    def compose(self) -> ComposeResult:
        yield Input("Filter...", id="filterBox")
        yield Button("Go", id="goButton")
class DirTree(DirectoryTree):
    id = "dirTree"
    show_root = reactive(False)
    show_guides = reactive(False)
    def __init__(self, dir, id, root):
        super().__init__(dir)
        self.id=id
        self.mainApp = root
    def on_directory_tree_file_selected(self, message):
        global SELECTED, CLIPBD
        SELECTED = message.path
        self.mainApp.notify("Selected file: {}".format(message.path))
class MainApp(App):
    TITLE = "File Browser"
    '''A file explorer written in Textual.'''
    CSS_PATH = "app.css"
    BINDINGS = [
            # ('/', 'filter', 'Filter'),
            ('o', 'openfile', 'Open File'),
            ('x', 'cut' , 'Cut'),
            ('c', 'copy' , 'Copy'),
            ('v', 'paste' , 'Paste'),
            ('d', 'delete', 'Delete'),
            ('i', 'info', 'File Info'),
            ('n', 'debug', 'Debug Info'),
            ('f1', 'help', 'Help'),
            ('ctrl+s', 'app.screenshot()', 'Screenshot'),
            ('q', 'quit', 'Quit'),
            ]
    def incomplete(self):
        self.notify("This feature has not been added yet.", severity="error")
    def compose(self):
        yield Header()
        yield Footer()
        self.ltDir = DirTree(DIRS[0], "ltDir", self)
        self.rtDir = DirTree(DIRS[1], "rtDir", self)
        yield Vertical(WarningBox(), Horizontal(self.ltDir, self.rtDir))
        self.notify("WARNING: The 'open file' functionality is currently not fully tested on all platforms.", severity="warning", timeout=5)
    def action_openfile(self) -> None:
        if SELECTED:
            if isUnix():
                subprocess.call(["xdg-open", SELECTED])
            else:
                os.startfile(SELECTED)
        else:
            self.notify("ERROR: No file is selected.", severity="error")
    def action_quit(self) -> None:
        self.exit()
    def action_delete(self) -> None:
        self.incomplete()
    def action_info(self) -> None:
        self.incomplete()
    def action_copy(self) -> None:
        if SELECTED:
            CLIPBD = SELECTED
            CLIPBD_MODE = "COPY"
            self.notify("Copied to clipboard: {}".format(CLIPBD))
        else:
            self.notify("Error: No file is selected.", severity="error")
    def action_cut(self) -> None:
        if SELECTED:
            CLIPBD = SELECTED
            CLIPBD_MODE = "CUT"
            self.notify("Cut to clipboard: {}".format(CLIPBD))
        else:
            self.notify("Error: No file is selected.", severity="error")
    def action_paste(self) -> None:
        self.incomplete()
    def action_debug(self) -> None:
        if SELECTED:
            pass
        else:
            self.notify("Error: No file is selected.", severity="error")
    def action_debug(self) -> None:
        self.notify(
            "Selected: {}\nClipboard: {}".format(SELECTED if SELECTED else "None", CLIPBD if CLIPBD else "None"))
    def action_filter(self) -> None:
        self.mount(FilterBox())

    def action_help(self) -> None:
        msg = "\n".join([
            "fb 0.1.0",
            "(c) 2023-2024 WinFan3672, some rights reserved.",
            "Licensed under GNU GPL version 2.0.",
            ])
        self.notify(msg)

if __name__ == "__main__":
    app = MainApp()
    app.run()
