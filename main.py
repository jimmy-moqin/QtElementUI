import os

uipath = os.path.dirname(os.path.abspath(__file__)) + '/ui/'
os.system("pyuic5 \"" + uipath + "Main_ui.ui\" --import-from=Icons -o \""+ uipath +"Main_ui.py\"")

resousepath = os.path.dirname(os.path.abspath(__file__)) + '/Icons/'
os.system("pyrcc5 \"" + resousepath + "Icons.qrc\" -o \""+ resousepath +"Icons_rc.py\"")

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from src.mainwidget import MainWidgetLogic

if __name__ == '__main__':
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    
    Ui_MainWidgetLogic=MainWidgetLogic()
    Ui_MainWidgetLogic.show()
    sys.exit(app.exec_())
