"""
自定义线程
作者: LoresDing
时间: 2023/03/22
"""
import json
from modules import *
from widgets import *
from .core import chinese_ocr

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
        for index, lines in chinese_ocr(Settings.CACHE_PATH, 
                                        Settings.CNOCR_MODEL_NAME, 
                                        Settings.CNOCR_MODEL_ROOT):
            self.signal.emit(index, lines)
            
