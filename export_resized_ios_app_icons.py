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

def resize_and_save_image(timg, tdrawable, size, dpi, directory, filename):
    img = timg.duplicate()

    fullpath = os.path.join(directory, filename)

    pdb.gimp_image_merge_visible_layers(img, CLIP_TO_IMAGE)
    pdb.gimp_image_scale(img, size, size)
    pdb.gimp_image_set_resolution(img, dpi, dpi)
    pdb.file_png_save(img, img.layers[0], fullpath, filename, 0, 9, 1, 1, 1, 1, 1)

def plugin_main(img, drawable, directory):
    #
    # List stolen from [https://stackoverflow.com/a/51343786]. Kudos to
    # pilgrim-ivanhoe [https://stackoverflow.com/users/2386045/pilgrim-ivanhoe], and
    # M Jesse [https://stackoverflow.com/users/1025019/m-jesse].
    #

    # // App Icons
    # app-icon@2x.png // iPhone | 60pt x 60pt | actual size: 120px x 120px
    resize_and_save_image(img, drawable, 120, 72, directory, "app-icon@2x.png")
    # app-icon@3x.png // iPhone | 60pt x 60pt | actual size: 180px x 180px
    resize_and_save_image(img, drawable, 180, 72, directory, "app-icon@3x.png")
    # app-icon~ipad.png // iPad | 76pt x 76pt | actual size: 76px x 76px
    resize_and_save_image(img, drawable, 76, 72, directory, "app-icon~ipad.png")
    # app-icon@2x~ipad.png // iPad | 76pt x 76pt | actual size: 152px x 152px
    resize_and_save_image(img, drawable, 152, 72, directory, "app-icon@2x~ipad.png")
    # app-icon-83.5@2x~ipad.png // iPad Pro | 83.5pt x 83.5pt | actual size: 167px x 167px 
    resize_and_save_image(img, drawable, 167, 72, directory, "app-icon-83.5@2x~ipad.png")
     
    # // Notification Icons
    # app-icon-20~ipad.png // iPad | 20pt x 20pt | actual size: 20px x 20px 
    resize_and_save_image(img, drawable, 20, 72, directory, "app-icon-20~ipad.png")
    # app-icon-20@2x~ipad.png // iPad | 20pt x 20pt | actual size: 40px x 40px 
    resize_and_save_image(img, drawable, 40, 72, directory, "app-icon-20@2x~ipad.png")
    # app-icon-20@2x.png // iPhone | 20pt x 20pt | actual size: 40px x 40px 
    resize_and_save_image(img, drawable, 40, 72, directory, "app-icon-20@2x.png")
    # app-icon-20@3x.png // iPhone | 20pt x 20pt | actual size: 60px x 60px 
    resize_and_save_image(img, drawable, 60, 72, directory, "app-icon-20@3x.png")
     
    # // Settings Icons
    # app-icon-29.png // iPhone | 29pt x 29pt | actual size: 29px x 29px     
    resize_and_save_image(img, drawable, 29, 72, directory, "app-icon-29.png")
    # app-icon-29~ipad.png // iPad | 29pt x 29pt | actual size: 29px x 29px 
    resize_and_save_image(img, drawable, 29, 72, directory, "app-icon-29~ipad.png")
    # app-icon-29@2x~ipad.png // iPad | 29pt x 29pt | actual size: 58px x 58px
    resize_and_save_image(img, drawable, 58, 72, directory, "app-icon-29@2x~ipad.png")
    # app-icon-29@2x.png // iPhone | 29pt x 29pt | actual size: 58px x 58px
    resize_and_save_image(img, drawable, 58, 72, directory, "app-icon-29@2x.png")
    # app-icon-29@3x.png // iPhone | 29pt x 29pt | actual size: 87px x 87px
    resize_and_save_image(img, drawable, 87, 72, directory, "app-icon-29@3x.png")
     
    # // Spotlight Icons
    # app-icon-40~ipad.png // iPad | 40pt x 40pt | actual size: 40px x 40px 
    resize_and_save_image(img, drawable, 40, 72, directory, "app-icon-40~ipad.png")
    # app-icon-40@2x~ipad.png // iPad | 40pt x 40pt | actual size: 80px x 80px 
    resize_and_save_image(img, drawable, 80, 72, directory, "app-icon-40@2x~ipad.png")
    # app-icon-40@2x.png // iPhone | 40pt x 40pt | actual size: 80px x 80px 
    resize_and_save_image(img, drawable, 80, 72, directory, "app-icon-40@2x.png")
    # app-icon-40@3x.png // iPhone | 40pt x 40pt | actual size: 120px x 120px 
    resize_and_save_image(img, drawable, 120, 72, directory, "app-icon-40@3x.png")
     
    # // App Store
    # app-icon~ios-marketing.png // 1024pt x 1024pt | actual size: 1024px x 1024px 
    resize_and_save_image(img, drawable, 1024, 72, directory, "app-icon~ios-marketing.png")


    # // CarPlay
    # app-icon@2x~car.png // 60pt x 60pt | actual size: 120px x 120px
    resize_and_save_image(img, drawable, 120, 72, directory, "app-icon@2x~car.png")
    # app-icon@3x~car.png // 60pt x 60pt | actual size: 180px x 180px
    resize_and_save_image(img, drawable, 180, 72, directory, "app-icon@3x~car.png")
     
    # // Apple Watch
    # app_icon~watch-marketing.png // 1024pt x 1024pt | actual size: 1024px x 1024px
    resize_and_save_image(img, drawable, 1024, 72, directory, "app_icon~watch-marketing.png")
 
register(
    "export_resized_ios_app_icons",
    "Exports app icons for all iOS platforms",
    "Exports app icons for all iOS platforms",
    "Techne Development AB",
    "Copyright (c) 2013-2017 Techne Development AB. Released under MIT License.",
    "2017",
    "<Image>/File/Export iOS app icons...",
    "RGB*, GRAY*",
    [
        (PF_DIRNAME, "directory", "Output directory", os.path.expanduser("~")),
        ],
    [],
    plugin_main)

main()
