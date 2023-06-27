import os

from PyQt5.QtCore import (QEvent, QPoint, QRect, QRectF, QSize, Qt, QUrl,
                          pyqtProperty, pyqtSignal)
from PyQt5.QtGui import (QColor, QDesktopServices, QFont, QFontMetrics, QIcon,
                         QPainter, QPixmap, QTextOption)
from PyQt5.QtWidgets import (QAction, QApplication, QFrame, QHBoxLayout,
                             QLayout, QLineEdit, QListWidget, QListWidgetItem,
                             QProxyStyle, QPushButton, QRadioButton,
                             QSizePolicy, QSpacerItem, QStyle,
                             QStyledItemDelegate, QStyleOptionButton,
                             QToolButton, QVBoxLayout, QWidget)

from .common.common_enums import Size, Type
from .ellabel import ElLabel


class ProxyStyle(QProxyStyle):
    '''自定义样式代理类,截获样式,用于修改QLineEdit的清除按钮图标'''

    def __init__(self, style):
        super().__init__(style)
        self.clearIcon = None
        self._changeClearIcon(QIcon(":/System/CircleClose.svg"))

    def standardIcon(self, standardIcon, option=None, widget=None):
        if standardIcon == QStyle.SP_LineEditClearButton:
            return self.clearIcon
        return super().standardIcon(standardIcon, option, widget)

    def _changeClearIcon(self, icon: QIcon):
        self.clearIcon = icon


