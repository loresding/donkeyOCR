"""
作者: LoresDing
版本: v2.0.0
时间: 2023/03/22
用于绑定结果显示操作事件
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem, QApplication
from gui.widgets import ZoomInMessageBox

class ResultViewFunctions:
    """
    识别结果文字展示事件
    """
    def __init__(self, window):
        self.window = window
        # 默认为框选文字tab页
        self.window.ui.resultTabs.setCurrentIndex(1)
        self.bindZoomInBtn()
        self.bindCutBtn()
        self.message = ZoomInMessageBox()

    def updateText(self, recognitions):
        """
        更新listwidget文本内容
        """
        # 设置textEdit文本
        self.window.ui.textEdit.setText("\n".join([item["text"] for item in recognitions]))
        # 清空ListWidget列表
        self.window.ui.listWidget.clear()
        for recognition in recognitions:
            item = QListWidgetItem(self.window.ui.listWidget)
            # 对齐方式：垂直方向居中，水平方向靠左
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)
            # 设置Item文字内容
            item.setText(recognition["text"])
            item.setCheckState(Qt.Checked)
            # 将Item添加到listWidget中
            self.window.ui.listWidget.addItem(item)

    def bindZoomInBtn(self):
        """
        放大结果按钮绑定事件
        """
        def zoomIn():
            tab_index = self.window.ui.resultTabs.currentIndex()
            text = ""
            if tab_index == 0:
                text = self.window.ui.textEdit.toPlainText()
            else:
                text = self.window.ui.listWidget.currentItem().text()
            self.message.updateText(text)
            self.message.exec_()
        self.window.ui.zoomInBtn.clicked.connect(zoomIn)

    def bindCutBtn(self):
        """
        复制按钮绑定事件
        """
        def cut():
            clipboard = QApplication.clipboard()
            clipboard.setText(self.window.ui.listWidget.currentItem().text())   
        self.window.ui.cutBtn.clicked.connect(cut)
        
        

        


    
