import os

import sass
from components.common.common_enums import Size, Type
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QIcon
from PyQt5.QtWidgets import QWidget
from ui.Main_ui import Ui_MainWidget



class MainWidgetLogic(QWidget, Ui_MainWidget):

    def __init__(self):
        super(MainWidgetLogic, self).__init__()
        self.setupUi(self)
        
        self.initUI()
        self.ElButtonsUI()
        self.ElListUI()
        
    
    def initUI(self):
        # 编译resource\qss\light下的scss文件,把所有文件合并成一个再编译
        files = os.listdir("resource\qss\light")
        self.qss = ""
        for file in files:
            # print(file)
            if file.endswith(".scss"):
                with open("resource\qss\light\\" + file, "r",encoding="utf-8") as f:
                    self.qss += f.read()
        self.qss = sass.compile(string=self.qss)
        self.setStyleSheet(self.qss)
        
    def ElButtonsUI(self):
        # 默认按钮样式的不同Type
        self.DefaultBtn.setType(Type.DEFAULT)
        self.PrimaryBtn.setType(Type.PRIMARY)
        self.SuccessBtn.setType(Type.SUCCESS)
        self.WarningBtn.setType(Type.WARNING)
        self.DangerBtn.setType(Type.DANGER)
        self.InfoBtn.setType(Type.INFO)

        # 朴素按钮样式的不同Type
        self.PlainBtn.isPlain(True)
        self.PlainPrimaryBtn.setType(Type.PRIMARY)
        self.PlainPrimaryBtn.isPlain(True)
        self.PlainSuccessBtn.setType(Type.SUCCESS)
        self.PlainSuccessBtn.isPlain(True)
        self.PlainWarningBtn.setType(Type.WARNING)
        self.PlainWarningBtn.isPlain(True)
        self.PlainDangerBtn.setType(Type.DANGER)
        self.PlainDangerBtn.isPlain(True)
        self.PlainInfoBtn.setType(Type.INFO)
        self.PlainInfoBtn.isPlain(True)

        # 圆角按钮样式的不同Type
        self.RoundDefaultBtn.isRound(True)
        self.RoundPrimaryBtn.setType(Type.PRIMARY)
        self.RoundPrimaryBtn.isRound(True)
        self.RoundSuccessBtn.setType(Type.SUCCESS)
        self.RoundSuccessBtn.isRound(True)
        self.RoundWarningBtn.setType(Type.WARNING)
        self.RoundWarningBtn.isRound(True)
        self.RoundDangerBtn.setType(Type.DANGER)
        self.RoundDangerBtn.isRound(True)
        self.RoundInfoBtn.setType(Type.INFO)
        self.RoundInfoBtn.isRound(True)
        
        # 圆形按钮样式的不同Type和不同图标
        self.CircleIconBtn_1.isCircle(True)
        self.CircleIconBtn_1.setType(Type.DEFAULT)
        self.CircleIconBtn_1.setIcon(QIcon(":/System/plus.svg"))
        self.CircleIconBtn_1.setIconColor(QColor(14,14,14))

        self.CircleIconBtn_2.isCircle(True)
        self.CircleIconBtn_2.setType(Type.PRIMARY)
        self.CircleIconBtn_2.setIcon(QIcon(":/Document/FolderOpened.svg"))
        self.CircleIconBtn_2.setIconColor(QColor(255,255,255))

        self.CircleIconBtn_3.isCircle(True)
        self.CircleIconBtn_3.setType(Type.SUCCESS)
        self.CircleIconBtn_3.setIcon(QIcon(":/Arrow/Expand.svg"))
        self.CircleIconBtn_3.setIconColor(QColor(255,255,255))

        self.CircleIconBtn_4.isCircle(True)
        self.CircleIconBtn_4.setType(Type.INFO)
        self.CircleIconBtn_4.setIcon(QIcon(":/Food/Orange.svg"))
        self.CircleIconBtn_4.setIconColor(QColor(255,255,255))

        self.CircleIconBtn_5.isCircle(True)
        self.CircleIconBtn_5.setType(Type.WARNING)
        self.CircleIconBtn_5.setIcon(QIcon(":/Media/Microphone.svg"))
        self.CircleIconBtn_5.setIconColor(QColor(255,255,255))
        
        self.CircleIconBtn_6.isCircle(True)
        self.CircleIconBtn_6.setType(Type.DANGER)
        self.CircleIconBtn_6.setIcon(QIcon(":/Arrow/Expand.svg"))
        self.CircleIconBtn_6.setIconColor(QColor(255,255,255))
        

        # 默认禁用状态按钮样式
        self.DefaultBtnDisabled.setType(Type.DEFAULT)
        self.DefaultBtnDisabled.setEnabled(False)
        self.PrimaryBtnDisabled.setType(Type.PRIMARY)
        self.PrimaryBtnDisabled.setEnabled(False)
        self.SuccessBtnDisabled.setType(Type.SUCCESS)
        self.SuccessBtnDisabled.setEnabled(False)
        self.WarningBtnDisabled.setType(Type.WARNING)
        self.WarningBtnDisabled.setEnabled(False)
        self.DangerBtnDisabled.setType(Type.DANGER)
        self.DangerBtnDisabled.setEnabled(False)
        self.InfoBtnDisabled.setType(Type.INFO)
        self.InfoBtnDisabled.setEnabled(False)

        # 朴素禁用状态按钮样式
        self.PlainBtnDisabled.isPlain(True)
        self.PlainBtnDisabled.setEnabled(False)
        self.PlainPrimaryBtnDisabled.setType(Type.PRIMARY)
        self.PlainPrimaryBtnDisabled.isPlain(True)
        self.PlainPrimaryBtnDisabled.setEnabled(False)
        self.PlainSuccessBtnDisabled.setType(Type.SUCCESS)
        self.PlainSuccessBtnDisabled.isPlain(True)
        self.PlainSuccessBtnDisabled.setEnabled(False)
        self.PlainWarningBtnDisabled.setType(Type.WARNING)
        self.PlainWarningBtnDisabled.isPlain(True)
        self.PlainWarningBtnDisabled.setEnabled(False)
        self.PlainDangerBtnDisabled.setType(Type.DANGER)
        self.PlainDangerBtnDisabled.isPlain(True)
        self.PlainDangerBtnDisabled.setEnabled(False)
        self.PlainInfoBtnDisabled.setType(Type.INFO)
        self.PlainInfoBtnDisabled.isPlain(True)
        self.PlainInfoBtnDisabled.setEnabled(False)

        # 图标按钮
        self.IconButton.setType(Type.PRIMARY)
        self.IconButton.setIcon(QIcon(":/Food/Orange.svg"))
        self.IconButton.setIconColor(QColor(255,255,255))
        
        # 左侧图标文字按钮
        self.IconTextButtonLeft.setType(Type.PRIMARY)
        self.IconTextButtonLeft.setIcon(QIcon(":/System/Search.svg"))
        self.IconTextButtonLeft.setIconColor(QColor(255,255,255))
        self.IconTextButtonLeft.setText(" Search")

        # 右侧图标文字按钮
        self.IconTextButtonRight.setType(Type.PRIMARY)
        self.IconTextButtonRight.setIcon(QIcon(":/Arrow/Expand.svg"))
        self.IconTextButtonRight.setIconColor(QColor(255,255,255))
        self.IconTextButtonRight.setText("Expand ")
        self.IconTextButtonRight.setLayoutDirection(Qt.RightToLeft)


        # 调整尺寸
        # 左1
        self.LargeBtn.setSize(Size.LARGE)
        self.SmallBtn.setSize(Size.SMALL)


        # 右1
        self.IconTextLargeBtn.setSize(Size.LARGE)
        self.IconTextLargeBtn.setIcon(QIcon(":/System/Search.svg"))

        self.IconTextMediumBtn.setIcon(QIcon(":/System/Search.svg"))
        self.IconTextMediumBtn.setIconColor(QColor(255,255,255))
        self.IconTextMediumBtn.setType(Type.PRIMARY)

        self.IconTextSmallBtn.setSize(Size.SMALL)
        self.IconTextSmallBtn.setIcon(QIcon(":/System/Search.svg"))
        self.IconTextSmallBtn.setIconColor(QColor(255,255,255))
        self.IconTextSmallBtn.setType(Type.SUCCESS)

        # 左2
        self.RoundLargeBtn.setSize(Size.LARGE)
        self.RoundLargeBtn.isRound(True)
        
        self.RoundMediumBtn.setSize(Size.DEFAULT)
        self.RoundMediumBtn.isRound(True)
        
        self.RoundSmallBtn.setSize(Size.SMALL)
        self.RoundSmallBtn.isRound(True)

        # 右2
        self.IconRoundTextLargeBtn.setSize(Size.LARGE)
        self.IconRoundTextLargeBtn.isRound(True)
        self.IconRoundTextLargeBtn.setType(Type.INFO)
        self.IconRoundTextLargeBtn.setIcon(QIcon(":/System/Search.svg"))
        self.IconRoundTextLargeBtn.setIconColor(QColor(255,255,255))

        self.IconRoundTextMediumBtn.setSize(Size.DEFAULT)
        self.IconRoundTextMediumBtn.isRound(True)
        self.IconRoundTextMediumBtn.setType(Type.WARNING)
        self.IconRoundTextMediumBtn.setIcon(QIcon(":/System/Search.svg"))
        self.IconRoundTextMediumBtn.setIconColor(QColor(255,255,255))

        self.IconRoundTextSmallBtn.setSize(Size.SMALL)
        self.IconRoundTextSmallBtn.isRound(True)
        self.IconRoundTextSmallBtn.setType(Type.DANGER)
        self.IconRoundTextSmallBtn.setIcon(QIcon(":/System/Search.svg"))
        self.IconRoundTextSmallBtn.setIconColor(QColor(255,255,255))

        # 左3
        self.CircleIconLargeBtn.setSize(Size.LARGE)
        self.CircleIconLargeBtn.isCircle(True)
        self.CircleIconLargeBtn.setIcon(QIcon(":/System/Search.svg"))

        self.CircleIconMediumBtn.setSize(Size.DEFAULT)
        self.CircleIconMediumBtn.isCircle(True)
        self.CircleIconMediumBtn.setIcon(QIcon(":/System/Search.svg"))

        self.CircleIconSmallBtn.setSize(Size.SMALL)
        self.CircleIconSmallBtn.isCircle(True)
        self.CircleIconSmallBtn.setIcon(QIcon(":/System/Search.svg"))

        



        self.RoundLargeBtn.clicked.connect(self.logic_1)

    def ElListUI(self):
        firstItemFont = QFont()
        firstItemFont.setFamily("Microsoft YaHei")
        firstItemFont.setPointSize(14)
        firstItemFont.setBold(True)
        self.leftListWidget.addItem("Basic基础组件",level="1",first_style=firstItemFont)
        # QListWidgetItem("Button按钮",self.leftListWidget,level="2")
        self.leftListWidget.addItem("Button按钮",level="2")
        self.leftListWidget.addItem("Item 3",level="2")
        self.leftListWidget.addItem("Item 4",level="2")

        self.leftListWidget.setItemBackgroundColor(QColor(236,245,255))
        self.leftListWidget.setItemBorderRadius(8)


    '''Logic Func below'''
    
    def logic_1(self):
        print(self.RoundLargeBtn.height())
        print(self.RoundLargeBtn.width())
        
