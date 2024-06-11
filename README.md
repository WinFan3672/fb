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

- [ ] Switching directories
- [ ] Pasting files
- [ ] Deleting files
- [x] Opening files
- [ ] Address bars for each file tree
- [ ] Backend changes
	- [ ] Ability to check which directory tree (if any) is selected
	- [ ] Message box function
- [ ] More CSS
- [ ] Customisable options/config file
- [ ] Pre-built Binaries
    - [x] Linux (x86_64)
    - [ ] Linux (x86)
    - [ ] Linux (ARM 64-bit)
    - [ ] Linux (ARM 32-bit)
    - [ ] Windows
    - [ ] MacOS (Silicon)
    - [ ] MacOS (Intel)

## Downloading and Installing (Linux)
1. [Go to the latest release](https://codeberg.org/WinFan3672/fb/release/latest) and download a Linux build. Binaries should be included.
2. Rename it to `fb` and copy it to `/bin` (you will require root permissions to do so).
## Compiling and Installing (Linux)
1. Clone this repo: `git clone https://codeberg.org/WinFan3672/fb`
2. `cd` into it
3. Run `pip install -r requirements.txt`
4. Run `make` to compile
5. Run `make install` to install your compiled executable
## Using
If you've installed `fb`, just run it like so:
```
$ fb
```
If you have not, from this repo:
```
$ python main.py
```
## Contributing
There are several ways you can contribute:
* Report issues. I would love to know if you have any bug reports or suggestions.
* Contribute code. Pull requests are welcome. In fact, I encourage it. If you're new to contributing to projects, definitely give it a try.
* Write documentation. If you enjoy doing that, go for it.
* Provide builds for alternate environments (other Linux architectures, Windows, etc.)
* Spread the word. If you like it, tell all your nerdy friends about it. Maybe they'll like it as well.
