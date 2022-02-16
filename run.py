from PySide2 import QtGui, QtCore, QtWidgets
import argparse
import sys
import yaml
import os

from app import App
from main_window import MainWindow

def main():
    app = App()
    qt_app = QtWidgets.QApplication([])
    qt_app.setStyle("fusion")
    # window = MainWindow(app)
    window = MainWindow()

    window.show()
    return qt_app.exec_()

if __name__ == '__main__':
    sys.exit(main())