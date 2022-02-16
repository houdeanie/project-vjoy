from PySide2 import QtGui, QtCore, QtWidgets

from preview_widget import PreviewWidget
from preview import Preview
from screen_rect import ScreenRect
from mouse_overlay import Joystick

# from .preview_adjuster_widget import PreviewAdjusterWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # self.app = app
        self.setWindowTitle("Joystick")
        self.is_running = True
        screen_rect = ScreenRect()
        self.preview = Preview(screen_rect)
        self.thread_pool = QtCore.QThreadPool(self)
        
        left_panel = self.create_left_panel()
        preview_widget = PreviewWidget(self, self.preview, self.thread_pool)
        
        main_tab = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(left_panel)
        layout.addWidget(preview_widget)
        main_tab.setLayout(layout)

        tabs = QtWidgets.QTabWidget()
        tabs.addTab(main_tab, "Primary")
        # self.setWindowFlags(
        #     QtCore.Qt.WindowStaysOnTopHint |
        #     QtCore.Qt.FramelessWindowHint |
        #     QtCore.Qt.X11BypassWindowManagerHint
        # )

        # def update_progress_tab(prog):
        #     tabs.setTabText(1, f"Progress ({prog*100:.0f}%)")
        
        # app.tracer.progress_changed.connect(update_progress_tab)
        self.setCentralWidget(tabs)
        self.adjustSize()

    def create_left_panel(self):
        group = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        joystick = Joystick()
        layout.addWidget(joystick)
        group.setLayout(layout)
        return group

    # active threads use app.is_running 
    # use this to stop all threads so app closes properly 
    def closeEvent(self, event):
        self.is_running = False
        return super().closeEvent(event)
