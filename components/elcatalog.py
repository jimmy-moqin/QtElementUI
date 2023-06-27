
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QListWidget, QStyledItemDelegate, QWidget


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
            option.rect.setLeft(option.rect.left() - left_offset)
            super().paint(painter, option, index)
        elif level == "2":
            super().paint(painter, option, index)


class ElCatalog(QListWidget):
    '''
    这是一个自定义的目录控件, 用于显示简单的2层目录结构;
    其中level为1的项不可选择,不可点击,为大标题,且字体加粗;
    level为2的项可选择,可点击,为小标题,且字体不加粗;
    如果需要显示更多层次的目录结构,建议使用其他控件.
    '''

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.delegate = LevelDelegate(self)
        self.setItemDelegate(self.delegate)

    def selectionChanged(self, selected, deselected):
        '''
        该函数在切换选项时会被调用, 用于设置选中项的样式
        弥补了在qss中不能对item进行字体设计的缺陷
        '''
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

    def addItem(self, item: str, level="2", first_style=QFont("Microsoft YaHei UI", 14, QFont.Bold)):
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
        else:
            raise ValueError("level must be 1 or 2.")

        self.update()
