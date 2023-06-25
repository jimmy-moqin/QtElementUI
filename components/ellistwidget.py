import os

from PyQt5.QtCore import (QPoint, QRectF, QSize, Qt, QUrl, pyqtProperty,
                          pyqtSignal)
from PyQt5.QtGui import (QColor, QDesktopServices, QFont, QFontMetrics, QIcon,
                         QPainter, QPixmap)
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QListWidget,
                             QListWidgetItem, QPushButton, QRadioButton,
                             QSizePolicy, QStyle, QStyledItemDelegate,
                             QStyleOptionButton, QToolButton, QWidget)

from .common.common_enums import Size, Type
from .ellabel import ElLabel


class LevelDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        

    def paint(self, painter, option, index):
        # 转换到父控件坐标系,获取项的左边距
        left_offset = self.parent.mapToParent(option.rect.topLeft()).x()

        level = index.data(Qt.UserRole)  # 获取项的level属性值
        
        if level == "1":
            # 绘制文字,左边距减去偏移量,从而保证level为1的项的文字顶格
            # 而level为2和3的项的文字会缩进padding的距离，而且background-color不会缩进
            option.rect.setLeft(option.rect.left()-left_offset)
            super().paint(painter, option, index)
        elif level == "2":
            super().paint(painter, option, index)

        elif level == "3":
            super().paint(painter, option, index)


class ElListWidget(QListWidget):

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.delegate = LevelDelegate(self)
        self.setItemDelegate(self.delegate)

    def selectionChanged(self, selected, deselected):
        super().selectionChanged(selected, deselected)

        # 恢复之前选中项的样式
        deselected_items = deselected.indexes()
        for index in deselected_items:
            item = self.itemFromIndex(index)
            if item:
                font = item.font()
                font.setWeight(QFont.Normal)
                item.setFont(font)

        # 设置当前选中项的样式
        selected_items = selected.indexes()
        for index in selected_items:
            item = self.itemFromIndex(index)
            if item:
                font = item.font()
                font.setWeight(QFont.Bold)
                item.setFont(font)

        self.update()

    def addItem(self, item:str, level="2", first_style=QFont("Microsoft YaHei UI", 16, QFont.Normal)):
        super().addItem(item)
        item_count = self.count()
        last_item = self.item(item_count - 1)

        # 设置自定义属性--level选项级别
        last_item.setData(Qt.UserRole, level)

        if level == "1":
            # 设置不可选择，不可点击，不可编辑，不可悬浮
            last_item.setFlags(Qt.NoItemFlags)
            # 设置字体
            last_item.setFont(first_style)
        elif level == "2":
            pass
        elif level == "3":
            pass

        self.update()

    