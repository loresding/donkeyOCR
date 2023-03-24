# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # 软件名称和描述
        # 小窗口标题
        title = "DonkeyOCR"
        description = "DonkeyOCR - 中文OCR."
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # 标题块样式
        # 系统为mac/linux为设为False
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # 自定义主题样式
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"
        if useCustomTheme:
            UIFunctions.theme(self, themeFile, True)
            AppFunctions.setThemeHack(self)

        # 默认界面
        widgets.stackedWidget.setCurrentWidget(widgets.ocr)

        # 文件转换界面
        OCRFunctions.binding(self)

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)
        
        # 软件展示
        self.show()

    # RESIZE EVENTS
    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QPixmap("./donkey.png"))
    window = MainWindow()
    sys.exit(app.exec())
