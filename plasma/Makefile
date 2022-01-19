DESKTOP_DIR=io.orbitrc.hydrogen.desktop

install: $(DESTDIR)/usr/share/plasma/look-and-feel
	if [ -d "$(DESTDIR)/usr/share/plasma/look-and-feel/$(DESKTOP_DIR)" ]; then \
		rm -r $(DESTDIR)/usr/share/plasma/look-and-feel/$(DESKTOP_DIR); \
	fi
	cp -r look-and-feel/$(DESKTOP_DIR) $(DESTDIR)/usr/share/plasma/look-and-feel/

$(DESTDIR)/usr/share/plasma/look-and-feel:
	mkdir -p $(DESTDIR)/usr/share/plasma/look-and-feel

