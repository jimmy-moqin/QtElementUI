from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

if __name__ == '__main__':
    app = QApplication([])

    # 创建主窗口
    window = QWidget()

    # 创建部件层次结构
    label1 = QLabel("Label 1")
    label2 = QLabel("Label 2")
    label3 = QLabel("Label 3")

    layout = QVBoxLayout()
    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(label3)
    window.setLayout(layout)

    # 设置部件的样式表
    label1.setStyleSheet("background-color: red;")
    label2.setStyleSheet("background-color: green;")
    label3.setStyleSheet("background-color: blue;")

    # 获取部件的背景颜色
    style = label1.style()
    option = style.standardPalette().color(QPalette.Window)
    label1_bg_color = option.name()
    label2_bg_color = option.name()
    label3_bg_color = option.name()

    # 输出背景颜色
    print("Label 1 背景颜色：", label1_bg_color)
    print("Label 2 背景颜色：", label2_bg_color)
    print("Label 3 背景颜色：", label3_bg_color)

    window.show()
    app.exec_()
