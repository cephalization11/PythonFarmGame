'''
Created on 22-05-2012

@author: orneo1212
'''

class Widget:
    '''
    Widget for gui
    '''


    def __init__(self, (width, height)):
        self.width = width
        self.height = height
        self.size = [self.width, self.height]
        self.visible = True
        self.callbacks = {}  # key=signal name value= function

    def redraw(self, surface):
        pass

    def update(self):
        pass

    def poll_event(self, event):
        pass

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True

    def connect(self, signal, function):
        self.callbacks[signal] = function
