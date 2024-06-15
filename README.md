# fb
![Screenshot of the app](screenshot.svg)
TUI File browser written using `textual`.
## What is it?
`fb` is a TUI (terminal user interface) program for browsing files. It has two simultaneous panels, an easy-to-use UI, and more.
## Why did you make it?
I couldn't find a similar tool. Most terminal-based tools are far too simple or far too complex, and none of them looked nice or familiar enough to meet my needs. So I decided to make my own. Sorry, `lf` users.
## Why 'fb'?
I noticed that a lot of similar tools ([lf](https://github.com/gokcehan/lf),[nnn](https://github.com/jarun/nnn), etc.) have 2-letter names for simplicity, so I went with `fb` because it stands for 'file browser'. 
## When will it be done?
Here's a to-do list of all features to be implemented by version 1.0:

- [x] Switching directories
- [x] Pasting files
- [x] Deleting files
- [x] Opening files
- [x] Address bar
- [ ] Customisable options/config file
- [ ] Pre-built binaries for releases
    - [x] Linux (x86_64)
    - [ ] Linux (ARM 64-bit)
    - [x] Windows (x86_64)
    - [ ] Windows (ARM 64-bit)
    - [ ] MacOS (ARM 64-bit)
    - [ ] MacOS (x86_64)
- [ ] External Packages
     - [ ] AUR Packages
         - [ ] `fb`
         - [ ] `fb-bin`
         - [ ] `fb-git`
     - [ ] Flatpak
     - [ ] Winget
## Downloading and Installing (Linux)
1. [Go to the latest release](https://codeberg.org/WinFan3672/fb/releases/latest) and download a Linux build. Binaries should be included.
2. Rename it to `fb` and copy it to `/bin` (you will require root permissions to do so).
## Compiling and Installing (Linux)
0. Make sure `clang` and `git` are installed (check with your distro for support);
1. Clone this repo: `git clone https://codeberg.org/WinFan3672/fb`;
2. `cd` into it;
3. Run `pip install -r requirements.txt`;
4. Run `pip install nuitka` to install Nuitka (the compiler);
5. Run `make` to compile;
6. Run `make install` to install your compiled executable.
## Downloading and Installing (Windows)
1. [Go to the latest release](https://codeberg.org/WinFan3672/fb/releases/latest) and download a Windows build;
2. Rename the downloaded file to `fb.exe`.

Currently, there is no way to install `fb`, so you'll need to run `fb.exe` to use it.
## Compiling (Windows)
0. Make sure you have both Visual Studio and Git for Windows installed;
1. Clone the repo: `git clone https://codeberg.org/WinFan3672/fb`;
2. `cd` into it and run `pip install -r requirements.txt` and `pip install nuitka`;
3. Run the `Compile-Windows.bat` script to compile `fb`;
4. Run the `Install-Windows.bat` script **as administrator** to install your newly compiled `fb`.
## Using
To run the installed `fb` from a terminal:

```
$ fb
```
## Contributing
There are several ways you can contribute:
* Report issues. I would love to know if you have any bug reports or suggestions.
* Contribute code. Pull requests are welcome. In fact, I encourage it. If you're new to contributing to projects, definitely give it a try.
* Write documentation. If you enjoy doing that, go for it.
* Provide builds for alternate environments (other Linux architectures, Windows, etc.)
* Spread the word. If you like it, tell all your nerdy friends about it. Maybe they'll like it as well.
