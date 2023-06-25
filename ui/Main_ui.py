# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'h:\QtElementUI/ui/Main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(928, 719)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainWidget)
        self.horizontalLayout.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftListWidget = ElListWidget(MainWidget)
        self.leftListWidget.setObjectName("leftListWidget")
        self.horizontalLayout.addWidget(self.leftListWidget)
        self.previewStackedWidget = QtWidgets.QStackedWidget(MainWidget)
        self.previewStackedWidget.setStyleSheet("#previewStackedWidget{background-color: rgb(255, 255, 255);}")
        self.previewStackedWidget.setObjectName("previewStackedWidget")
        self.Buttons = QtWidgets.QWidget()
        self.Buttons.setStyleSheet(".QLabel{\n"
"    color:rgb(31, 31, 31);\n"
"}")
        self.Buttons.setObjectName("Buttons")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Buttons)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Buttons)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(-192, 0, 826, 934))
        self.scrollAreaWidgetContents_5.setStyleSheet("#scrollAreaWidgetContents_5{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DefaultBtn = ElButton(self.widget_2)
        self.DefaultBtn.setFlat(False)
        self.DefaultBtn.setObjectName("DefaultBtn")
        self.horizontalLayout_3.addWidget(self.DefaultBtn)
        self.PrimaryBtn = ElButton(self.widget_2)
        self.PrimaryBtn.setObjectName("PrimaryBtn")
        self.horizontalLayout_3.addWidget(self.PrimaryBtn)
        self.SuccessBtn = ElButton(self.widget_2)
        self.SuccessBtn.setObjectName("SuccessBtn")
        self.horizontalLayout_3.addWidget(self.SuccessBtn)
        self.InfoBtn = ElButton(self.widget_2)
        self.InfoBtn.setObjectName("InfoBtn")
        self.horizontalLayout_3.addWidget(self.InfoBtn)
        self.WarningBtn = ElButton(self.widget_2)
        self.WarningBtn.setObjectName("WarningBtn")
        self.horizontalLayout_3.addWidget(self.WarningBtn)
        self.DangerBtn = ElButton(self.widget_2)
        self.DangerBtn.setObjectName("DangerBtn")
        self.horizontalLayout_3.addWidget(self.DangerBtn)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.PlainBtn = ElButton(self.widget_3)
        self.PlainBtn.setObjectName("PlainBtn")
        self.horizontalLayout_5.addWidget(self.PlainBtn)
        self.PlainPrimaryBtn = ElButton(self.widget_3)
        self.PlainPrimaryBtn.setObjectName("PlainPrimaryBtn")
        self.horizontalLayout_5.addWidget(self.PlainPrimaryBtn)
        self.PlainSuccessBtn = ElButton(self.widget_3)
        self.PlainSuccessBtn.setObjectName("PlainSuccessBtn")
        self.horizontalLayout_5.addWidget(self.PlainSuccessBtn)
        self.PlainInfoBtn = ElButton(self.widget_3)
        self.PlainInfoBtn.setObjectName("PlainInfoBtn")
        self.horizontalLayout_5.addWidget(self.PlainInfoBtn)
        self.PlainWarningBtn = ElButton(self.widget_3)
        self.PlainWarningBtn.setObjectName("PlainWarningBtn")
        self.horizontalLayout_5.addWidget(self.PlainWarningBtn)
        self.PlainDangerBtn = ElButton(self.widget_3)
        self.PlainDangerBtn.setObjectName("PlainDangerBtn")
        self.horizontalLayout_5.addWidget(self.PlainDangerBtn)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RoundDefaultBtn = ElButton(self.widget)
        self.RoundDefaultBtn.setObjectName("RoundDefaultBtn")
        self.horizontalLayout_2.addWidget(self.RoundDefaultBtn)
        self.RoundPrimaryBtn = ElButton(self.widget)
        self.RoundPrimaryBtn.setObjectName("RoundPrimaryBtn")
        self.horizontalLayout_2.addWidget(self.RoundPrimaryBtn)
        self.RoundSuccessBtn = ElButton(self.widget)
        self.RoundSuccessBtn.setObjectName("RoundSuccessBtn")
        self.horizontalLayout_2.addWidget(self.RoundSuccessBtn)
        self.RoundInfoBtn = ElButton(self.widget)
        self.RoundInfoBtn.setObjectName("RoundInfoBtn")
        self.horizontalLayout_2.addWidget(self.RoundInfoBtn)
        self.RoundWarningBtn = ElButton(self.widget)
        self.RoundWarningBtn.setObjectName("RoundWarningBtn")
        self.horizontalLayout_2.addWidget(self.RoundWarningBtn)
        self.RoundDangerBtn = ElButton(self.widget)
        self.RoundDangerBtn.setObjectName("RoundDangerBtn")
        self.horizontalLayout_2.addWidget(self.RoundDangerBtn)
        self.verticalLayout.addWidget(self.widget)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.CircleIconBtn_1 = ElButton(self.widget_4)
        self.CircleIconBtn_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CircleIconBtn_1.setStyleSheet("color: rgb(85, 255, 0);")
        self.CircleIconBtn_1.setText("")
        self.CircleIconBtn_1.setIconSize(QtCore.QSize(20, 20))
        self.CircleIconBtn_1.setObjectName("CircleIconBtn_1")
        self.horizontalLayout_4.addWidget(self.CircleIconBtn_1)
        self.CircleIconBtn_2 = ElButton(self.widget_4)
        self.CircleIconBtn_2.setText("")
        self.CircleIconBtn_2.setObjectName("CircleIconBtn_2")
        self.horizontalLayout_4.addWidget(self.CircleIconBtn_2)
        self.CircleIconBtn_3 = ElButton(self.widget_4)
        self.CircleIconBtn_3.setText("")
        self.CircleIconBtn_3.setObjectName("CircleIconBtn_3")
        self.horizontalLayout_4.addWidget(self.CircleIconBtn_3)
        self.CircleIconBtn_4 = ElButton(self.widget_4)
        self.CircleIconBtn_4.setText("")
        self.CircleIconBtn_4.setObjectName("CircleIconBtn_4")
        self.horizontalLayout_4.addWidget(self.CircleIconBtn_4)
        self.CircleIconBtn_5 = ElButton(self.widget_4)
        self.CircleIconBtn_5.setText("")
        self.CircleIconBtn_5.setObjectName("CircleIconBtn_5")
        self.horizontalLayout_4.addWidget(self.CircleIconBtn_5)
        self.CircleIconBtn_6 = ElButton(self.widget_4)
        self.CircleIconBtn_6.setText("")
        self.CircleIconBtn_6.setObjectName("CircleIconBtn_6")
        self.horizontalLayout_4.addWidget(self.CircleIconBtn_6)
        self.verticalLayout.addWidget(self.widget_4)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.DefaultBtnDisabled = ElButton(self.widget_5)
        self.DefaultBtnDisabled.setFlat(False)
        self.DefaultBtnDisabled.setObjectName("DefaultBtnDisabled")
        self.horizontalLayout_6.addWidget(self.DefaultBtnDisabled)
        self.PrimaryBtnDisabled = ElButton(self.widget_5)
        self.PrimaryBtnDisabled.setObjectName("PrimaryBtnDisabled")
        self.horizontalLayout_6.addWidget(self.PrimaryBtnDisabled)
        self.SuccessBtnDisabled = ElButton(self.widget_5)
        self.SuccessBtnDisabled.setObjectName("SuccessBtnDisabled")
        self.horizontalLayout_6.addWidget(self.SuccessBtnDisabled)
        self.InfoBtnDisabled = ElButton(self.widget_5)
        self.InfoBtnDisabled.setObjectName("InfoBtnDisabled")
        self.horizontalLayout_6.addWidget(self.InfoBtnDisabled)
        self.WarningBtnDisabled = ElButton(self.widget_5)
        self.WarningBtnDisabled.setObjectName("WarningBtnDisabled")
        self.horizontalLayout_6.addWidget(self.WarningBtnDisabled)
        self.DangerBtnDisabled = ElButton(self.widget_5)
        self.DangerBtnDisabled.setObjectName("DangerBtnDisabled")
        self.horizontalLayout_6.addWidget(self.DangerBtnDisabled)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.PlainBtnDisabled = ElButton(self.widget_6)
        self.PlainBtnDisabled.setObjectName("PlainBtnDisabled")
        self.horizontalLayout_7.addWidget(self.PlainBtnDisabled)
        self.PlainPrimaryBtnDisabled = ElButton(self.widget_6)
        self.PlainPrimaryBtnDisabled.setObjectName("PlainPrimaryBtnDisabled")
        self.horizontalLayout_7.addWidget(self.PlainPrimaryBtnDisabled)
        self.PlainSuccessBtnDisabled = ElButton(self.widget_6)
        self.PlainSuccessBtnDisabled.setObjectName("PlainSuccessBtnDisabled")
        self.horizontalLayout_7.addWidget(self.PlainSuccessBtnDisabled)
        self.PlainInfoBtnDisabled = ElButton(self.widget_6)
        self.PlainInfoBtnDisabled.setObjectName("PlainInfoBtnDisabled")
        self.horizontalLayout_7.addWidget(self.PlainInfoBtnDisabled)
        self.PlainWarningBtnDisabled = ElButton(self.widget_6)
        self.PlainWarningBtnDisabled.setObjectName("PlainWarningBtnDisabled")
        self.horizontalLayout_7.addWidget(self.PlainWarningBtnDisabled)
        self.PlainDangerBtnDisabled = ElButton(self.widget_6)
        self.PlainDangerBtnDisabled.setObjectName("PlainDangerBtnDisabled")
        self.horizontalLayout_7.addWidget(self.PlainDangerBtnDisabled)
        self.verticalLayout.addWidget(self.widget_6)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.widget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.IconButton = ElButton(self.widget_7)
        self.IconButton.setText("")
        self.IconButton.setObjectName("IconButton")
        self.horizontalLayout_8.addWidget(self.IconButton)
        self.IconTextButtonLeft = ElButton(self.widget_7)
        self.IconTextButtonLeft.setText("")
        self.IconTextButtonLeft.setObjectName("IconTextButtonLeft")
        self.horizontalLayout_8.addWidget(self.IconTextButtonLeft)
        self.IconTextButtonRight = ElButton(self.widget_7)
        self.IconTextButtonRight.setText("")
        self.IconTextButtonRight.setObjectName("IconTextButtonRight")
        self.horizontalLayout_8.addWidget(self.IconTextButtonRight)
        self.verticalLayout.addWidget(self.widget_7)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.widget_8 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_10 = QtWidgets.QWidget(self.widget_8)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.IconTextLargeBtn = ElButton(self.widget_10)
        self.IconTextLargeBtn.setObjectName("IconTextLargeBtn")
        self.horizontalLayout_10.addWidget(self.IconTextLargeBtn)
        self.IconTextMediumBtn = ElButton(self.widget_10)
        self.IconTextMediumBtn.setObjectName("IconTextMediumBtn")
        self.horizontalLayout_10.addWidget(self.IconTextMediumBtn)
        self.IconTextSmallBtn = ElButton(self.widget_10)
        self.IconTextSmallBtn.setObjectName("IconTextSmallBtn")
        self.horizontalLayout_10.addWidget(self.IconTextSmallBtn)
        self.gridLayout.addWidget(self.widget_10, 0, 1, 1, 1)
        self.widget_11 = QtWidgets.QWidget(self.widget_8)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.IconRoundTextLargeBtn = ElButton(self.widget_11)
        self.IconRoundTextLargeBtn.setObjectName("IconRoundTextLargeBtn")
        self.horizontalLayout_12.addWidget(self.IconRoundTextLargeBtn)
        self.IconRoundTextMediumBtn = ElButton(self.widget_11)
        self.IconRoundTextMediumBtn.setObjectName("IconRoundTextMediumBtn")
        self.horizontalLayout_12.addWidget(self.IconRoundTextMediumBtn)
        self.IconRoundTextSmallBtn = ElButton(self.widget_11)
        self.IconRoundTextSmallBtn.setObjectName("IconRoundTextSmallBtn")
        self.horizontalLayout_12.addWidget(self.IconRoundTextSmallBtn)
        self.gridLayout.addWidget(self.widget_11, 1, 1, 1, 1)
        self.widget_12 = QtWidgets.QWidget(self.widget_8)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.RoundLargeBtn = ElButton(self.widget_12)
        self.RoundLargeBtn.setObjectName("RoundLargeBtn")
        self.horizontalLayout_11.addWidget(self.RoundLargeBtn)
        self.RoundMediumBtn = ElButton(self.widget_12)
        self.RoundMediumBtn.setObjectName("RoundMediumBtn")
        self.horizontalLayout_11.addWidget(self.RoundMediumBtn)
        self.RoundSmallBtn = ElButton(self.widget_12)
        self.RoundSmallBtn.setObjectName("RoundSmallBtn")
        self.horizontalLayout_11.addWidget(self.RoundSmallBtn)
        self.gridLayout.addWidget(self.widget_12, 1, 0, 1, 1)
        self.widget_13 = QtWidgets.QWidget(self.widget_8)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.CircleIconLargeBtn = ElButton(self.widget_13)
        self.CircleIconLargeBtn.setText("")
        self.CircleIconLargeBtn.setObjectName("CircleIconLargeBtn")
        self.horizontalLayout_13.addWidget(self.CircleIconLargeBtn)
        self.CircleIconMediumBtn = ElButton(self.widget_13)
        self.CircleIconMediumBtn.setText("")
        self.CircleIconMediumBtn.setObjectName("CircleIconMediumBtn")
        self.horizontalLayout_13.addWidget(self.CircleIconMediumBtn)
        self.CircleIconSmallBtn = ElButton(self.widget_13)
        self.CircleIconSmallBtn.setText("")
        self.CircleIconSmallBtn.setObjectName("CircleIconSmallBtn")
        self.horizontalLayout_13.addWidget(self.CircleIconSmallBtn)
        self.gridLayout.addWidget(self.widget_13, 2, 0, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.LargeBtn = ElButton(self.widget_9)
        self.LargeBtn.setObjectName("LargeBtn")
        self.horizontalLayout_9.addWidget(self.LargeBtn)
        self.MediumBtn = ElButton(self.widget_9)
        self.MediumBtn.setObjectName("MediumBtn")
        self.horizontalLayout_9.addWidget(self.MediumBtn)
        self.SmallBtn = ElButton(self.widget_9)
        self.SmallBtn.setObjectName("SmallBtn")
        self.horizontalLayout_9.addWidget(self.SmallBtn)
        self.gridLayout.addWidget(self.widget_9, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_8)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.previewStackedWidget.addWidget(self.Buttons)
        self.previewStackedWidgetPage2 = QtWidgets.QWidget()
        self.previewStackedWidgetPage2.setObjectName("previewStackedWidgetPage2")
        self.previewStackedWidget.addWidget(self.previewStackedWidgetPage2)
        self.horizontalLayout.addWidget(self.previewStackedWidget)
        self.horizontalLayout.setStretch(1, 8)

        self.retranslateUi(MainWidget)
        self.previewStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Form"))
        self.label_2.setText(_translate("MainWidget", "Button 按钮"))
        self.label.setText(_translate("MainWidget", "基础用法"))
        self.label_6.setText(_translate("MainWidget", "<html><head/><body><p><span style=\" font-size:11pt;\">使用 </span><span style=\" font-family:\'JetBrains Mono\'; font-size:11pt;\">type</span><span style=\" font-size:11pt;\">、</span><span style=\" font-family:\'JetBrains Mono\'; font-size:11pt;\">plain</span><span style=\" font-size:11pt;\">、</span><span style=\" font-family:\'JetBrains Mono\'; font-size:11pt;\">round</span><span style=\" font-size:11pt;\"> 和 </span><span style=\" font-family:\'JetBrains Mono\'; font-size:11pt;\">circle</span><span style=\" font-size:11pt;\"> 来定义按钮的样式。</span></p></body></html>"))
        self.DefaultBtn.setText(_translate("MainWidget", "Default"))
        self.PrimaryBtn.setText(_translate("MainWidget", "Primary"))
        self.SuccessBtn.setText(_translate("MainWidget", "Success"))
        self.InfoBtn.setText(_translate("MainWidget", "Info"))
        self.WarningBtn.setText(_translate("MainWidget", "Warning"))
        self.DangerBtn.setText(_translate("MainWidget", "Danger"))
        self.PlainBtn.setText(_translate("MainWidget", "Plain"))
        self.PlainPrimaryBtn.setText(_translate("MainWidget", "Primary"))
        self.PlainSuccessBtn.setText(_translate("MainWidget", "Success"))
        self.PlainInfoBtn.setText(_translate("MainWidget", "Info"))
        self.PlainWarningBtn.setText(_translate("MainWidget", "Warning"))
        self.PlainDangerBtn.setText(_translate("MainWidget", "Danger"))
        self.RoundDefaultBtn.setText(_translate("MainWidget", "Round"))
        self.RoundPrimaryBtn.setText(_translate("MainWidget", "Primary"))
        self.RoundSuccessBtn.setText(_translate("MainWidget", "Success"))
        self.RoundInfoBtn.setText(_translate("MainWidget", "Info"))
        self.RoundWarningBtn.setText(_translate("MainWidget", "Warning"))
        self.RoundDangerBtn.setText(_translate("MainWidget", "Danger"))
        self.label_3.setText(_translate("MainWidget", "禁用状态"))
        self.label_7.setText(_translate("MainWidget", "你可以使用 disabled 属性来定义按钮是否被禁用。\n"
"使用 disabled 属性来控制按钮是否为禁用状态。 该属性接受一个 Boolean 类型的值。"))
        self.DefaultBtnDisabled.setText(_translate("MainWidget", "Default"))
        self.PrimaryBtnDisabled.setText(_translate("MainWidget", "Primary"))
        self.SuccessBtnDisabled.setText(_translate("MainWidget", "Success"))
        self.InfoBtnDisabled.setText(_translate("MainWidget", "Info"))
        self.WarningBtnDisabled.setText(_translate("MainWidget", "Warning"))
        self.DangerBtnDisabled.setText(_translate("MainWidget", "Danger"))
        self.PlainBtnDisabled.setText(_translate("MainWidget", "Plain"))
        self.PlainPrimaryBtnDisabled.setText(_translate("MainWidget", "Primary"))
        self.PlainSuccessBtnDisabled.setText(_translate("MainWidget", "Success"))
        self.PlainInfoBtnDisabled.setText(_translate("MainWidget", "Info"))
        self.PlainWarningBtnDisabled.setText(_translate("MainWidget", "Warning"))
        self.PlainDangerBtnDisabled.setText(_translate("MainWidget", "Danger"))
        self.label_4.setText(_translate("MainWidget", "图标按钮"))
        self.label_8.setText(_translate("MainWidget", "使用图标为按钮添加更多的含义。 你也可以单独使用图标不添加文字来节省显示区域占用。"))
        self.label_5.setText(_translate("MainWidget", "调整尺寸"))
        self.label_9.setText(_translate("MainWidget", "除了默认的大小，按钮组件还提供了几种额外的尺寸可供选择，以便适配不同的场景。"))
        self.IconTextLargeBtn.setText(_translate("MainWidget", "Search"))
        self.IconTextMediumBtn.setText(_translate("MainWidget", "Search"))
        self.IconTextSmallBtn.setText(_translate("MainWidget", "Search"))
        self.IconRoundTextLargeBtn.setText(_translate("MainWidget", "Search"))
        self.IconRoundTextMediumBtn.setText(_translate("MainWidget", "Search"))
        self.IconRoundTextSmallBtn.setText(_translate("MainWidget", "Search"))
        self.RoundLargeBtn.setText(_translate("MainWidget", "Large"))
        self.RoundMediumBtn.setText(_translate("MainWidget", "Default"))
        self.RoundSmallBtn.setText(_translate("MainWidget", "Small"))
        self.LargeBtn.setText(_translate("MainWidget", "Large"))
        self.MediumBtn.setText(_translate("MainWidget", "Default"))
        self.SmallBtn.setText(_translate("MainWidget", "Small"))
from components.elbutton import ElButton
from components.ellistwidget import ElListWidget
from Icons import Icons_rc
