from PySide2 import QtWidgets, QtCore, QtGui
import sys
from enum import Enum
import time

class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class Joystick(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Joystick, self).__init__(parent)
        self.setMinimumSize(500, 500)
        # self.setMouseTracking(True)
        self.movingOffset = QtCore.QPointF(0, 0)
        self.movable = False
        self.__maxDistance = 200
        self.__centerMaxDistance = 30

    def _centerEllipse(self):
        if self.movable:
            return QtCore.QRectF(-10, -10, 20, 20).translated(self.movingOffset)
        return QtCore.QRectF(-10, -10, 20, 20).translated(self._center())
    
    def _outerEllipse(self):
        return QtCore.QRectF(-10, -10, 20, 20).translated(self._center())
    
    def _center(self):
        return QtCore.QPointF(self.width()/2, self.height()/2)
        
    def paintEvent(self, event):
        pointer = QtGui.QPainter(self)
        bounds1 = QtCore.QRectF(-self.__maxDistance, 
            -self.__maxDistance, 
            self.__maxDistance * 2, 
            self.__maxDistance * 2).translated(self._center())
        pointer.drawEllipse(bounds1)
        # pointer.setBrush(QtCore.Qt.transparent)
        pointer.drawEllipse(self._centerEllipse())
        centerBound = QtGui.QPainter(self)
        bounds2 = QtCore.QRectF(-self.__centerMaxDistance, 
            -self.__centerMaxDistance, 
            self.__centerMaxDistance * 2, 
            self.__centerMaxDistance * 2).translated(self._center())
        centerBound.drawEllipse(bounds2)
        # centerBound.setBrush(QtCore.Qt.white)
        centerBound.drawEllipse(self._centerEllipse())

    def _boundJoystick(self, point):
        limitLine = QtCore.QLineF(self._center(), point)
        if (limitLine.length() > self.__maxDistance):
            limitLine.setLength(self.__maxDistance)
        return limitLine.p2()
        
    def _checkInOuterBound(self, pointer): 
        # print(pointer)
        # if pointer in :
        self.movable = True
        return True
        # else:
        #     self.movable = False
        #     return False

    def joystickDirection(self):
        if not self.movable:
            return 0
        normVector = QtCore.QLineF(self._center(), self.movingOffset)
        currentDistance = normVector.length()
        angle = normVector.angle()
        distance = min(currentDistance / self.__maxDistance, 1.0)
        if 45 <= angle < 135:
            return (Direction.Up, distance)
        elif 135 <= angle < 225:
            return (Direction.Left, distance)
        elif 225 <= angle < 315:
            return (Direction.Down, distance)
        return (Direction.Right, distance)
        
    # def mousePressEvent(self, ev):
    #     print(ev.pos())
    #     self.movable = self._centerEllipse().contains(ev.pos())
    #     return super().mousePressEvent(ev)

    # def mouseReleaseEvent(self, event):
    #     self.movable = False
    #     self.movingOffset = QtCore.QPointF(0, 0)
    #     self.update()

    def mouseMoveEvent(self, event):
        # if self._centerEllipse().contains(event.pos()):
        if self._checkInOuterBound(event.pos()):
            print("Moving")
            self.movingOffset = self._boundJoystick(event.pos())
            self.update()
            print(self.joystickDirection())
        return super().mouseMoveEvent(event)
        
if __name__ == '__main__':
    # Create main application window
    app = QtWidgets.QApplication([])
    app.setStyle(QtWidgets.QStyleFactory.create("Cleanlooks"))
    mw = QtWidgets.QMainWindow()
    mw.setWindowTitle('Joystick example')

    # Create and set widget layout
    # Main widget container
    cw = QtWidgets.QWidget()
    ml = QtWidgets.QGridLayout()
    cw.setLayout(ml)
    mw.setCentralWidget(cw)

    # Create joystick 
    joystick = Joystick()
    joystick.setAutoFillBackground(True)

    # ml.addLayout(joystick.get_joystick_layout(),0,0)
    ml.addWidget(joystick,0,0)
    mw.show()

    ## Start Qt event loop unless running in interactive mode or using pyside.
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()

