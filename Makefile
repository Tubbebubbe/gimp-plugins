PLUGINS_DIR := ~/Library/Application\ Support/GIMP/2.8/plug-ins

FILES := export_resized_ios_app_icons.py \
					export_resized_macos_app_icons.py \
					export_resized_ios_assets.py \
					export_resized_android_app_icons.py

help:
	@echo "Targets:" && \
	echo "  install		Install in GIMP plug-ins dir"

install:
	$(foreach src_file, $(FILES), install -v -m 0755 $(src_file) $(PLUGINS_DIR);)
