import os
import subprocess
import platform
import hashlib
import pathlib

from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, DirectoryTree, Label, Input, Log, TextArea
from textual.containers import Horizontal, Vertical, Middle, Center
from textual.reactive import reactive
from textual.widget import Widget
from textual.screen import Screen
from textual.binding import Binding

global SELECTED, CLIPBD, CLIPBD_MODE, TODELETE, VERSION, CSS_PATH

SELECTED = ""
CLIPBD = ""
CLIPBD_MODE = "COPY"
TODELETE = ""
VERSION = "0.3.1"

CSS_PATH = "app.css"

class AddressBar(Input):
    def __init__(self, ltDir):
        super().__init__(os.getcwd())
        self.ltDir = ltDir
    def action_submit(self):
        self.ltDir.path = self.value
        self.ltDir.reload()

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

class MessageBox(Screen):
    def __init__(self, message):
        super().__init__()
        self.message = message
    def compose(self):
        yield Static(self.message)
        yield Button("OK", variant="success")
    def on_button_pressed(self, event):
        self.remove()

class DebugLog(Log):
    id = "debugLog"
    focusable = False

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
        self.notify("Selected file: {}".format(SELECTED))
def helpMessage():
    global VERSION
    return "fb {}\n(c) 2023-2024 WinFan3672, some rights reserved.\nLicensed under GNU GPL version 2.0.".format(VERSION)

class MainApp(App):
    global SELECTED, CLIPBD, CLIPBD_MODE, TODELETE
    TITLE = ""
    '''A file explorer written in Textual.'''
    CSS_PATH = CSS_PATH
    SCREENS = {"aboutBox": MessageBox(helpMessage())}

    CLEARDEL = Binding(action="cancelDelete", description="Cancel Delete", key="f2", show=False)
    CLEARCPIP = Binding(action="clearClipboard", description="Clear Clipboard", key="f3", show=False)
    DESEL = Binding(action="deselect", description="Clear Selection", key="f4", show=False)

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
        CLEARDEL,
        CLEARCPIP,
        DESEL,
        # Binding(action="test", key="t", description="Test", show=False),
    ]


    def incomplete(self):
        self.notify("This feature has not been added yet.", severity="error")


    def compose(self):
        yield Footer()
        self.ltDir = DirTree(os.getcwd(), "ltDir", self)
        self.addr = AddressBar(self.ltDir)
        yield Vertical(self.addr, self.ltDir)

        self.ltDir.focus()
        self.notify("Warning: This is pre-release software. Expect bugs and incomplete features.", severity="warning", timeout=5)
        self.notify("Warning: The 'open file' functionality is currently not fully tested on all platforms.", severity="warning", timeout=5)


    def action_clearClipboard(self):
        global CLIPBD
        if CLIPBD:
            CLIPBD = ""
            self.notify("Cleared clipboard.")
        else:
            self.notify("ERROR: Clipboard is empty.", severity="error")


    def action_cancelDelete(self):
        global TODELETE
        if TODELETE:
            TODELETE = ""
            self.notify("Delete operation canceled.")
        else:
            self.notify("ERROR: No operation to cancel.", severity="error")


    def action_openfile(self) -> None:
        if SELECTED:
            if os.name == "posix":
                self.incomplete()
            else:
                os.startfile(SELECTED)
        else:
            self.notify("ERROR: No file is selected.", severity="error")


    def action_quit(self) -> None:
        self.exit()


    def action_delete(self) -> None:
        global TODELETE
        if TODELETE == "" and SELECTED:
            TODELETE = SELECTED
            self.notify("Are you sure you want to delete '{}'?\nD: Confirm\nF2: Cancel".format(SELECTED), severity="warning", timeout=8)
        elif not SELECTED:
            self.notify("ERROR: No file is selected.", severity="error")
        else:
            try:
                os.remove(SELECTED)
                self.notify("Successfully deleted file.")
            except:
                self.notify("ERROR: Failed to delete file!", severity="error")
            self.action_refresh()


    def action_deselect(self):
        global SELECTED
        if SELECTED:
            SELECTED = ""
            self.notify("Deselected file.")
        else:
            self.notify("ERROR: No file is selected.", severity="error")


    def action_info(self) -> None:
        if SELECTED:
            rawSize = os.path.getsize(SELECTED)
            if rawSize >= 1024**3:
                size = "{} GiB".format(rawSize // 1024**3)
            if rawSize >= 1048576:
                size = "{} MiB".format(rawSize // 1048576)
            elif rawSize >= 1024:
                size = "{} KiB".format(rawSize // 1024)
            else:
                size = "{} B".format(rawSize)

            self.notify("File: {}\nSize: {}".format(SELECTED, size))
        else:
            self.notify("ERROR: No file is selected.", severity="error")


    def action_copy(self) -> None:
        global CLIPBD
        if SELECTED:
            CLIPBD = SELECTED
            CLIPBD_MODE = "COPY"
            self.notify("Copied to clipboard: {}\nF3: Clear Clipboard".format(CLIPBD))
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
        if CLIPBD:
            self.notify("Copying {} to {}...".format(CLIPBD, self.ltDir.path))
            with open(SELECTED, "rb") as f:
                data = f.read()
            if CLIPBD_MODE == "CUT":
                os.remove(CLIPBD)
            with open(os.path.join(self.ltDir.path, os.path.basename(CLIPBD)), "wb") as f:
                f.write(data)
            self.notify("Copied successfully.")
            self.ltDir.reload()
        else:
            self.notify("Cannot paste, clipboard empty", severity="error")


    def action_debug(self) -> None:
        if SELECTED:
            pass
        else:
            self.notify("Error: No file is selected.", severity="error")
    def action_debug(self) -> None:
        self.notify("Selected: {}\nClipboard: {}\nClipboard Mode: {}".format(SELECTED if SELECTED else "None", CLIPBD if CLIPBD else "None", CLIPBD_MODE))


    def action_filter(self) -> None:
        self.mount(FilterBox())


    def action_help(self):
        self.notify(helpMessage())


    def action_refresh(self):
        self.ltDir.reload() 
        self.screen.refresh()

if __name__ == "__main__":
    app = MainApp()
    app.run()
