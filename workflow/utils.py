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









#*************************************************************************
#workbench extension point and extensions utils
#*************************************************************************

def get_extensions_of_extensionpoint(workbench,extensionpointid):
    '''
    Given the workbench,and extension point id ,get all the extensions of the
    extension point id.
     
    workbench: the extensions reside on
    
    extensionpointid: the extension point id,eg.'enaml.workbench.ui.workspaces'
    
    '''
    extpoint = workbench.get_extension_point(extensionpointid)
    
    return extpoint.extensions
    
    
def get_worknodes_naviagate_parameters(workbench):
    extp_id = 'enaml.workbench.workflow.worknodes'
    
    extensions = get_extensions_of_extensionpoint(workbench,extp_id)
       
    nav_params =  [() for i in range(len(extensions))]
    
    
    
    for ext in extensions:  
        current_worknode = ext.factory(workbench)
        post =current_worknode.navigate_position
        
        icontule = (current_worknode.navigate_icon_normal,
                    current_worknode.navigate_icon_active)
        
        nav_params[post]= icontule
   
   
    return   nav_params
    
   
    













#************************************************************************
#icons utilities
#************************************************************************

def load_icon(path,name):    
    fname = os.path.join(path, name)
    with open(fname, 'rb') as f:
        data = f.read()
    img = Image(data=data)
    icg = IconImage(image=img)

    return Icon(images=[icg])


def load_icon2(path,normalname,activename):
   
    normalfname = os.path.join(path, normalname)
     
    activename = os.path.join(path, activename)


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




