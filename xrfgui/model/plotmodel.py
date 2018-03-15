from . import roiselector as roi
import numpy as np
import os
from PIL import Image
import logging
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from matplotlib.colorbar import ColorbarBase
from atom.api import Atom, Str, observe, Typed, Dict, List, Int, Enum, Float, Bool

class PlotModel(Atom):
    data = Typed(np.ndarray)
    fig = Typed(Figure)
    ax = Typed(Axes)
    im = Typed(AxesImage)
    cbar = Typed(ColorbarBase)
    cax = Typed(Axes)
    data_logger = logging.getLogger('program_log')
    
    
    def __init__(self):
        self.data = np.zeros((80, 80))
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.im = self.ax.imshow(self.data)
        self.cax = self.fig.add_axes([.85, .05, .025, .9])
        norm = mpl.colors.Normalize(vmin=np.amin(self.data), vmax=np.amax(self.data))
        self.cbar = ColorbarBase(self.cax, cmap='viridis', norm=norm, orientation='vertical')
        
    def plot(self, data):
        self.cbar.remove()
        vmin = np.amin(data)
        vmax=np.amax(data)
        norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
        self.cax = self.fig.add_axes([.85, .05, .025, .9])
        self.cbar = ColorbarBase(self.cax, cmap='viridis', norm=norm, orientation='vertical')
        self.im.set_data(data)
        self.im.autoscale()
        self.im.set_extent((0, data.shape[1], data.shape[0], 0))
        self.fig.canvas.draw()
        roi.RoiSelector(self.ax, 'rectangle')