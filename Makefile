QUIET := @
PLUGINS_DIR := ~/Library/Application\ Support/GIMP/2.8/plug-ins

help:
	@echo "Targets:" && \
	echo "  install		Install in GIMP plug-ins dir"

install:
	$(QUIET)install -v -m 0755 export_resized_ios_app_icons.py $(PLUGINS_DIR) && \
	install -v -m 0755 export_resized_ios_assets.py $(PLUGINS_DIR)
