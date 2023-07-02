import os

from PyQt5.QtCore import (QEvent, QPoint, QRect, QRectF, QSize, Qt, QUrl,
                          pyqtProperty, pyqtSignal)
from PyQt5.QtGui import (QColor, QDesktopServices, QFont, QFontMetrics, QIcon,
                         QPainter, QPixmap, QTextOption)
from PyQt5.QtWidgets import (QAction, QApplication, QFrame, QHBoxLayout,
                             QHeaderView, QLayout, QLineEdit, QListWidget,
                             QListWidgetItem, QProxyStyle, QPushButton,
                             QRadioButton, QSizePolicy, QSpacerItem, QStyle,
                             QStyledItemDelegate, QStyleOptionButton,
                             QStyleOptionViewItem, QTableWidget,
                             QTableWidgetItem, QToolButton, QVBoxLayout,
                             QWidget)

from .common.common_enums import Align
from .ellabel import ElLabel

# 定义一个设置item的委托，用于绘制不同样式的单元格

class ElTable(QTableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.line_num = False  # 是否开启行号
        self.stripe = False  # 是否开启斑马纹
        self.h_expand = True  # 是否开启水平拉伸
        self.header_align = Align.LEFT  # 表头对齐方式
        self.clear_selcet_out_focus = True  # 是否在失去焦点时清除选中
        self.bordered = False  # 是否显示垂直边框

        self.setSelectionBehavior(QTableWidget.SelectRows)  # 设置整行选中

        self.setLineNum(self.line_num)
        self.setStripe(self.stripe)
        self.setHExpand(self.h_expand)
        self.setHeaderAlign(self.header_align)
        self.setBorder(self.bordered)

    # # 定义一个委托，用于绘制不同样式的单元格
    # def openCustomStyle(self,):
    #     '''开启自定义样式,实际上是设置一个委托'''
    #     self.item_delegate = ElTableItemDelegate(self)
    #     self.setItemDelegate(self.item_delegate)

    def paintEvent(self, event) -> None:
        # 当表格没有数据时，切换样式表，默认显示三行
        if self.rowCount() == 0:
            self.setProperty("none", True)
            self.style().polish(self)
        else:
            self.setProperty("none", False)
            self.style().polish(self)

        return super().paintEvent(event)

    def focusOutEvent(self, event):
        if self.clear_selcet_out_focus:
            self.clearSelection()
        return super().focusOutEvent(event)

    def setLineNum(self, line_num: bool):
        self.line_num = line_num
        if self.line_num:
            # 是否开启行号
            self.verticalHeader().setVisible(True)
            self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
            self.verticalHeader().setDefaultSectionSize(30)
        else:
            self.verticalHeader().setVisible(False)

    def setStripe(self, stripe: bool):
        self.stripe = stripe
        if self.stripe:
            # 是否开启斑马纹
            self.setAlternatingRowColors(True)
        else:
            self.setAlternatingRowColors(False)

    def setHExpand(self, h_expand: bool):
        self.h_expand = h_expand
        if self.h_expand:
            # 是否开启水平拉伸
            self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def setHeaderAlign(self, header_align: Align):
        # 表头对齐方式
        self.header_align = header_align
        if self.header_align == Align.LEFT:
            self.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        elif self.header_align == Align.CENTER:
            self.horizontalHeader().setDefaultAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        elif self.header_align == Align.RIGHT:
            self.horizontalHeader().setDefaultAlignment(Qt.AlignRight | Qt.AlignVCenter)

    def setBorder(self, bordered: bool):
        self.bordered = bordered
        if self.bordered:
            self.setShowGrid(True)
        else:
            self.setShowGrid(False)

    def loadPandasDf(self, df):
        self.setColumnCount(df.shape[1])
        self.setRowCount(df.shape[0])
        self.setHorizontalHeaderLabels(df.columns)
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                self.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setSelectionMode(QTableWidget.SingleSelection)


    def setItemDelegateForCell(self, item, delegate):
        delegate.setItemLoc((item.row(), item.column()))
        return super().setItemDelegate(delegate)
        

    def setItemDelegateForRow(self, row: int, delegate) -> None:
        delegate.setRowIndex(row)
        return super().setItemDelegateForRow(row, delegate)

    def setItemDelegateForColumn(self, column: int, delegate) -> None:
        delegate.setColumnIndex(column)
        return super().setItemDelegateForColumn(column, delegate)

    # def setRowStyle(self, delegate,row, ):
        
    #     # 强制重绘
        

    def setColumnStyle(self, column, style: dict):
        self.item_delegate.setStyle(style)
        self.item_delegate.setColumnIndex(column)
        # 强制重绘
        self.viewport().update()


    def setItemStyle(self, row, column, style: dict):
        self.item_delegate.setStyle(style)
        self.item_delegate.setItemLoc(row, column)
        # 强制重绘
        self.viewport().update()
