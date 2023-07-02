import os
import sys

from PyQt5 import QtCore, QtGui

app=QtGui.QApplication(sys.argv)

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self):
        QtCore.QAbstractTableModel.__init__(self)        
        self.items=['One','Two','Three','Four','Five','Six','Seven']

    def rowCount(self, parent=QtCore.QModelIndex()):   
        return len(self.items)
    def columnCount(self, index=QtCore.QModelIndex()):
        return 1

    def data(self, index, role):
        if not index.isValid() or not (0<=index.row()<len(self.items)):
            return QtCore.QVariant()

        item=str(self.items[index.row()])

        if role==QtCore.Qt.UserRole:
            return item
        if role==QtCore.Qt.DisplayRole:
            return item
        if role==QtCore.Qt.TextColorRole:
            return QtCore.QVariant(QtGui.QColor(QtCore.Qt.white))
        if role == QtCore.Qt.BackgroundRole:
            if index.row()%2:
                return QtCore.QVariant(QtGui.QColor("#242424"))
            else:
                return QtCore.QVariant(QtGui.QColor(QtCore.Qt.black))

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if role!=QtCore.Qt.DisplayRole:   return QtCore.QVariant()
        if orientation==QtCore.Qt.Horizontal: return QtCore.QVariant('My Column Name') 

class TableView(QtGui.QTableView):
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)
        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)        

        myModel=TableModel()
        self.setModel(myModel)      

        appStyle="""
        QTableView
        {   
            background-color: black;
            gridline-color:grey;
            color: black;
        }
        QTableView::item 
        {   
            color: white;         
        }
        QTableView::item:hover
        {   
            color: black;
            background: #ffaa00;            
        }
        QTableView::item:focus
        {   
            color: black;
            background: #0063cd;            
        }        
        """
        self.setStyleSheet(appStyle)

view=TableView()
view.show()   
sys.exit(app.exec_())
