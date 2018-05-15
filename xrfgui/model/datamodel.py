import numpy as np
import os
from PIL import Image
import logging
from atom.api import Atom, Str, observe, Typed, Dict, List, Int, Enum, Float, Bool

class DataListModel(Atom):
    data_list = List()
    length = Int()
    
    def __init__(self):
        self.data_list = []
        self.length = 0
    
    def add_data(self, path):
        logger = logging.getLogger('program_log')
        try:
            data = Data(np.array(Image.open(path)), path)
            self.data_list.append(data)
            self.length += 1
            print('SUCCESSFUL IMAGE LOAD', len(self.data_list))
        except:
            logger.error('I/O error')
            print('Select image file (.jpeg, .tiff, etc.)')
    
    def get_data(self, index=0):
        if self.length == 0:
            print('List is empty, must add data')
            return
        else:
            return self.data_list[index]
        
    
        
        
class Data(Atom):
    raw_data = Typed(np.ndarray)
    plot_data = Typed(np.ndarray)
    norm_data = Typed(np.ndarray)
    align_data = Typed(np.ndarray)
    file_name = Str()
    is_norm = Bool()
    is_align = Bool()
    normed = Bool()
    aligned = Bool()
    
    def __init__(self, raw_data, file_name):
        self.raw_data = raw_data
        self.file_name = file_name
        self.plot_data = np.ma.copy(raw_data)
        self.norm_data = np.ma.zeros((4,4))
        self.align_data = np.ma.zeros((4,4))
        self.is_norm = False
        self.is_align = False
        self.normed = False
        self.aligned = False
        
    def add_norm_data(self, path=None, array=None):
        try:
            if path != None:
                norm_data = np.array(Image.open(path))
                self.norm_data = np.ma.masked_where(norm_data <= 0.0, norm_data)
            if array != None:
                self.norm_data = np.ma.masked_where(array<=0.0, array)
        except:
            print('bad path')
    
    def add_align_data(self, path=None, array=None):
        #try:
        if path != None:
            align_data = np.array(Image.open(path))
            self.align_data = np.ma.copy(align_data)
        if isinstance(array) is not None:
            self.align_data = np.ma.copy(array)
        #except:
            print('bad path')