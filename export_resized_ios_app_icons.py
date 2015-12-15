#!/usr/bin/env python
"""

export_resized_ios_app_icons

Gimp plugin to export app icons for an iOS app


Author:
-------
Tobias Blom, Techne Development AB <tobias.blom@techne-dev.se>


Installation:
-------------
(Mac OS X)
Run make:

 > make install

or copy this file to ~/Library/Application Support/GIMP/x.x/plug-ins and
make it executable (chmod 755)


Usage:
------
1. Create your image at a resolution of 1024 x 1024 @ 144 dpi

2. Run the plug-in (from the File menu) and select the output
   directory.

License:
--------
Released under the MIT License

Copyright (c) 2013 Techne Development AB

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from gimpfu import *
import os

def gprint(text):
    pdb.gimp_message(text)
    return 

def resize_and_save_image(timg, tdrawable, size, dpi, dir, filename):
    img = timg.duplicate()

    fullpath = os.path.join(dir, filename)

    pdb.gimp_image_merge_visible_layers(img, CLIP_TO_IMAGE)
    pdb.gimp_image_scale(img, size, size)
    pdb.gimp_image_set_resolution(img, dpi, dpi)
    pdb.file_png_save(img, img.layers[0], fullpath, filename, 0, 9, 1, 1, 1, 1, 1)

def plugin_main(img, drawable, dir):
    resize_and_save_image(img, drawable, 29, 72, dir, "AppIcon-29x29.png")
    resize_and_save_image(img, drawable, 29, 72, dir, "AppIcon_Settings-29x29.png")
    resize_and_save_image(img, drawable, 40, 72, dir, "AppIcon-40x40.png")
    resize_and_save_image(img, drawable, 50, 72, dir, "AppIcon-50x50.png")
    resize_and_save_image(img, drawable, 57, 72, dir, "AppIcon-57x57.png")
    resize_and_save_image(img, drawable, 58, 72, dir, "AppIcon-58x58.png")
    resize_and_save_image(img, drawable, 58, 72, dir, "AppIcon_Settings-58x58.png")
    resize_and_save_image(img, drawable, 72, 72, dir, "AppIcon-72x72.png")
    resize_and_save_image(img, drawable, 76, 72, dir, "AppIcon-76x76.png")
    resize_and_save_image(img, drawable, 80, 72, dir, "AppIcon-80x80.png")
    resize_and_save_image(img, drawable, 80, 72, dir, "AppIcon_Spotlight-80x80.png")
    resize_and_save_image(img, drawable, 87, 72, dir, "AppIcon-87x87.png")
    resize_and_save_image(img, drawable, 100, 72, dir, "AppIcon-100x100.png")
    resize_and_save_image(img, drawable, 114, 72, dir, "AppIcon-114x114.png")
    resize_and_save_image(img, drawable, 120, 72, dir, "AppIcon-120x120.png")
    resize_and_save_image(img, drawable, 152, 72, dir, "AppIcon-152x152.png")
    resize_and_save_image(img, drawable, 167, 72, dir, "AppIcon-167x167.png")
    resize_and_save_image(img, drawable, 180, 72, dir, "AppIcon-180x180.png")

    resize_and_save_image(img, drawable, 512, 72, dir, "iTunesArtwork")

    gprint("Images exported to:\n %s" % (dir))


register(
    "export_resized_ios_app_icons",
    "Exports app icons for all iOS platforms",
    "Exports app icons for all iOS platforms",
    "Techne Development AB",
    "Copyright (c) 2013 Techne Development AB. Released under MIT License.",
    "2013",
    "<Image>/File/Export iOS App Icons...",
    "RGB*, GRAY*",
    [
        (PF_DIRNAME, "dir", "Output directory", os.path.expanduser("~")),
        ],
    [],
    plugin_main)

main()
