import os

from PyQt5.QtCore import (QEvent, QPoint, QRect, QRectF, QSize, Qt, QUrl, pyqtProperty, pyqtSignal)
from PyQt5.QtGui import (QColor, QDesktopServices, QFont, QFontMetrics, QIcon, QPainter, QPixmap, QTextOption)
from PyQt5.QtWidgets import (QAction, QApplication, QFrame, QHBoxLayout, QHeaderView, QLayout, QLineEdit, QListWidget,
                             QListWidgetItem, QProxyStyle, QPushButton, QRadioButton, QSizePolicy, QSpacerItem, QStyle,
                             QStyledItemDelegate, QStyleOptionButton, QStyleOptionViewItem, QTableWidget,
                             QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

from components.common.common_enums import Align


class ElTableItemDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self._style = None
        self.item_loc = None
        self.row_index = None
        self.column_index = None

    def setStyle(self, _style: dict):
        self._style = _style

    def setItemLoc(self, item_loc: tuple):
        self.item_loc = item_loc

    def setRowIndex(self, row_index: int):
        self.row_index = row_index

    def setColumnIndex(self, column_index: int):
        self.column_index = column_index

    def parseStyle(self):
        # 解析样式
        self.bg_color = self._style.get("background-color", "transparent")
        self.color = self._style.get("color", "black")
        self.font_size = self._style.get("font-size", "14px")
        self.font_weight = self._style.get("font-weight", "normal")
        self.font_family = self._style.get("font-family", "Microsoft YaHei")
        self.text_align = self._style.get("text-align", "left")
        self.padding_left = self._style.get("padding-left", "8px")
        self.padding_right = self._style.get("padding-right", "0px")

        if self.font_weight == "normal":
            self.font_weight = QFont.Normal
        elif self.font_weight == "bold":
            self.font_weight = QFont.Bold
        else:
            self.font_weight = QFont.Normal

        if self.text_align == "left":
            self.text_align = Qt.AlignLeft
        elif self.text_align == "center":
            self.text_align = Qt.AlignCenter
        elif self.text_align == "right":
            self.text_align = Qt.AlignRight
        else:
            self.text_align = Qt.AlignLeft

    def paint(self, painter, option, index):
        self.parseStyle()
        # 重写绘制函数
        if self._style:  # 如果有样式，就按照样式绘制
            # view_item_option = QStyleOptionViewItem(option)
            # self.initStyleOption(view_item_option, index)

            # 在这里设置字体样式
            font = QFont(self.font_family, int(self.font_size[:-2]), self.font_weight)
            # 定义一个矩形，用于绘制文本
            text_rect = (option.rect.left() + int(self.padding_left[:-2]), 
                        option.rect.top(),
                        option.rect.width() - int(self.padding_left[:-2]) - int(self.padding_right[:-2]),
                        option.rect.height()
                    )
            text_rect = QRect(*text_rect)
            painter.setFont(font)

            if self.row_index == index.row():  # 如果指定了行号，就整行绘制样式
                painter.fillRect(option.rect, QColor(self.bg_color))
                painter.setPen(QColor(self._style["color"]))
                option.rect = text_rect
                painter.drawText(option.rect, self.text_align | Qt.AlignVCenter, index.data())
            elif self.column_index == index.column():  # 如果指定了列号，就整列绘制样式
                painter.fillRect(option.rect, QColor(self.bg_color))
                painter.setPen(QColor(self._style["color"]))
                option.rect = text_rect
                painter.drawText(option.rect, self.text_align | Qt.AlignVCenter, index.data())
            elif self.item_loc == (index.row(), index.column()):  # 如果指定了单元格，就绘制单元格样式
                painter.fillRect(option.rect, QColor(self.bg_color))
                painter.setPen(QColor(self._style["color"]))
                option.rect = text_rect
                painter.drawText(option.rect, self.text_align | Qt.AlignVCenter, index.data())
            else:
                # 否则按照默认样式绘制
                super().paint(painter, option, index)
        else:
            # 否则按照默认样式绘制
            super().paint(painter, option, index)
