default:
	cd cursors ; make

install:
	cd cursors ; make DESTDIR=$(DESTDIR) install
	cd plasma ; make DESTDIR=$(DESTDIR) install
