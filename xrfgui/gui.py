from model.plotmodel import PlotModel
from model.datamodel import DataListModel
import enaml
from enaml.qt.qt_application import QtApplication
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

with enaml.imports():
    from view.main_window import Main

def run():
    app = QtApplication()
    logging.info('Program Started')
    logging.info('testing')
    data_list = DataListModel()
    plot = PlotModel()
    gui_run = Main(plot=plot, data_list=data_list)
    gui_run.show()
    app.start()

if __name__ == '__main__':
    run()