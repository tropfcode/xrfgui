import numpy as np
import os
from PIL import Image
import logging
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from atom.api import Atom, Str, observe, Typed, Dict, List, Int, Enum, Float, Bool

class PlotModel(Atom):
    data = Typed(np.ndarray)
    fig = Typed(Figure)
    ax = Typed(Axes)
    im = Typed(AxesImage)
    data_logger = logging.getLogger('program_log')
    
    
    def __init__(self):
        self.data = np.zeros((80, 80))
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.im = self.ax.imshow(self.data)
        
    def plot(self, data):
        self.im.set_data(data)
        self.im.set_extent((0, data.shape[1], data.shape[0], 0))
        self.fig.canvas.draw()