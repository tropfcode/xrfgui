from model.plotmodel import PlotModel
import enaml
from enaml.qt.qt_application import QtApplication
import logging

with enaml.imports():
    from view.main_window import Main
    
def run():
    app = QtApplication()
    logger = logging.getLogger('program_log')
    fh = logging.FileHandler('program.log')
    logger.addHandler(fh)
    logger.info('Program Started')
    plot = PlotModel()
    gui_run = Main(plot=plot)
    gui_run.show()
    app.start()

if __name__ == '__main__':
    run()