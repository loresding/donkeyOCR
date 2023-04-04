"""
作者: LoresDing
版本: v2.0.0
时间: 2023/03/22
用于绑定识别来源图片展示
"""
import math
from PySide6.QtCore import Qt
from gui.widgets import GraphScene, GraphicsImageItem, GraphicsPolygonItem

class SourceViewFunctions:
    """
    图像、识别结果显示事件
    """
    def __init__(self, window):
        self.window = window
        self.scene = GraphScene()
        # 设置view可以进行鼠标的拖拽选择
        self.window.ui.sourceView.setDragMode(self.window.ui.sourceView.ScrollHandDrag)
        #隐藏滑动条
        self.window.ui.sourceView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #隐藏滑动条
        self.window.ui.sourceView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 绑定场景
        self.window.ui.sourceView.setScene(self.scene)
        # 重新设定滑轮滚动事件，实现缩放
        self.resetWheelEvent()

    def updateView(self, path, recognitions):
        """
        更新图片和识别信息
        """
        # 清空当前所有图元
        self.scene.clear()
        # 添加图片
        GraphicsImageItem(path, self.scene)
        # 添加框
        for index, item in enumerate(recognitions):
            GraphicsPolygonItem(item["position"], index, self.scene, self.window)
    
    def resetWheelEvent(self):
        """
        滑轮滚动绑定事件
        """
        def wheelEvent(event):
            factor = math.pow(2.0, -event.angleDelta().y() / 240.0)
            self.window.ui.sourceView.scale(factor, factor)
        self.window.ui.sourceView.wheelEvent = wheelEvent



