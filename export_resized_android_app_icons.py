#!/usr/bin/env python
"""

export_resized_android_app_icons

Gimp plugin to export app icons for an Android app


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

Copyright (c) 2013-2017 Techne Development AB

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
    resize_and_save_image(img, drawable, 192, 72, dir, "ic_launcher-192x192.png")
    resize_and_save_image(img, drawable, 144, 72, dir, "ic_launcher-144x144.png")
    resize_and_save_image(img, drawable, 96, 72, dir, "ic_launcher-96x96.png")
    resize_and_save_image(img, drawable, 72, 72, dir, "ic_launcher-72x72.png")
    resize_and_save_image(img, drawable, 48, 72, dir, "ic_launcher-48x48.png")

    gprint("Images exported to:\n %s" % (dir))


register(
    "export_resized_android_app_icons",
    "Exports app icons for Android apps",
    "Exports app icons for Android apps",
    "Techne Development AB",
    "Copyright (c) 2013-2016 Techne Development AB. Released under MIT License.",
    "2013-2016",
    "<Image>/File/Export Android App Icons...",
    "RGB*, GRAY*",
    [
        (PF_DIRNAME, "dir", "Output directory", os.path.expanduser("~")),
        ],
    [],
    plugin_main)

main()
