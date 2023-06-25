
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QColor, QFontMetrics, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QPushButton, QStyle, QWidget

from .common.common_enums import Size, Type


class ElBaseButton(QPushButton):
    """ push button """

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.isHovered = False
        self.isPressed = False
        self.hasIcon = False
        self.isDarkMode = False

    def mousePressEvent(self, e):
        self.isPressed = True
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        self.isPressed = False
        super().mouseReleaseEvent(e)

    def enterEvent(self, e):
        self.isHover = True
        self.update()

    def leaveEvent(self, e):
        self.isHover = False
        self.update()

    def getFontHeight(self):
        fm = QFontMetrics(self.font())
        return fm.height()

    def getFontWidth(self):
        fm = QFontMetrics(self.font())
        return fm.width(self.text())

    def getMargin(self):
        margin = self.style().pixelMetric(QStyle.PM_ButtonMargin, None, self)
        return margin

    def getPaddings(self):
        if self.property("size_") == Size.DEFAULT.value:
            return 8, 15
        elif self.property("size_") == Size.LARGE.value:
            return 12, 20
        elif self.property("size_") == Size.SMALL.value:
            return 4, 7


class ElButton(ElBaseButton):

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.is_round = False
        self.is_plain = False
        self.is_disabled = False
        self.is_circle = False

        self.setType(Type.DEFAULT)
        self.setSize(Size.DEFAULT)

    def setType(self, btntype: Type):
        if isinstance(btntype, Type):
            self.type = btntype
            if self.type == Type.DEFAULT:
                self.setProperty("type", btntype.value)
                self.style().polish(self)
            elif self.type == Type.PRIMARY:
                self.setProperty("type", btntype.value)
                self.style().polish(self)
            elif self.type == Type.SUCCESS:
                self.setProperty("type", btntype.value)
                self.style().polish(self)
            elif self.type == Type.WARNING:
                self.setProperty("type", btntype.value)
                self.style().polish(self)
            elif self.type == Type.DANGER:
                self.setProperty("type", btntype.value)
                self.style().polish(self)
            elif self.type == Type.INFO:
                self.setProperty("type", btntype.value)
                self.style().polish(self)
        else:
            raise TypeError("Type must be an instance of Type Enum")

    def setSize(self, btnsize: Size):
        if isinstance(btnsize, Size):
            self.size = btnsize
            if self.size == Size.DEFAULT:
                self.setProperty("size_", btnsize.value)
                self.style().polish(self)
            elif self.size == Size.LARGE:
                self.setProperty("size_", btnsize.value)
                self.style().polish(self)
            elif self.size == Size.SMALL:
                self.setProperty("size_", btnsize.value)
                self.style().polish(self)
        else:
            raise TypeError("Size must be an instance of Size Enum")

    def isRound(self, is_round: bool):
        if isinstance(is_round, bool):
            self.is_round = is_round
            if self.is_round:
                self.setProperty("round", "true")
                fh = self.getFontHeight()
                # print("fh:",fh)
                paddingv = self.getPaddings()[0]
                # print("paddingv:",paddingv)
                radius = (fh + paddingv * 2 + 2) // 2
                # print("radius:",radius)
                self.setStyleSheet(self.styleSheet() + "border-radius: %dpx;" % radius)
                self.style().polish(self)
            else:
                self.setProperty("round", "false")
                self.setStyleSheet(self.styleSheet() + "border-radius: 4px;")
                self.style().polish(self)
        else:
            raise TypeError("is_round must be an instance of bool")

    def isPlain(self, is_plain: bool):
        if isinstance(is_plain, bool):
            self.is_plain = is_plain
            if self.is_plain:
                self.setProperty("plain", "true")
                self.style().polish(self)
            else:
                self.setProperty("plain", "false")
                self.style().polish(self)
        else:
            raise TypeError("is_plain must be an instance of bool")

    def isCircle(self, is_circle: bool):
        if isinstance(is_circle, bool):
            self.is_circle = is_circle
            if self.is_circle:
                self.setProperty("circle", "true")
                icon_size = self.iconSize().width()
                # print(icon_size)
                paddingv = self.getPaddings()[0]
                # print(paddingv)
                radius = (icon_size + paddingv * 2 + 2) // 2
                # print(radius)
                
                self.setStyleSheet(self.styleSheet() + "border-radius: %dpx;" % (radius))
                self.style().polish(self)
            else:
                self.setProperty("circle", "false")
                self.setStyleSheet(self.styleSheet() + "border-radius: 4px;")
                self.style().polish(self)
        else:
            raise TypeError("is_circle must be an instance of bool")

    def setIconColor(self, color: QColor) -> None:
        # create a function that sets the icon color
        # 获取当前的图标
        current_icon = self.icon()

        # 创建一个空白的图片，并将图标绘制在上面
        pixmap = QPixmap(current_icon.actualSize(QSize(64, 64)))
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        current_icon.paint(painter, pixmap.rect(), Qt.AlignCenter)

        # 修改图标的颜色
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)

        painter.end()

        # 创建新的图标
        new_icon = QIcon(pixmap)

        # 设置窗口的新图标
        self.setIcon(new_icon)

    def isDisabled(self, is_disabled: bool):
        if isinstance(is_disabled, bool):
            self.is_disabled = is_disabled
            if self.is_disabled:
                self.setProperty("disabled", "true")
                self.style().polish(self)
            else:
                self.setProperty("disabled", "false")
                self.style().polish(self)
        else:
            raise TypeError("is_disabled must be an instance of bool")
