"""
OCR界面元素绑定的函数集合
作者: LoresDing
时间: 2023/03/20
"""
import os
import shutil
from PIL import Image
from modules import *
from widgets import *
from .screenshot import ScreenshotWidget
from .message_box import OCRMessageBox
from .core import get_images_from_pdf
from .threads import OCRThread

class OCRFunctions:
    """
    OCR界面的信号槽绑定函数
    """
    PAGE_INDEX = 0
    PAGE_NUM = 1
    OCR_RESULT = {}
    @staticmethod
    def screenshot(window):
        """
        截图
        """
        window.showMinimized()
        window.ui.screenshot_widget.start()

    @staticmethod
    def ocr(window):
        """
        文字识别
        """
        window.thread = OCRThread()
        window.thread.signal.connect(lambda x, y: OCRFunctions.update_message_result(window, x, y))
        window.thread.start()
        window.ui.message_box.exec_()

    @staticmethod
    def update_message_result(window, index, lines):
        """
        更新提示消息框内容和识别结果
        """
        # 更新提示框进度
        window.ui.message_box.update_value(index, OCRFunctions.PAGE_NUM)
        # 更新识别结果
        OCRFunctions.OCR_RESULT[index] = lines
        if index == OCRFunctions.PAGE_NUM-1:
            window.ui.message_box.close()
            OCRFunctions.update(window)

    @staticmethod
    def upload_image(window):
        """
        上传图片
        """
        # 对话框选择图片
        filenames, _ = QFileDialog.getOpenFileNames(window, "选择图片文件", "C://", "图片 (*.png *.jpg *.PNG *.JPG)")
        if len(filenames) > 0:
            # 清空缓存路径
            cache_path = Settings.CACHE_PATH
            if os.path.exists(cache_path):
                shutil.rmtree(cache_path)
            os.makedirs(cache_path, exist_ok=True)
            # 拷贝文件
            for filename in filenames:
                temp = Image.open(filename)
                prefix, _ = os.path.splitext(os.path.basename(filename))
                new_filename = os.path.join(cache_path, prefix + ".png")
                temp.save(new_filename)
            # 更新界面
            OCRFunctions.update(window, reset=True)

    @staticmethod
    def upload_pdf(window):
        """
        上传pdf
        """
        # 对话框选择图片
        filename, _ = QFileDialog.getOpenFileName(window, "选择PDF文件", "C://", "PDF (*.pdf)")
        if filename:
            # 从选择的文件获取图片
            get_images_from_pdf(filename, Settings.CACHE_PATH)
            # 更新界面
            OCRFunctions.update(window, reset=True)

    @staticmethod
    def next_page(window):
        """
        下一页
        """
        OCRFunctions.PAGE_INDEX = min(OCRFunctions.PAGE_NUM-1, OCRFunctions.PAGE_INDEX+1)
        # 更新界面
        OCRFunctions.update(window)
    
    @staticmethod
    def last_page(window):
        """
        上一页
        """
        OCRFunctions.PAGE_INDEX = max(0, OCRFunctions.PAGE_INDEX-1)
        # 更新界面
        OCRFunctions.update(window)
    
    @staticmethod
    def update(window, reset=False):
        """
        更新界面信息
        """
        # 需要重置结果
        if reset:
            OCRFunctions.OCR_RESULT = {}
            OCRFunctions.PAGE_INDEX = 0
            window.ui.message_box.update_value(0, 0)
        cache_path = Settings.CACHE_PATH
        filenames = sorted(os.listdir(cache_path))
        if len(filenames) > 0:
            OCRFunctions.PAGE_NUM = len(filenames)
        page_index = OCRFunctions.PAGE_INDEX
        page_num = OCRFunctions.PAGE_NUM
        ocr_result = OCRFunctions.OCR_RESULT
        # 更新页码
        window.ui.label_page.setText("%d/%d"%(page_index+1, page_num))
        # 更新图片
        if page_index < len(filenames):
            window.ui.label_image.setPixmap(QPixmap(os.path.join(cache_path, filenames[page_index])))
        else:
            window.ui.label_image.setText("暂无图片展示")
        # 更新识别结果
        if page_index < len(ocr_result):
            window.ui.edit_result.setText(ocr_result[page_index])
        else:
            window.ui.edit_result.setText("暂无识别结果, 请按<识别>按钮进行OCR识别.")
        # 更新按钮是否可用
        if page_index == 0:
            window.ui.btn_last.setEnabled(False)
        else:
            window.ui.btn_last.setEnabled(True)
        if page_index == page_num-1:
            window.ui.btn_next.setEnabled(False)
        else:
            window.ui.btn_next.setEnabled(True)
        if window.isMinimized():
            window.showNormal()
        window.update()
        
    @staticmethod
    def binding(window):
        """
        文件转换界面的信号槽
        """
        # 截屏widget
        window.ui.screenshot_widget = ScreenshotWidget()
        # 截屏工具栏确认按钮
        window.ui.screenshot_widget.toolbar.signal.connect(lambda: OCRFunctions.update(window, reset=True))
        # 消息提示框
        window.ui.message_box = OCRMessageBox(window)
        # 截屏软件
        window.ui.btn_screen.clicked.connect(lambda: OCRFunctions.screenshot(window))
        # ocr识别软件
        window.ui.btn_ocr.clicked.connect(lambda: OCRFunctions.ocr(window))
        # 上传图片按钮
        window.ui.btn_upload_image.clicked.connect(lambda: OCRFunctions.upload_image(window))
        # 上传PDF按钮
        window.ui.btn_upload_pdf.clicked.connect(lambda: OCRFunctions.upload_pdf(window))
        # 下一页
        window.ui.btn_next.clicked.connect(lambda: OCRFunctions.next_page(window))
        # 上一页
        window.ui.btn_last.clicked.connect(lambda: OCRFunctions.last_page(window))


        



