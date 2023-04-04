"""
作者: LoresDing
版本: v2.0.0
时间: 2023/03/22
用于隐藏默认标题栏, 并自定义标题栏
"""
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

class TitleBarFunctions:
    """
    自定义标题栏事件
    """
    def __init__(self, window=None):
        self.window = window
        self.isNormalFlag = True
        # 标题栏设置
        self.hideDefaultBar()
        self.resetPressEvent()
        self.resetMoveEvent()
        self.resetNormalMaxmizeEvent()
        # 标题栏按钮事件绑定
        self.window.ui.minimizeBtn.clicked.connect(lambda: self.window.showMinimized())
        self.window.ui.closeBtn.clicked.connect(lambda: self.window.close())

    def hideDefaultBar(self):
        """
        隐藏默认标题栏
        """
        self.window.setWindowFlags(Qt.FramelessWindowHint)
        self.window.setAttribute(Qt.WA_TranslucentBackground)

    def resetPressEvent(self):
        """
        重新设定按鼠标的事件
        """
        def pressTitle(event):
            if event.buttons() == Qt.LeftButton:
                self.dragPos = event.globalPos()
        self.window.ui.titleInfo.mousePressEvent = pressTitle
        
    def resetMoveEvent(self):
        """
        重新设定移动标签栏的事件
        """
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.window.move(self.window.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.window.ui.titleInfo.mouseMoveEvent = moveWindow

    def resetNormalMaxmizeEvent(self):
        """
        重新设定通过双击标签栏和全屏按钮放大缩小的事件
        """
        def setNormalMaxmize(event):
            if self.isNormalFlag == True:
                self.window.showMaximized()
                self.window.ui.maxmizeBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
                self.isNormalFlag = False
            else:
                self.window.showNormal()
                self.window.ui.maxmizeBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
                self.isNormalFlag = True
        
        self.window.ui.titleInfo.mouseDoubleClickEvent = setNormalMaxmize
        self.window.ui.maxmizeBtn.clicked.connect(setNormalMaxmize)


