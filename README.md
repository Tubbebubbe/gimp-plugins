gimp-plugins
============

export_resized_ios_images
-------------------------

Exports images at 50% (144 dpi) and 25% (72 dpi) size

<table>
  <tr><th>GIMP image</th><th>Plug-in output</th></tr>
  <tr>
    <td>80 x 80 @ 144 dpi</td>
    <td>Icon 20 x 20 @ 72 dpi<br>Icon 40 x 40 @ 144 dpi</td>
  </tr>
  <tr>
    <td>120 x 120 @ 144 dpi</td>
    <td>Icon 30 x 30 @ 72 dpi<br>Icon 60 x 60 @ 144 dpi</td>
  </tr>
</table>

Released under the MIT License

Installation
============

Copy file to plug-in directory and make executable.

* Mac OS X 10.8.3
* GIMP 2.8.4 from http://gimp.lisanet.de/Website/Download.html

Default directory: ~/Library/Application Support/GIMP/2.8/plug-ins

    > cp export_resized_ios_images.py ~/Library/Application Support/GIMP/2.8/plug-ins
    > chmod 755 ~/Library/Application Support/GIMP/2.8/plug-ins/export_resized_ios_images.py
