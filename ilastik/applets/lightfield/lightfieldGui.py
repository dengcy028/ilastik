'''
Created on Oct 14, 2012

@author: fredo
'''
from ilastik.applets.layerViewer.layerViewerGui import LayerViewerGui
from PyQt4 import uic
import os
useVTK = True
import numpy as np
import logging
import pickle

try:
    from volumina.view3d.view3d import OverviewScene
except:
    print "Warning: could not import optional dependency VTK"
    useVTK = False

class LightfieldGui(LayerViewerGui):
    
    APPLET_DRAWER_PATH = os.path.join(os.path.dirname(__file__),"drawerNew.ui")
    logger = logging.getLogger(__name__)
    
    def __init__(self, toplevelOperator):
        super(LightfieldGui,self).__init__(toplevelOperator)
        #=======================================================================
        # rearrange views
        #=======================================================================
#        x_slicing_view = self.volumeEditorWidget.quadview.splitHorizontal1.widget(1)
#        y_slicing_view = self.volumeEditorWidget.quadview.splitHorizontal2.widget(0)
#        z_slicing_view = self.volumeEditorWidget.quadview.splitHorizontal1.widget(0)
#        view_3d = self.volumeEditorWidget.quadview.splitHorizontal2.widget(1)
#        
#        self.volumeEditorWidget.quadview.splitHorizontal1.addWidget(x_slicing_view)
#        self.volumeEditorWidget.quadview.splitHorizontal1.addWidget(y_slicing_view)
#        self.volumeEditorWidget.quadview.splitHorizontal1.addWidget(z_slicing_view)
#        self.volumeEditorWidget.quadview.splitHorizontal2.addWidget(view_3d)
        self.topLevelOperator = toplevelOperator
        self.initDrawers()
        self.dataSelectionOperator = None
        
        
    def initDrawers(self):
        self._drawers = uic.loadUi(self.APPLET_DRAWER_PATH)
        self._drawers.editDepthSubmit.clicked.connect(self.editDepth)
        
    def appletDrawer(self):
#        return [("Lightfield View", self._drawers )]
        return self._drawers
    
    def editDepth(self):
        inner = self._drawers.editDepthInner.value()
        outer = self._drawers.editDepthOuter.value()
#        self.operation = "pass"
#        self.options = {}
#        self.logger.info("Calculating depth")
#        depth = operations.depth(self.dataSelectionOperator.outputs["Image"][:].allocate().wait(),inner,outer)
#        depth.dirty = True
        self.topLevelOperator.innerScale.setValue(inner)
        self.topLevelOperator.outerScale.setValue(outer)
    
    @property
    def operation(self):
        pass
    
    @operation.setter
    def operation(self,value):
        self.topLevelOperator.Operation.setValue(value)
    
    @property
    def options(self):
        pass
    
    @options.setter
    def options(self,value):
        self.topLevelOperator.Options.setValue(value)

    
#    def setupLayers(self ):
#        self.logger.info("setupLayers called")
#        slotNames = ["InputImage, outerScale, innerScale, Output"]
#        layers = []
#        for slot, name in zip(self.observedSlots, slotNames):
#            if slot.ready() and slot.meta.axistags is not None:
#                layer = self.createStandardLayerFromSlot(slot)
#                layer.name = name 
#                layers.append(layer)
#        return layers

#        # Show the thresholded data
#        outputImageSlot = self.topLevelOperator.Output[ currentImageIndex ]
#        if outputImageSlot.ready():
#            outputLayer = self.createStandardLayerFromSlot( outputImageSlot )
#            outputLayer.name = "min <= x <= max"
#            outputLayer.visible = True
#            outputLayer.opacity = 0.75
#            layers.append(outputLayer)
        
#        # Show the  data
#        invertedOutputSlot = self.topLevelOperator.InvertedOutput[ currentImageIndex ]
#        if invertedOutputSlot.ready():
#            invertedLayer = self.createStandardLayerFromSlot( invertedOutputSlot )
#            invertedLayer.name = "(x < min) U (x > max)"
#            invertedLayer.visible = True
#            invertedLayer.opacity = 0.25
#            layers.append(invertedLayer)
        
        # Show the raw input data
#        inputImageSlot = self.topLevelOperator.InputImage[ currentImageIndex ]
#        if inputImageSlot.ready():
#            inputLayer = self.createStandardLayerFromSlot( inputImageSlot )
#            inputLayer.name = "Raw Input"
#            inputLayer.visible = True
#            inputLayer.opacity = 1.0
#            layers.append(inputLayer)
#
#        return layers
    
        