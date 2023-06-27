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
    clicked = pyqtSignal()
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        
        self.is_clickable = False
        self.type = Type.DEFAULT
        self.is_round = False
        self.is_plain = False
        
    def setClickable(self, is_clickable: bool):
        self.is_clickable = is_clickable

    def mousePressEvent(self, event):
        if self.is_clickable:
            self.clicked.emit()
        super().mousePressEvent(event)

    def setPixmapSize(self, size: QSize):
        self.setFixedSize(size)
        self.adjustPixmapSize()

    def adjustPixmapSize(self):
        if self.pixmap():
            scaledPixmap = self.pixmap().scaled(self.size(), aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
            self.setPixmap(scaledPixmap)

    def setType(self,t:Type):
        if t == Type.PRIMARY:
            self.setProperty("type", "primary")
        elif t == Type.SUCCESS:
            self.setProperty("type", "success")
        elif t == Type.WARNING:
            self.setProperty("type", "warning")
        elif t == Type.DANGER:
            self.setProperty("type", "danger")
        elif t == Type.INFO:
            self.setProperty("type", "info")
        elif t == Type.DEFAULT:
            self.setProperty("type", "default")
        self.style().polish(self)

    def isPlain(self, is_plain: bool):
        self.is_plain = is_plain
        if is_plain:
            self.setProperty("plain", "true")
        else:
            self.setProperty("plain", "false")
        self.style().polish(self)
