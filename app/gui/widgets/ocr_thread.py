"""
自定义线程
作者: LoresDing
时间: 2023/03/22
识别进程
"""
from PySide6.QtCore import QThread, Signal
from core import chineseOcr
from settings import Settings

class OCRThread(QThread):
    """
    ocr识别线程
    """
    signal = Signal(int, str)
    def __init__(self):
        super().__init__()

    def run(self):
        """
        执行ocr
        """
        for index, lines in chineseOcr():
            self.signal.emit(index, lines)
            
