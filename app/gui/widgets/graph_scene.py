"""
作者: LoresDing
版本: v2.0.0
时间: 2023/03/22
图元管理widget,用于展示识别来源
"""
import random
from settings import Settings
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsItem, QGraphicsPolygonItem, QStyle
from PySide6.QtGui import QPixmap, QPolygon, QPen, QColor
from PySide6.QtCore import QPoint

class GraphScene(QGraphicsScene):
    """
    图像管理场景
    """
    def __init__(self):
        super().__init__()

class GraphicsPolygonItem(QGraphicsPolygonItem):
    """
    框图元
    """
    def __init__(self, points, index, parent, window):
        super().__init__()
        # 识别结果的id
        self.index = index
        self.window = window
        self.color = random.choices(Settings.BOX_COLORS)[0]
        self.points = points
        self.setPen(QPen(QColor(*self.color), 1))
        # 画框
        self.polygon = QPolygon()
        for point in points:
            self.polygon.append(QPoint(point[0], point[1]))
        self.setPolygon(self.polygon)
        # 设置可以选择
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        parent.addItem(self)

    def paint(self, painter, option, widget):
        # 设置选中样式
        if self.isSelected():
            painter.setBrush(QColor(*self.color, 127))
            painter.setPen(QPen(QColor(*self.color), 1))
            painter.drawPolygon(self.polygon)
            # 取消默认的虚线
            option.state = QStyle.State_None
            self.window.ui.listWidget.setCurrentRow(self.index)
            # self.signal.emit(self.index)
        super().paint(painter, option, widget)
    
class GraphicsImageItem(QGraphicsPixmapItem):
    """
    照片图源
    """
    def __init__(self, path, parent):
        super().__init__()
        self.pix = QPixmap(path)
        # 设置图元
        self.setPixmap(self.pix)
        # 加入图元
        parent.addItem(self)