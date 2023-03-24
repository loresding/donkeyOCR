"""
自定义的通知消息框
作者: LoresDing
时间: 2023/03/22
"""
from modules import *
from widgets import *


class OCRMessageBox(QDialog):
    """
    OCR界面通知框
    """
    def __init__(self, parent=None, title="通知"):
        super().__init__(parent)
        # 通知框标题
        self.setWindowTitle(title)
        # 设置样式
        self.setStyleSheet('''
            QDialog {background-color: rgb(52, 59, 72);color: rgb(255, 170, 255);}
            QDialog QLabel{color: rgb(255, 170, 255);}
            QDialog QProgressBar{background-color: rgb(52, 59, 72);color: white;text-align: center;border-radius: 5px; border: 2px solid grey}
            QDialog QProgressBar::chunk{background-color: rgb(255, 170, 255)}
            ''')
        # 进度条
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.resize(300, 20)
        self.progress_bar.setFormat('识别中 %p%'.format(self.progress_bar.value()-self.progress_bar.minimum()))
        self.progress_bar.move(50, 35)
        
    def resizeEvent(self, event):
        self.setFixedSize(400, 90)

    def showEvent(self, event):
        super().showEvent(event)
        self.setFixedSize(400, 90)
    
    def update_value(self, index, num):
        if num == 0:
            self.progress_bar.setValue(0)
        else:
            self.progress_bar.setValue(int((index+1)/num*100))