# # importing libraries
# # from PyQt5.QtWidgets import * 
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtGui import * 
# from PyQt5.QtCore import * 
# import sys

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # setting title
#         self.setWindowTitle("Python ")
#         # setting geometry
#         self.setGeometry(100, 100, 600, 400)
#         # calling method
#         self.UiComponents()
#         # showing all the widgets
#         self.show()
  
#     # method for widgets
#     def UiComponents(self):
#         # creating a check-able combo box object
#         self.combo_box = QComboBox(self)
#         # setting geometry of combo box
#         self.combo_box.setGeometry(200, 150, 100, 30)
#         # geek list
#         geek_list = ["Sayian", "Super Sayian", "Super Sayian 2", "Super Sayian B"]
#         # adding list of items to combo box
#         self.combo_box.addItems(geek_list)
#         # setting stylesheet of the combo box
#         self.combo_box.setStyleSheet("border : 1px solid red;")
#         # creating label to show label
#         self.label = QLabel(self)
#         # setting geometry to the label
#         self.label.setGeometry(200, 200, 200, 30)
#         # creating a timer object
#         timer = QTimer(self)
#         # adding action to the timer
#         timer.timeout.connect(self.do_something)
#         # starting timer
#         timer.start(100)
  
#     # action called by the timer
#     def do_something(self):
#         # checking if the combo box is under mouse
#         under = self.combo_box.underMouse()
#         # setting text to the label
#         self.label.setText("Under Mouse ? : " + str(under))
  
# # create pyqt5 app
# App = QApplication(sys.argv)
# # create the instance of our Window
# window = Window()
# # start the app
# sys.exit(App.exec())

# import sys
# from PyQt5 import QtWidgets, QtCore, QtGui
# class TranslucentWidgetSignals(QtCore.QObject):
#     # SIGNALS
#     CLOSE = QtCore.pyqtSignal()
# class TranslucentWidget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(TranslucentWidget, self).__init__(parent)
#         # make the window frameless
#         self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
#         self.fillColor = QtGui.QColor(30, 30, 30, 120)
#         self.penColor = QtGui.QColor("#333333")
#         self.popup_fillColor = QtGui.QColor(240, 240, 240, 255)
#         self.popup_penColor = QtGui.QColor(200, 200, 200, 255)
#         self.close_btn = QtWidgets.QPushButton(self)
#         self.close_btn.setText("x")
#         font = QtGui.QFont()
#         font.setPixelSize(18)
#         font.setBold(True)
#         self.close_btn.setFont(font)
#         self.close_btn.setStyleSheet("background-color: rgb(0, 0, 0, 0)")
#         self.close_btn.setFixedSize(30, 30)
#         self.close_btn.clicked.connect(self._onclose)
#         self.SIGNALS = TranslucentWidgetSignals()
#     def resizeEvent(self, event):
#         s = self.size()
#         popup_width = 300
#         popup_height = 120
#         ow = int(s.width() / 2 - popup_width / 2)
#         oh = int(s.height() / 2 - popup_height / 2)
#         self.close_btn.move(ow + 265, oh + 5)
#     def paintEvent(self, event):
#         # This method is, in practice, drawing the contents of
#         # your window.
#         # get current window size
#         s = self.size()
#         qp = QtGui.QPainter()
#         qp.begin(self)
#         qp.setRenderHint(QtGui.QPainter.Antialiasing, True)
#         qp.setPen(self.penColor)
#         qp.setBrush(self.fillColor)
#         qp.drawRect(0, 0, s.width(), s.height())
#         # drawpopup
#         qp.setPen(self.popup_penColor)
#         qp.setBrush(self.popup_fillColor)
#         popup_width = 300
#         popup_height = 120
#         ow = int(s.width()/2-popup_width/2)
#         oh = int(s.height()/2-popup_height/2)
#         qp.drawRoundedRect(ow, oh, popup_width, popup_height, 5, 5)
#         font = QtGui.QFont()
#         font.setPixelSize(18)
#         font.setBold(True)
#         qp.setFont(font)
#         qp.setPen(QtGui.QColor(70, 70, 70))
#         tolw, tolh = 80, -5
#         qp.drawText(ow + int(popup_width/2) - tolw, oh + int(popup_height/2) - tolh, "Yep, I'm a pop up.")
#         qp.end()
#     def _onclose(self):
#         print("Close")
#         self.SIGNALS.CLOSE.emit()


