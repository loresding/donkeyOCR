"""
作者: LoresDing
版本: v2.0.0
程序主入口
用于交流, 禁止商用
Main program entrance.
For technical exchange, commercial use prohibited!
"""


import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QPixmap
from gui.widgets import Ui_MainWindow
from gui.functions import TitleBarFunctions, OperateBtnsFunctions, SourceViewFunctions, ResultViewFunctions

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
     
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #     # 软件名称和描述
    #     # 小窗口标题
    #     title = "DonkeyOCR"
    #     description = "DonkeyOCR - 中文OCR."
    #     self.setWindowTitle(title)
    #     widgets.titleRightInfo.setText(description)

    #     # 标题块样式
    #     # 系统为mac/linux为设为False
    #     Settings.ENABLE_CUSTOM_TITLE_BAR = True

    #     # 自定义主题样式
    #     useCustomTheme = False
    #     themeFile = "themes\py_dracula_light.qss"
    #     if useCustomTheme:
    #         UIFunctions.theme(self, themeFile, True)
    #         AppFunctions.setThemeHack(self)

    #     # 默认界面
    #     widgets.stackedWidget.setCurrentWidget(widgets.ocr)

    #     # 文件转换界面
    #     OCRFunctions.binding(self)

    #     # SET UI DEFINITIONS
    #     UIFunctions.uiDefinitions(self)
        self.source_view_funcs = SourceViewFunctions(self)
        TitleBarFunctions(self)
        OperateBtnsFunctions(self)
        self.result_view_funcs = ResultViewFunctions(self)
        # 软件展示
        self.show()

    # # RESIZE EVENTS
    # def resizeEvent(self, event):
    #     UIFunctions.resize_grips(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QPixmap("./donkey.png"))
    window = MainWindow()
    sys.exit(app.exec())
