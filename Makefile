CC=nuitka3

nuitka:
	$(CC) --onefile main.py --clang --include-data-file=app.css=app.css --remove-output
install:
	install -m 755 main.bin /bin/fb
uninstall:
	-rm /bin/fb
clean:
	-rm main.bin
