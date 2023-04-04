"""
作者: LoresDing
版本: v2.0.0
时间: 2023/03/22
用于左侧按钮绑定事件
"""
import os
import json
import shutil
from PIL import Image
from PySide6.QtWidgets import QFileDialog
from core import getPdfImages
from settings import Settings
from gui.widgets import OCRThread, MessageBox, ScreenshotWidget

class OperateBtnsFunctions:
    """
    操作按钮事件
    """
    def __init__(self, window=None):
        self.window = window
        # 当前页码
        self.page_index = 0
        # 图片总数
        self.page_num = 1
        # 识别结果
        self.recognitions = {}
        # 进度通知栏
        self.message_box = MessageBox(self.window)
        # 截屏widget
        self.screenshot_widget = ScreenshotWidget()
        # 按钮绑定事件
        self.bindImageBtn()
        self.bindPdfBtn()
        self.bindOcrBtn()
        self.bindLastPageBtn()
        self.bindNextPageBtn()
        self.bindScreenshotBtn()

    def bindImageBtn(self):
        """
        上传图片按钮绑定事件
        """
        def uploadImage():
             # 对话框选择图片
            filenames, _ = QFileDialog.getOpenFileNames(self.window, "选择图片文件", "C://", "图片 (*.png *.jpg *.PNG *.JPG)")
            if len(filenames) > 0:
                # 清空缓存路径
                cache_path = Settings.CACHE_PATH
                if os.path.exists(cache_path):
                    shutil.rmtree(cache_path)
                os.makedirs(cache_path, exist_ok=True)
                # 拷贝文件
                for index, filename in enumerate(filenames):
                    temp = Image.open(filename)
                    new_filename = os.path.join(cache_path, str(index+1) + ".png")
                    temp.save(new_filename)
                # 更新界面
                self.updateWindow(reset=True)
        self.window.ui.imageBtn.clicked.connect(uploadImage)

    def bindPdfBtn(self):
        """
        上传图片按钮绑定事件
        """
        def uploadPDF():
            # 对话框选择图片
            filename, _ = QFileDialog.getOpenFileName(self.window, "选择PDF文件", "C://", "PDF (*.pdf)")
            if filename:
                # 从选择的文件获取图片
                getPdfImages(filename, Settings.CACHE_PATH)
            self.updateWindow(reset=True)
        self.window.ui.pdfBtn.clicked.connect(uploadPDF)
    
    def bindOcrBtn(self):
        """
        OCR识别按钮绑定事件
        """
        def updateMessageBox(index, recognition):
            # 更新提示框进度
            self.message_box.updateValue(index, self.page_num)
            # 更新识别结果
            self.recognitions[index] = json.loads(recognition)
            if index == self.page_num-1:
                self.message_box.close()
                self.updateWindow()

        def ocr():
            self.window.thread = OCRThread()
            self.window.thread.signal.connect(lambda x, y: updateMessageBox(x, y))
            self.window.thread.start()
            self.message_box.exec_()
        self.window.ui.ocrBtn.clicked.connect(ocr)
    
    def bindScreenshotBtn(self):
        """
        截屏按钮绑定事件
        """
        def scrennshot():
            self.window.showMinimized()
            self.screenshot_widget.start()
        self.window.ui.screenshotBtn.clicked.connect(scrennshot)
        self.screenshot_widget.toolbar.signal.connect(lambda: self.updateWindow(reset=True))

    def bindLastPageBtn(self):
        """
        上一页按钮绑定事件
        """
        def lastPage():
            self.page_index = max(0, self.page_index-1)
            self.updateWindow()
        self.window.ui.lastPageBtn.clicked.connect(lastPage)

    def bindNextPageBtn(self):
        """
        下一页按钮绑定事件
        """
        def nextPage():
            self.page_index = min(self.page_index+1, self.page_num)
            self.updateWindow()
        self.window.ui.nextPageBtn.clicked.connect(nextPage)
   
    def updateWindow(self, reset=False):
        """
        更新界面信息
        """
        # 重置参数
        if reset:
            self.page_index = 0
            self.recognitions = {}
            self.message_box.updateValue(0, 0)
        # 获取缓存路径下的图片路径
        cache_path = Settings.CACHE_PATH
        filenames = sorted(os.listdir(cache_path))
        # 设定图片个数
        if len(filenames) > 0:
            self.page_num = len(filenames)
        # 更新页码
        self.window.ui.pageLabel.setText("%d/%d"%(self.page_index+1, self.page_num))
        # 更新图片和识别结果
        recognition = self.recognitions.get(self.page_index, [])
        if self.page_index < self.page_num :
            image_path = os.path.join(cache_path, filenames[self.page_index])
            self.window.source_view_funcs.updateView(image_path, recognition)
        if self.page_index < len(self.recognitions):
            self.window.result_view_funcs.updateText(recognition)
        # 更新按钮是否可用
        if self.page_index == 0:
            self.window.ui.lastPageBtn.setEnabled(False)
        else:
            self.window.ui.lastPageBtn.setEnabled(True)
        if self.page_index == self.page_num-1:
            self.window.ui.nextPageBtn.setEnabled(False)
        else:
            self.window.ui.nextPageBtn.setEnabled(True)
        if self.window.isMinimized():
            self.window.showNormal()