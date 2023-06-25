import os

from PyQt5.QtCore import (QPoint, QRectF, QSize, Qt, QUrl, pyqtProperty,
                          pyqtSignal)
from PyQt5.QtGui import (QColor, QDesktopServices, QFont, QFontMetrics, QIcon,
                         QPainter, QPixmap)
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
                             QPushButton, QRadioButton, QSizePolicy, QStyle,
                             QStyleOptionButton, QToolButton, QWidget)

from .common.common_enums import Size, Type


class ElLabel(QLabel):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.is_clickable = False
        self.is_bold = False

    def isBold(self, isBold: bool):
        self.is_bold = isBold
        if isBold:
            font = self.font()
            font.setWeight(QFont.Bold)
            self.setFont(font)
        else:
            font = self.font()
            font.setWeight(QFont.Normal)
            self.setFont(font)
        self.style().polish(self)


