# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 716)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.app = QWidget(MainWindow)
        self.app.setObjectName(u"app")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.app.setFont(font)
        self.appMargins = QVBoxLayout(self.app)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.titles = QFrame(self.app)
        self.titles.setObjectName(u"titles")
        self.titles.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(33, 37, 43);\n"
" 	border: none;\n"
"}\n"
"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" 	border: none;  \n"
"	border-radius: 5px;\n"
" }\n"
"QPushButton:hover { \n"
"	background-color: rgb(44, 49, 57); \n"
"	border-style: solid; \n"
"	border-radius: 4px; \n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(23, 26, 30); \n"
"	border-style: solid; \n"
"	border-radius: 4px; \n"
"}")
        self.titles.setFrameShape(QFrame.StyledPanel)
        self.titles.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titles)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.titleInfo = QFrame(self.titles)
        self.titleInfo.setObjectName(u"titleInfo")
        self.titleInfo.setFrameShape(QFrame.StyledPanel)
        self.titleInfo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleInfo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.titleInfo)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"padding-left: 10px;color: white;")

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.titleInfo)

        self.titleBtns = QFrame(self.titles)
        self.titleBtns.setObjectName(u"titleBtns")
        self.titleBtns.setFrameShape(QFrame.StyledPanel)
        self.titleBtns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.titleBtns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.minimizeBtn = QPushButton(self.titleBtns)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon)
        self.minimizeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.maxmizeBtn = QPushButton(self.titleBtns)
        self.maxmizeBtn.setObjectName(u"maxmizeBtn")
        self.maxmizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxmizeBtn.setIcon(icon1)
        self.maxmizeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.maxmizeBtn)

        self.closeBtn = QPushButton(self.titleBtns)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout.addWidget(self.titleBtns)

        self.horizontalLayout.setStretch(0, 15)
        self.horizontalLayout.setStretch(1, 1)

        self.appMargins.addWidget(self.titles)

        self.content = QFrame(self.app)
        self.content.setObjectName(u"content")
        self.content.setCursor(QCursor(Qt.ArrowCursor))
        self.content.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(40, 44, 52);\n"
"}")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.operateBtns = QFrame(self.content)
        self.operateBtns.setObjectName(u"operateBtns")
        self.operateBtns.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: none;\n"
"}\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color:  rgb(52, 59, 72);\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.operateBtns.setFrameShape(QFrame.StyledPanel)
        self.operateBtns.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.operateBtns)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ocrBtn = QPushButton(self.operateBtns)
        self.ocrBtn.setObjectName(u"ocrBtn")
        self.ocrBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ocrBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(189, 147, 249);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(189, 147, 249);\n"
"	border: 2px solid rgb(189, 147, 249);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(153, 120, 202);\n"
"	border: 2px solid rgb(153, 120, 202);\n"
"}")

        self.verticalLayout.addWidget(self.ocrBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.screenshotBtn = QPushButton(self.operateBtns)
        self.screenshotBtn.setObjectName(u"screenshotBtn")
        self.screenshotBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-screen-desktop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.screenshotBtn.setIcon(icon3)

        self.verticalLayout.addWidget(self.screenshotBtn)

        self.imageBtn = QPushButton(self.operateBtns)
        self.imageBtn.setObjectName(u"imageBtn")
        self.imageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-image-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imageBtn.setIcon(icon4)

        self.verticalLayout.addWidget(self.imageBtn)

        self.pdfBtn = QPushButton(self.operateBtns)
        self.pdfBtn.setObjectName(u"pdfBtn")
        self.pdfBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pdfBtn.setIcon(icon5)

        self.verticalLayout.addWidget(self.pdfBtn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.lastPageBtn = QPushButton(self.operateBtns)
        self.lastPageBtn.setObjectName(u"lastPageBtn")
        self.lastPageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.lastPageBtn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-caret-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lastPageBtn.setIcon(icon6)

        self.verticalLayout.addWidget(self.lastPageBtn)

        self.nextPageBtn = QPushButton(self.operateBtns)
        self.nextPageBtn.setObjectName(u"nextPageBtn")
        self.nextPageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-caret-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextPageBtn.setIcon(icon7)

        self.verticalLayout.addWidget(self.nextPageBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 20)

        self.horizontalLayout_4.addWidget(self.operateBtns)

        self.source = QFrame(self.content)
        self.source.setObjectName(u"source")
        self.source.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.source.setFrameShape(QFrame.StyledPanel)
        self.source.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.source)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sourceView = QGraphicsView(self.source)
        self.sourceView.setObjectName(u"sourceView")

        self.verticalLayout_3.addWidget(self.sourceView)

        self.pageLabel = QLabel(self.source)
        self.pageLabel.setObjectName(u"pageLabel")
        self.pageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.pageLabel)

        self.verticalLayout_3.setStretch(0, 30)
        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_4.addWidget(self.source)

        self.reuslts = QFrame(self.content)
        self.reuslts.setObjectName(u"reuslts")
        self.reuslts.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: none;\n"
