#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
""" An example of the `ImageView` widget.

This example shows how a PNG image (in an enaml Image object) can displayed.

<< autodoc-me >>
"""
import os

from enaml.icon import Icon,IconImage
from enaml.image import Image
from enaml.layout.api import vbox, hbox, spacer
from enaml.widgets.api import Window, Container, ComboBox, ImageView,PushButton




def load_icon(path,name):    
    fname = os.path.join(path, '%s.png' % name)
    with open(fname, 'rb') as f:
        data = f.read()
    img = Image(data=data)
    icg = IconImage(image=img)

    return Icon(images=[icg])


def load_icon2(path,normalname,activename):
   
    normalfname = os.path.join(path, '%s.png' % normalname)
     
    activename = os.path.join(path, '%s.png' % activename)


    with open(normalfname, 'rb') as f1:
        data1 = f1.read()
    normalimg = Image(data=data1)
    
    normalicg = IconImage(image=normalimg) 
    normalicg.mode = 'normal'

    with open(activename, 'rb') as f2:
        data2 = f2.read()
    activeimg = Image(data=data2)
    
    activeicg = IconImage(image=activeimg)
    activeicg.mode =  'active'

    return Icon(images=[normalicg,activeicg])




