from vjoy import *
import numpy as np
import math

def norm_clip( func):
    def wrapped(self, x):
        return func(self, np.clip(x, 0, 1))
    return wrapped

class Controller:
    def __init__(self, rid):
        self.rid = rid
        if not VJoy.AcquireVJD(self.rid):
            pid = VJoy.GetOwnerPid(self.rid)
            raise IOError(f"vjoy {rid} in use by pid {pid}")

        self.max_x = VJoy.GetVJDAxisMax(rid, HID_USAGE_X)
        self.max_y = VJoy.GetVJDAxisMax(rid, HID_USAGE_Y)
        self.max_z = VJoy.GetVJDAxisMax(rid, HID_USAGE_Z)
        self.max_rx = VJoy.GetVJDAxisMax(rid, HID_USAGE_RX)
        self.max_ry = VJoy.GetVJDAxisMax(rid, HID_USAGE_RY)
        self.max_rz = VJoy.GetVJDAxisMax(rid, HID_USAGE_RZ)
        self.max_btns = VJoy.GetVJDButtonNumber(rid)
        self.max_sl0 = VJoy.GetVJDAxisMax(rid, HID_USAGE_SL0)
        self.max_sl1 = VJoy.GetVJDAxisMax(rid, HID_USAGE_SL1)
        self.max_pov = 0x8C40

        self.reset()
    
    def reset(self):
        pdata = JOYSTICK_POSITION()
        pdata.wAxisX = self.max_x >> 1
        pdata.wAxisY = self.max_y >> 1
        pdata.wAxisZ = self.max_z >> 1
        pdata.wAxisXRot = self.max_rx >> 1
        pdata.wAxisYRot = self.max_ry >> 1
        pdata.wAxisZRot = self.max_rz >> 1

        pdata.wSL0 = self.max_sl0 >> 1
        pdata.wSL1 = self.max_sl1 >> 1
        pdata.lButtons = 0x00000000
        pdata.bHats = self.max_pov 
        self.pdata = pdata
        self.update()
    
    def update(self):
        return VJoy.UpdateVJD(self.rid, self.pdata)

    @norm_clip
    def set_x(self, x):
        self.pdata.wAxisX = math.floor(self.max_x*x)
        self.update()

    @norm_clip
    def set_y(self, y):
        self.pdata.wAxisY = math.floor(self.max_y*y)
        self.update()

    @norm_clip
    def set_z(self, z):
        self.pdata.wAxisZ = math.floor(self.max_z*z)
        self.update()

    @norm_clip
    def set_rx(self, rx):
        self.pdata.wAxisXRot = math.floor(self.max_rx*rx)
        self.update()

    @norm_clip
    def set_ry(self, ry):
        self.pdata.wAxisYRot = math.floor(self.max_ry*ry)
        self.update()

    @norm_clip
    def set_rz(self, rz):
        self.pdata.wAxisZRot = math.floor(self.max_rz*rz)
        self.update()
    
    @norm_clip
    def set_slider_0(self, v):
        self.pdata.wSL0 = math.floor(self.max_sl0*v)
        self.update()

    @norm_clip
    def set_slider_1(self, v):
        self.pdata.wSL1 = math.floor(self.max_sl1*v)
        self.update()

    def set_button(self, btn, state):
        if btn <= 0 or btn > self.max_btns:
            raise ValueError(f"Invalid button {btn}")

        if state:
            self.pdata.lButtons |= 1 << (btn-1)
        else:
            self.pdata.lButtons &= ~(1 << (btn-1))
        self.update()
    
    def on_button_press(self, btn):
        self.set_button(btn, True)
    
    def on_button_release(self, btn):
        self.set_button(btn, False)

# from vjoy import *
# import time
# from threading import Thread
# import numpy as np
# RID = 1
# def main():
#     if not VJoy.AcquireVJD(RID):
#         pid = VJoy.GetOwnerPid(RID)
#         print(f"VJoy already used by {pid}")
#         return
#     min_x, max_x = VJoy.GetVJDAxisMin(RID, HID_USAGE_X), VJoy.GetVJDAxisMax(RID, HID_USAGE_Y)
#     dt = 0.01
#     speed = int((max_x-min_x) * dt)
#     scale = 5
#     sspeed = scale * speed
#     running = True
#     VJoy.ResetVJD(RID)
#     print(VJoy.GetVJDStatus(RID))
#     max_axis = HID_USAGE_X
#     for axis in range(HID_USAGE_X, HID_USAGE_POV+1):
#         if VJoy.GetVJDAxisExist(RID, axis):
#             max_axis = axis
#         else:
#             break
#     def axis_test():
#         axis_range = list(range(min_x, max_x, sspeed))
#         axis_spread = axis_range + axis_range[::-1]
#         while running:
#             for val in axis_spread:
#                 for axis in range(HID_USAGE_X, max_axis+1):
#                     VJoy.SetAxis(val, RID, axis)
#                 time.sleep(0.01)
#     def pov_test():
#         while running:
#             #VJoy.SetContPov()
#             break
#     def button_test():
#         while running:
#             n = VJoy.GetVJDButtonNumber(1)
#             states = np.random.rand(n) > 0.5
#             for i, state in enumerate(states):
#                 bid = i+1
#                 VJoy.SetBtn(state, RID, bid)
#             time.sleep(0.2)
#     t1 = Thread(target=axis_test)
#     t2 = Thread(target=button_test)
#     t1.start()
#     t2.start()
#     try:
#         while True:
#             time.sleep(0.1)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         running = False
#         t1.join()
#         t2.join()


# if __name__ == '__main__':
#     main()

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