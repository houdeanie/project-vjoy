from PySide2 import QtCore
from preview import Preview
from screen_rect import ScreenRect

class App(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.is_running = True
        screen_rect = ScreenRect()
        self.preview = Preview(screen_rect)
        self.thread_pool = QtCore.QThreadPool(self)