# class ParentWidget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(ParentWidget, self).__init__(parent)
#         self._popup = QtWidgets.QPushButton("Gimme Popup!!!")
#         self._popup.setFixedSize(150, 40)
#         self._popup.clicked.connect(self._onpopup)
#         self._other1 = QtWidgets.QPushButton("A button")
#         self._other2 = QtWidgets.QPushButton("A button")
#         self._other3 = QtWidgets.QPushButton("A button")
#         self._other4 = QtWidgets.QPushButton("A button")
#         hbox = QtWidgets.QHBoxLayout()
#         hbox.addWidget(self._popup)
#         hbox.addWidget(self._other1)
#         hbox.addWidget(self._other2)
#         hbox.addWidget(self._other3)
#         hbox.addWidget(self._other4)
#         self.setLayout(hbox)
#         self._popframe = None
#         self._popflag = False
#     def resizeEvent(self, event):
#         if self._popflag:
#             self._popframe.move(0, 0)
#             self._popframe.resize(self.width(), self.height())
#     def _onpopup(self):
#         self._popframe = TranslucentWidget(self)
#         self._popframe.move(0, 0)
#         self._popframe.resize(self.width(), self.height())
#         self._popframe.SIGNALS.CLOSE.connect(self._closepopup)
#         self._popflag = True
#         self._popframe.show()
#     def _closepopup(self):
#         self._popframe.close()
#         self._popflag = False

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     main = ParentWidget()
#     main.resize(500, 500)
#     main.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5 import QtWidgets, QtCore
# app = QtWidgets.QApplication(sys.argv)
# # create invisble widget
# window = QtWidgets.QWidget()
# window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
# window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
# window.setFixedSize(800, 600)

# # add visible child widget, when this widget is transparent it will also be invisible
# visible_child = QtWidgets.QWidget(window)
# visible_child.setStyleSheet('QWidget{background-color: white}')
# visible_child.setObjectName('vc')
# visible_child.setFixedSize(800, 600)
# layout = QtWidgets.QGridLayout()

# # add a close button
# close_button = QtWidgets.QPushButton()
# close_button.setText('close window')
# close_button.clicked.connect(lambda: app.exit(0))
# layout.addWidget(close_button)

# # add a button that makes the visible child widget transparent
# change_size_button = QtWidgets.QPushButton()
# change_size_button.setText('change size')
# change_size_button.clicked.connect(lambda: visible_child.setStyleSheet('QWidget#vc{background-color: transparent}'))
# layout.addWidget(change_size_button)

# visible_child.setLayout(layout)
# window.show()
# app.exec()

# import sys

# from PyQt5 import QtGui, QtCore, uic
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QApplication


# class MainWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.setWindowFlags(
#             QtCore.Qt.WindowStaysOnTopHint |
#             QtCore.Qt.FramelessWindowHint |
#             QtCore.Qt.X11BypassWindowManagerHint
#         )
#         self.setGeometry(
#             QtWidgets.QStyle.alignedRect(
#                 QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
#                 QtCore.QSize(220, 32),
#                 QtWidgets.qApp.desktop().availableGeometry()
#         ))

#     def mousePressEvent(self, event):
#         QtWidgets.qApp.quit()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mywindow = MainWindow()
#     mywindow.show()
#     app.exec_()