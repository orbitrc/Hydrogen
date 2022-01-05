PNG = png/x1/arrow.png \
	png/x1.5/arrow.png \
	png/x2/arrow.png \
	png/x1/closedhand.png \
	png/x1.5/closedhand.png \
	png/x2/closedhand.png \
	png/x1/context_menu.png \
	png/x1.5/context_menu.png \
	png/x2/context_menu.png \
	png/x1/copy.png \
	png/x1.5/copy.png \
	png/x2/copy.png \
	png/x1/cross.png \
	png/x1.5/cross.png \
	png/x2/cross.png \
	png/x1/crossed_circle.png \
	png/x1.5/crossed_circle.png \
	png/x2/crossed_circle.png \
	png/x1/forbidden.png \
	png/x1.5/forbidden.png \
	png/x2/forbidden.png \
	png/x1/help.png \
	png/x1.5/help.png \
	png/x2/help.png \
	png/x1/link.png \
	png/x1.5/link.png \
	png/x2/link.png \
	png/x1/openhand.png \
	png/x1.5/openhand.png \
	png/x2/openhand.png \
	png/x1/pointer.png \
	png/x1.5/pointer.png \
	png/x2/pointer.png \
	png/x1/size_all.png \
	png/x1.5/size_all.png \
	png/x2/size_all.png \
	png/x1/size_bdiag.png \
	png/x1.5/size_bdiag.png \
	png/x2/size_bdiag.png \
	png/x1/size_fdiag.png \
	png/x1.5/size_fdiag.png \
	png/x2/size_fdiag.png \
	png/x1/size_hor.png \
	png/x1.5/size_hor.png \
	png/x2/size_hor.png \
	png/x1/size_ver.png \
	png/x1.5/size_ver.png \
	png/x2/size_ver.png \
	png/x1/split_hor.png \
	png/x1.5/split_hor.png \
	png/x2/split_hor.png \
	png/x1/split_ver.png \
	png/x1.5/split_ver.png \
	png/x2/split_ver.png

CONFIG = $(wildcard src/config/*.cursor)

default: $(PNG)
	mkdir -p Hydrogen/cursors
	$(foreach name,$(CONFIG), \
		make Hydrogen/cursors/`basename -s .cursor $(name)`;)
	cp index.theme Hydrogen/index.theme

Hydrogen/cursors/%: src/config/%.cursor
	xcursorgen $^ $@

png/x1/%.png: src/%.svg
	mkdir -p png/x1
	inkscape --export-filename=$@ $<

png/x1.5/%.png: src/%.svg
	mkdir -p png/x1.5
	inkscape --export-filename=$@ --export-width=36 --export-height=36 $<

png/x2/%.png: src/%.svg
	mkdir -p png/x2
	inkscape --export-filename=$@ --export-width=48 --export-height=48 $<

clean:
	rm -r png
