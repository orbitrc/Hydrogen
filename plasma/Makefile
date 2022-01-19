DESKTOP_DIR=io.orbitrc.hydrogen.desktop

install:
	if [ -d "$(DESTDIR)/usr/share/plasma/look-and-feel/$(DESKTOP_DIR)" ]; then \
		rm -r $(DESTDIR)/usr/share/plasma/look-and-feel/$(DESKTOP_DIR); \
	fi
	cp -r look-and-feel/$(DESKTOP_DIR) $(DESTDIR)/usr/share/plasma/look-and-feel/