"}\n"
"QTabWidget::pane {\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QTabBar::tab {\n"
"	color:  white;\n"
"	background-color:  rgb(40, 44, 52);\n"
"}\n"
"QTabBar::tab:selected {\n"
"	color:  white;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color:  rgb(52, 59, 72);\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"QTextEdit QScrollBar:horizontal{\n"
"	border: none;\n"
"	background: rgb(189, 147, 249);\n"
"	width: 8px;\n"
"	margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"QTextEdit QScrollBar"
                        ":vertical{\n"
"	border: none;\n"
"	background: rgb(189, 147, 249);\n"
"	width: 8px;\n"
"	margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"QListWidget {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"QListWidget QScrollBar:horizontal{\n"
"	border: none;\n"
"	background: rgb(189, 147, 249);\n"
"	width: 8px;\n"
"	margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"QListWidget QScrollBar:vertical{\n"
"	border: none;\n"
"	background: rgb(189, 147, 249);\n"
"	width: 8px;\n"
"	margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
"}")
        self.reuslts.setFrameShape(QFrame.StyledPanel)
        self.reuslts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.reuslts)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.resultTabs = QTabWidget(self.reuslts)
        self.resultTabs.setObjectName(u"resultTabs")
        self.resultTabs.setCursor(QCursor(Qt.ArrowCursor))
        self.text = QWidget()
        self.text.setObjectName(u"text")
        self.horizontalLayout_7 = QHBoxLayout(self.text)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.textEdit = QTextEdit(self.text)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMidLineWidth(0)

        self.horizontalLayout_7.addWidget(self.textEdit)

        self.resultTabs.addTab(self.text, "")
        self.boxes = QWidget()
        self.boxes.setObjectName(u"boxes")
        self.boxes.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalLayout_6 = QHBoxLayout(self.boxes)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.listWidget = QListWidget(self.boxes)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_6.addWidget(self.listWidget)

        self.resultTabs.addTab(self.boxes, "")

        self.verticalLayout_2.addWidget(self.resultTabs)

        self.zoomInBtn = QPushButton(self.reuslts)
        self.zoomInBtn.setObjectName(u"zoomInBtn")
        self.zoomInBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomInBtn.setIcon(icon8)

        self.verticalLayout_2.addWidget(self.zoomInBtn)

        self.cutBtn = QPushButton(self.reuslts)
        self.cutBtn.setObjectName(u"cutBtn")
        self.cutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-cut.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cutBtn.setIcon(icon9)

        self.verticalLayout_2.addWidget(self.cutBtn)


        self.horizontalLayout_4.addWidget(self.reuslts)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 7)
        self.horizontalLayout_4.setStretch(2, 2)

        self.appMargins.addWidget(self.content)

        self.appMargins.setStretch(0, 1)
        self.appMargins.setStretch(1, 20)
        MainWindow.setCentralWidget(self.app)

        self.retranslateUi(MainWindow)

        self.resultTabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"OCR\u8bc6\u522b", None))
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
        self.maxmizeBtn.setText("")
        self.closeBtn.setText("")
        self.ocrBtn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.screenshotBtn.setText(QCoreApplication.translate("MainWindow", u"\u5c4f\u5e55\u622a\u56fe", None))
        self.imageBtn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.pdfBtn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20PDF", None))
        self.lastPageBtn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.nextPageBtn.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.pageLabel.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.resultTabs.setTabText(self.resultTabs.indexOf(self.text), QCoreApplication.translate("MainWindow", u"\u6574\u4f53\u6587\u5b57", None))
        self.resultTabs.setTabText(self.resultTabs.indexOf(self.boxes), QCoreApplication.translate("MainWindow", u"\u6846\u9009\u6587\u5b57", None))
        self.zoomInBtn.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5927\u67e5\u770b", None))
        self.cutBtn.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u5230\u526a\u5207\u677f", None))
    # retranslateUi

