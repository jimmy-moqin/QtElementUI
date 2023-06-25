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
        self.first_level_offset = (0, 0, 0, 0)
        self.second_level_offset = (20, 0, 0, 0)
        self.third_level_offset = (40, 0, 0, 0)

        self.item_background_color = QColor(0, 0, 0, 0)
        self.item_border_radius = 5

        self.item_background_offset = (0, 0, 0, 0)

    def paint(self, painter, option, index):
        level = index.data(Qt.UserRole)  # 获取项的level属性值

        if level == "1":
            # 绘制文字
            option.rect.adjust(*self.first_level_offset)
            super().paint(painter, option, index)
        elif level == "2":

            selected = option.state & QStyle.State_Selected
            hovered = option.state & QStyle.State_MouseOver
            if selected:
                # 绘制圆角矩形背景
                painter.setPen(Qt.NoPen)
                painter.setBrush(self.item_background_color)
                painter.drawRoundedRect(option.rect, self.item_border_radius, self.item_border_radius)

            text_rect = option.rect
            text_rect.adjust(*self.second_level_offset)  # 向右偏移20像素
            super().paint(painter, option, index)

        elif level == "3":
            # 在距左侧40像素的位置绘制文字
            option.rect.adjust(*self.third_level_offset)
            super().paint(painter, option, index)
        else:
            # 默认绘制样式
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

    def setItemBackgroundColor(self, color: QColor):
        self.delegate.item_background_color = color

    def setItemBorderRadius(self, num):
        self.delegate.item_border_radius = num

    def setItemBackgroundOffset(self, offset):
        self.delegate.item_background_offset = offset

    def setLevelOffset(self, level, offset):
        if level == "1":
            self.delegate.first_level_offset = offset
        elif level == "2":
            self.delegate.second_level_offset = offset
        elif level == "3":
            self.delegate.third_level_offset = offset
