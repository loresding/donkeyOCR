"""
截屏操作，来源于@ardeas https://blog.csdn.net/u010501845/article/details/124931326 adeas
作者: LoresDing
时间: 2023/03/20
用于识别截图widget
"""
import os
import shutil
from settings import Settings
from PySide6.QtWidgets import QToolBar, QApplication, QWidget
from PySide6.QtCore import Qt, QPoint, QRect, QRectF, QPointF, QSizeF, Signal
from PySide6.QtGui import QIcon, QAction, QPainter, QPen, QPalette, QBrush

class ScreenshotToolBar(QToolBar):
    """
    截图工具条
    """
    signal = Signal()
    def __init__(self, widget):
        super().__init__(widget)
        self.widget = widget
        # 是否编辑状态
        self.is_draw_flag = True
        # 设置文字在图标旁
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        # 设置样式
        self.setStyleSheet('''
            QToolBar {border-radius: 5px;padding: 3px;background-color: black;}
            ''')
        # 默认移动到屏幕顶部居中位置
        desktop = QApplication.primaryScreen().size()
        top_center_point = QPoint(desktop.width()*0.5, 0)
        self.move(top_center_point)
        # 默认的按钮样式
        self._style_normal = "QToolBar QToolButton{color: white;}"
        # 选择后的按钮样式，悬停样式一样
        self._style_selected = "QToolBar QToolButton{color: black;background-color: rgb(189, 147, 249)}"
        # 确定按钮
        self._at_comfirm = QAction(QIcon(r"images/icons/cil-check-circle.png"), '确定', self, triggered=self.comfirm)
        self.addAction(self._at_comfirm)
        # 分割线
        self.addSeparator()
        # 退出按钮
        self._at_exit = QAction(QIcon(r"images/icons/cil-account-logout.png"), '退出', self, triggered=self.exit)
        self.addAction(self._at_exit)
        # 绑定事件方法
        self.actionTriggered.connect(self.onActionTriggered)
        # 所有的action
        self.actions = [self._at_exit, self._at_comfirm]
        # 初始化样式
        self.init()
        # 画图的矩阵坐标
        self.rect_top = None
        self.rect_left = None
        self.rect_bottom = None
        self.rect_right = None

    def init(self):
        """
        初始化action的样式
        """
        self.is_draw_flag = True
        for at in self.actions:
            self.widgetForAction(at).setStyleSheet(self._style_normal)

    def exit(self):
        """
        退出事件
        """
        self.is_draw_flag = False
        self.widget.close()
        self.signal.emit()

    def comfirm(self):
        """
        确认截图
        """
        # 清空缓存文件
        cache_path = Settings.CACHE_PATH
        shutil.rmtree(cache_path)
        os.makedirs(cache_path)
        # 截图并存入缓存文件
        image = self.widget._screen_pixmap.toImage()
        rect = QRect(self.rect_left, self.rect_top, self.rect_right-self.rect_left, self.rect_bottom-self.rect_top)
        image = image.copy(rect)
        save_path = os.path.join(cache_path, "1.png")
        image.save(save_path, "PNG", 100)
        # 信号
        self.signal.emit()
        # 退出
        self.exit()
    
    def onActionTriggered(self, action):
        """
        根据按钮更换样式
        """
        action_text = action.text()
        for at in self.actions:
            if at.text() == action_text:
                self.widgetForAction(at).setStyleSheet(self._style_selected)
            else:
                self.widgetForAction(at).setStyleSheet(self._style_normal)

class ScreenshotWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.toolbar = ScreenshotToolBar(self)
        
        # 鼠标是否移动flag
        self.move_flag = False

    def mousePressEvent(self, event):
        """
        重写mousePressEvent
        """
        if self.toolbar.is_draw_flag:
            self.toolbar.rect_top = event.y()
            self.toolbar.rect_left = event.x()
            self.move_flag = True

    def mouseReleaseEvent(self, event):
        """
        重新mouseReleaseEvent
        """
        if self.toolbar.is_draw_flag:
            self.move_flag = False
            # 进行大小值比较，重新赋值
            if self.toolbar.rect_left > self.toolbar.rect_right:
                self.toolbar.rect_right, self.toolbar.rect_left = self.toolbar.rect_left, self.toolbar.rect_right
            
            if self.toolbar.rect_top > self.toolbar.rect_bottom:
                self.toolbar.rect_top, self.toolbar.rect_bottom = self.toolbar.rect_bottom, self.toolbar.rect_top

    def mouseMoveEvent(self, event):
        """
        重写mouseMoveEvent
        """
        if self.toolbar.is_draw_flag and self.move_flag:
            self.toolbar.rect_bottom = event.y()
            self.toolbar.rect_right = event.x()

            self.update()

    def paintEvent(self, event):
        """
        重写paintEvent
        """
        super().paintEvent(event)
        if self.toolbar.is_draw_flag and self.move_flag:
            rect = QRect(self.toolbar.rect_left, self.toolbar.rect_top, self.toolbar.rect_right - self.toolbar.rect_left, self.toolbar.rect_bottom - self.toolbar.rect_top)
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(rect)
    
    def captureScreen(self):
        """
        截屏
        """
        # 截图整个屏幕
        self._screen_pixmap = QApplication.primaryScreen().grabWindow()
        # 设备像素比
        self._pixel_ratio = self._screen_pixmap.devicePixelRatio()
        # 即当前屏幕显示的大小
        self._rt_screen = QRectF(QPointF(0, 0),
                                QSizeF(self._screen_pixmap.width()/self._pixel_ratio, 
                                       self._screen_pixmap.height() / self._pixel_ratio))
        # 设置 screenPixmap 为窗口背景
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(self._screen_pixmap))
        self.setPalette(palette)
        # 设置widget尺寸
        self.setGeometry(self._rt_screen.toRect())

    def start(self):
        self.toolbar.init()
        self.captureScreen()
        self.showFullScreen()