class ElLineEdit(QLineEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.parent.setProperty("_focus", "false")

    def focusInEvent(self, event) -> None:
        self.parent.setProperty("_focus", "true")
        self.parent.style().polish(self.parent)
        return super().focusInEvent(event)

    def focusOutEvent(self, event) -> None:
        self.parent.setProperty("_focus", "false")
        self.parent.style().polish(self.parent)
        return super().focusOutEvent(event)


class ElInput(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.clearable = False

        self.prefix_icon_setted = False
        self.suffix_icon_setted = False

        self.prefix_widget_setted = False
        self.suffix_widget_setted = False

        # 设置代理样式
        self.proxy_style = ProxyStyle(self.lineEdit.style())
        self.lineEdit.setStyle(self.proxy_style)

    def setupUi(self, parent):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(parent)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.inputContainer = QWidget(parent)
        self.inputContainer.setObjectName(u"inputContainer")
        # sizePolicy.setHeightForWidth(self.inputContainer.sizePolicy().hasHeightForWidth())
        self.inputContainer.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.inputContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.prefix = QWidget(self.inputContainer)
        self.prefix.setObjectName(u"prefix")
        self.prefix.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.horizontalLayout.addWidget(self.prefix)
        self.lineEdit = ElLineEdit(self.inputContainer)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.lineEdit.setPlaceholderText("Please input")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.suffix = QWidget(self.inputContainer)
        self.suffix.setObjectName(u"suffix")
        self.suffix.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.horizontalLayout.addWidget(self.suffix)
        self.verticalLayout.addWidget(self.inputContainer)

    def paintEvent(self, event):
        super().paintEvent(event)

    def setClearable(self, clearable: bool):
        self.clearable = clearable
        if self.clearable:
            self.lineEdit.textChanged.connect(self._onTextChanged)
            self.lineEdit.installEventFilter(self)
        else:
            self.lineEdit.textChanged.disconnect(self._onTextChanged)
            self.lineEdit.removeEventFilter(self)

    def _onTextChanged(self, text: str):
        if text:
            self.lineEdit.setClearButtonEnabled(True)
        else:
            self.lineEdit.setClearButtonEnabled(False)

    def changeClearIcon(self, icon: QIcon):
        '''继承代理类的设置函数,暴露给外部修改清除按钮图标'''
        self.proxy_style._changeClearIcon(icon)

    def setPrefixIcon(self, pixmap: QPixmap, size=QSize(16, 16)):
        if self.prefix_widget_setted:
            raise Exception("prefix widget has been setted,can't set prefix icon.")
        else:
            if self.prefix_icon_setted:
                self.prefixIconLabel.setPixmap(pixmap)
                self.prefixIconLabel.setPixmapSize(size)
            else:
                self.prefixIconLabel = ElLabel()
                self.prefixIconLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.prefixIconLabel.setPixmap(pixmap)
                self.prefixIconLabel.setPixmapSize(size)
                self.prefixIconLabel.setObjectName("prefixIcon")
                # add
                prefix_layout = QHBoxLayout(self.prefix)
                prefix_layout.setContentsMargins(0, 0, 0, 0)
                prefix_layout.addWidget(self.prefixIconLabel)
                self.prefix_icon_setted = True

    def setSuffixIcon(self, pixmap: QPixmap, size=QSize(16, 16)):
        if self.suffix_widget_setted:
            raise Exception("suffix widget has been setted,can't set suffix icon.")
        else:
            if self.suffix_icon_setted:
                self.suffixIconLabel.setPixmap(pixmap)
                self.suffixIconLabel.setPixmapSize(size)
            else:
                self.suffixIconLabel = ElLabel()
                self.suffixIconLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.suffixIconLabel.setPixmap(pixmap)
                self.suffixIconLabel.setPixmapSize(size)
                self.suffixIconLabel.setObjectName("suffixIcon")
                # add
                suffix_layout = QHBoxLayout(self.suffix)
                suffix_layout.setContentsMargins(0, 0, 0, 0)
                suffix_layout.addWidget(self.suffixIconLabel)
                self.suffix_icon_setted = True

    def setPrefixWidget(self, widget):
        if self.prefix_icon_setted:
            raise Exception("prefix icon has been setted,can't set prefix widget.")
        else:
            if self.prefix_widget_setted:
                self.prefix_layout.findChild(QWidget).deleteLater()
            else:
                pass
            self.prefix_layout = QVBoxLayout(self.prefix)
            self.prefix_layout.setContentsMargins(0, 0, 0, 0)
            self.prefix_layout.addItem(QSpacerItem(0, 2, QSizePolicy.Expanding, QSizePolicy.Minimum))
            widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

            self.sub_widget = QWidget()
            self.sub_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
            self.sub_layout = QHBoxLayout(self.sub_widget)
            self.sub_layout.setContentsMargins(0, 0, 0, 0)
            self.sub_layout.addItem(QSpacerItem(2, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
            self.sub_layout.addWidget(widget)
            self.sub_layout.addItem(QSpacerItem(2, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
            self.prefix_layout.addWidget(self.sub_widget)

            self.prefix_layout.addItem(QSpacerItem(0, 2, QSizePolicy.Expanding, QSizePolicy.Minimum))
            self.prefix_widget_setted = True

    def setPrefixWidth(self, w: int):
        self.prefix.setMaximumWidth(w)

    def setSuffixWidget(self, widget):
        if self.suffix_icon_setted:
            raise Exception("suffix icon has been setted,can't set suffix widget.")
        else:
            if self.suffix_widget_setted:
                self.suffix_layout.findChild(QWidget).deleteLater()
            else:
                pass
            self.suffix_layout = QVBoxLayout(self.suffix)
            self.suffix_layout.setContentsMargins(0, 0, 0, 0)
            self.suffix_layout.addItem(QSpacerItem(0, 2, QSizePolicy.Expanding, QSizePolicy.Minimum))
            widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

            self.sub_widget = QWidget()
            self.sub_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
            self.sub_layout = QHBoxLayout(self.sub_widget)
            self.sub_layout.setContentsMargins(0, 0, 0, 0)
            self.sub_layout.addItem(QSpacerItem(2, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
            self.sub_layout.addWidget(widget)
            self.sub_layout.addItem(QSpacerItem(2, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
            self.suffix_layout.addWidget(self.sub_widget)

            self.suffix_layout.addItem(QSpacerItem(0, 2, QSizePolicy.Expanding, QSizePolicy.Minimum))
            self.suffix_widget_setted = True

    def setSuffixWidth(self, w: int):
        self.suffix.setMaximumWidth(w)
