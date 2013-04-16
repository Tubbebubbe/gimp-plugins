#!/usr/bin/env python
"""

export_resized_ios_images

Gimp plugin to export image to icon files usable on iOS.


Author:
-------
Tobias Blom <tobias@blom.org>


Installation:
-------------
Under Mac OS X, copy this file to ~/Library/GIMP/x.x/plug-ins and
make it executable (chmod 755)


Usage:
------
1. Create your image at a resolution four times what you want on a
   standard iOS device, twice the size on a retina device.
 
      GIMP image             Plug-in output
   -------------------------------------------------
    80 x 80 @ 144 dpi    |  Icon 20 x 20 @ 72 dpi
                         |  Icon 40 x 40 @ 144 dpi
   -------------------------------------------------
    120 x 120 @ 144 dpi  |  Icon 30 x 30 @ 72 dpi
                         |  Icon 60 x 60 @ 144 dpi
   -------------------------------------------------

2. Run the plug-in (from the File menu) and select the output
   directory.

License:
--------
Released under the MIT License

Copyright (c) 2013 Tobias Blom

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

def resize_and_save_image(timg, tdrawable, factor, dpi, fullpath, filename):
    currentWidth = tdrawable.width
    currentHeight = tdrawable.height

    newWidth = float(currentWidth) * float(factor) 
    newHeight = float(currentHeight) * float(factor)

    img = timg.duplicate()

    pdb.gimp_image_merge_visible_layers(img, CLIP_TO_IMAGE)
    pdb.gimp_image_scale(img, newWidth, newHeight)
    pdb.gimp_image_set_resolution(img, dpi, dpi)
    pdb.file_png_save(img, img.layers[0], fullpath, filename, 0, 9, 1, 1, 1, 1, 1)

def plugin_main(img, drawable, dir):
    basename = os.path.basename(img.filename[0:-4])

    filename = basename + ".png"
    fullpath = os.path.join(dir, filename)

    filename_retina = basename + "@2x.png"
    fullpath_retina = os.path.join(dir, filename_retina)
    
    resize_and_save_image(img, drawable, 0.5, 144, fullpath_retina, filename_retina)
    resize_and_save_image(img, drawable, 0.25, 72, fullpath, filename)

    gprint("Images exported to:\n %s\n %s" % (fullpath, fullpath_retina))


register(
    "export_resized_ios_images",
    "Exports images at 50% (144 dpi) and 25% (72 dpi) size",
    "Exports images at 50% (144 dpi) and 25% (72 dpi) size",
    "Tobias Blom",
    "Copyright (c) 2013 Tobias Blom. Released under MIT License.",
    "2013",
    "<Image>/File/Export iOS images...",
    "RGB*, GRAY*",
    [
        (PF_DIRNAME, "dir", "Output directory", os.path.expanduser("~")),
        ],
    [],
    plugin_main)

main()
