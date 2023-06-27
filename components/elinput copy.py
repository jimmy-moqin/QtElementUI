import os

from PyQt5.QtCore import (QEvent, QPoint, QRect, QRectF, QSize, Qt, QUrl,
                          pyqtProperty, pyqtSignal)
from PyQt5.QtGui import (QColor, QDesktopServices, QFont, QFontMetrics, QIcon,
                         QPainter, QPixmap, QTextOption)
from PyQt5.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLayout,
                             QListWidget, QListWidgetItem, QPushButton,
                             QRadioButton, QSizePolicy, QSpacerItem, QStyle,
                             QStyledItemDelegate, QStyleOptionButton,
                             QTextEdit, QToolButton, QVBoxLayout, QWidget)

from .common.common_enums import Size, Type
from .ellabel import ElLabel


class ElInput(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.is_textarea = False
        self.scroll_enabled = False

    def setupUi(self, parent):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.verticalLayout_2 = QVBoxLayout(parent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(parent)
        self.widget_2.setObjectName(u"widget_2")
        # sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.prefix = QWidget(self.widget_2)
        self.prefix.setObjectName(u"prefix")

        self.horizontalLayout.addWidget(self.prefix)

        self.textContainer = QWidget(self.widget_2)
        self.textContainer.setObjectName(u"textContainer")
        sizePolicy.setHeightForWidth(self.textContainer.sizePolicy().hasHeightForWidth())
        self.textContainer.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.textContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.textEdit = QTextEdit(self.textContainer)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit.setPlaceholderText("Please input...")

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.textContainer)

        self.suffix = QWidget(self.widget_2)
        self.suffix.setObjectName(u"suffix")

        self.horizontalLayout.addWidget(self.suffix)


        self.verticalLayout_2.addWidget(self.widget_2)
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.widget_2 = QWidget(parent)
        # self.widget_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.widget_2.setObjectName(u"widget_2")
        # self.horizontalLayout = QHBoxLayout(self.widget_2)
        # self.horizontalLayout.setSpacing(0)
        # self.horizontalLayout.setObjectName(u"horizontalLayout")
        # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # self.prefix = QWidget(self.widget_2)
        # self.prefix.setObjectName(u"prefix")

        # self.horizontalLayout.addWidget(self.prefix)

        # self.textContainer = QWidget(self.widget_2)
        # self.textContainer.setObjectName(u"textContainer")
        # self.verticalLayout = QVBoxLayout(self.textContainer)
        # self.verticalLayout.setSpacing(0)
        # self.verticalLayout.setObjectName(u"verticalLayout")
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # # 设置大小策略
        # self.textContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # self.verticalLayout.addItem(self.verticalSpacer_2)

        # self.textEdit = QTextEdit(self.textContainer)
        # self.textEdit.setObjectName(u"textEdit")
        # self.textEdit.setFrameShape(QFrame.NoFrame)
        # self.textEdit.setFrameShadow(QFrame.Plain)
        # self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        # self.textEdit.setPlaceholderText("Please input...")
        # self.textEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # self.verticalLayout.addWidget(self.textEdit)

        # self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # self.verticalLayout.addItem(self.verticalSpacer)

        # self.horizontalLayout.addWidget(self.textContainer)

        # self.suffix = QWidget(self.widget_2)
        # self.suffix.setObjectName(u"suffix")

        # self.horizontalLayout.addWidget(self.suffix)

    def paintEvent(self, event):
        super().paintEvent(event)
        height = self.height()  # 根据需要进行调整
        self.widget_2.setMinimumHeight(height)
        self.widget_2.setMaximumHeight(height)
        font_height = self.textEdit.fontMetrics().height()
        # font_size = self.textEdit.font().pointSize()
        self.textEdit.setMinimumHeight(font_height + 10)
        self.textEdit.setMaximumHeight(font_height + 10)

            
        
            




