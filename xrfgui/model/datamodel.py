import numpy as np
import os
from PIL import Image
import logging
from atom.api import Atom, Str, observe, Typed, Dict, List, Int, Enum, Float, Bool

class DataListModel(Atom):
    data_list = List()
    
    def __init__(self):
        self.data_list = []
    
    def add_data(self, path):
        logger = logging.getLogger('program_log')
        try:
            data = Data(np.array(Image.open(path)), path)
            self.data_list.append(data)
        except IOError as e:
            logger.error('I/O error({0}): {1}'.format(e.errno, e.strerror))
            logger.error('Select image file (.jpeg, .tiff, etc.)')
    
    def get_data(self, index=0):
        if len(self.data_list) == 0:
            return
        else:
            return self.data_list[index]
        
        
class Data(Atom):
    raw_data = Typed(np.ndarray)
    plot_data = Typed(np.ndarray)
    file_name = Str()
    
    def __init__(self, raw_data, file_name):
        self.raw_data = raw_data
        self.file_name = file_name
        self.plot_data = np.copy(raw_data)