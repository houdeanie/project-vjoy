from PySide2.QtCore import QObject, Signal, Property, Slot

class ScreenRect(QObject):
    left_changed = Signal(int)
    top_changed = Signal(int)
    width_changed = Signal(int)
    height_changed = Signal(int)

    def __init__(self):
        super().__init__()
        self.set_left(0)
        self.set_top(0)
        self.set_width(1920)
        self.set_height(1080)

    @Property(int, notify=left_changed)
    def left(self):
        return self._left

    @Slot(int)    
    def set_left(self, left):
        self._left = left
        self.left_changed.emit(left)

    @Property(int, notify=top_changed)
    def top(self):
        return self._top

    @Slot(int)
    def set_top(self, top):
        self._top = top
        self.top_changed.emit(top)

    @Property(int, notify=width_changed)
    def width(self):
        return self._width

    @Slot(int)
    def set_width(self, width):
        self._width = width
        self.width_changed.emit(width)

    @Property(int, notify=height_changed)
    def height(self):
        return self._height

    @Slot(int) 
    def set_height(self, height):
        self._height = height
        self.height_changed.emit(height)