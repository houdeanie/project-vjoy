from PySide2 import QtGui, QtCore, QtWidgets
import time
import cv2
from lambda_runner import LambdaRunner

class PreviewWidget(QtWidgets.QLabel):
    def __init__(self, parent, preview, thread_pool):
        super().__init__(parent=parent)
        self.preview = preview
        self.thread_pool = thread_pool

        self.colour_map = {
            "characters":   (255, 0, 0),
            "bonuses":      (0, 255, 0),
            "values":       (0, 0, 255),
        }

        self.panning = False
        self._last_position = QtCore.QPoint(0, 0)

        @LambdaRunner
        def start_runner():
            while parent.is_running:
                self.update()
                time.sleep(25 / 1000)

        self.thread_pool.start(start_runner)
    
    def update(self):
        preview = self.preview.take_screenshot()
        preview = preview.copy()
        
        # for key, bounding_boxes in self.preview.bounding_boxes.items():
        #     colour = self.colour_map.get(key, (255, 0, 0))
        #     for bounding_box in bounding_boxes:
        #         left, top, right, bottom = bounding_box
        #         cv2.rectangle(preview, (left, top), (right, bottom), colour)
                
        # display
        height, width, channel = preview.shape
        bytes_per_line = width * 3
        image = cv2.cvtColor(preview, cv2.COLOR_BGR2RGB)
        self.qt_image = QtGui.QImage(image.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        self.setPixmap(QtGui.QPixmap.fromImage(self.qt_image))
    
    # def mousePressEvent(self, ev):
    #     if ev.button() == QtCore.Qt.MidButton:
    #         self.panning = True
    #         self._last_position = ev.pos()
    #     return super().mousePressEvent(ev)
    
    # def mouseReleaseEvent(self, ev):
    #     if ev.button() == QtCore.Qt.MidButton:
    #         self.panning = False
    #     return super().mouseReleaseEvent(ev)
    
    # def mouseMoveEvent(self, ev):
    #     if self.panning:
    #         delta = self._last_position-ev.pos()
    #         self._last_position = ev.pos()
    #         self.preview.screen_rect.set_left(delta.x() + self.preview.screen_rect.left)
    #         self.preview.screen_rect.set_top(delta.y() + self.preview.screen_rect.top)
    #     return super().mouseMoveEvent(ev)
