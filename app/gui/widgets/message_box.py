"""
自定义的通知消息框
作者: LoresDing
时间: 2023/03/22
弹窗消息框, 包括识别界面消息框和结果放大消息框
"""
from PySide6.QtWidgets import QDialog, QProgressBar, QTextEdit
from PySide6.QtCore import Qt


class MessageBox(QDialog):
    """
    OCR识别进度界面通知框
    """
    def __init__(self, parent=None, title="识别中"):
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
    
    def updateValue(self, index, num):
        if num == 0:
            self.progress_bar.setValue(0)
        else:
            self.progress_bar.setValue(int((index+1)/num*100))


class ZoomInMessageBox(QDialog):
    """
    识别结果放大查看通知框
    """
    def __init__(self, parent=None, title="放大查看"):
        super().__init__(parent)
        # 通知框标题
        self.setWindowTitle(title)
        # 设置样式
        self.setStyleSheet('''
            QDialog {background-color: rgb(52, 59, 72);color: rgb(255, 170, 255);}
            QDialog QTextEdit{color: white; background-color: rgb(52, 59, 72);}
            ''')
        self.textEdit = QTextEdit(self)
        self.textEdit.resize(400, 600)

    def resizeEvent(self, event):
        self.setFixedSize(400, 600)
    
    def updateText(self, text):
        """
        更新放大
        """
        self.textEdit.setText(text)
