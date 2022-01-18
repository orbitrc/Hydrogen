DESKTOP_DIR=io.orbitrc.hydrogen.desktop

install:
	if [ -d "/usr/share/plasma/look-and-feel/$(DESKTOP_DIR)" ]; then \
		rm -r /usr/share/plasma/look-and-feel/$(DESKTOP_DIR); \
	fi
	cp -r look-and-feel/$(DESKTOP_DIR) /usr/share/plasma/look-and-feel/
