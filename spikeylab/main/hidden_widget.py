from PyQt4 import QtGui
from spikeylab.resources.icons import arrowup, arrowdown

class WidgetHider(QtGui.QWidget):   
    def __init__(self, content, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.title = QtGui.QLabel(content.windowTitle())
        self.hideIcon = arrowdown()
        self.showIcon = arrowup()
        self.hideBtn = QtGui.QPushButton('',self)
        self.hideBtn.setIcon(self.showIcon)
        self.hideBtn.setFlat(True)
        self.hideBtn.clicked.connect(self.hide)
        titlebarLayout = QtGui.QHBoxLayout()
        titlebarLayout.setSpacing(0)
        titlebarLayout.setContentsMargins(0,0,0,0)
        titlebarLayout.addWidget(self.title)
        titlebarLayout.addWidget(self.hideBtn)
        titlebarLayout.addStretch(1)

        layout = QtGui.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)

        layout.addLayout(titlebarLayout)
        layout.addWidget(content)

        self.content = content
        content.hide()
        self.setFixedHeight(30)

        self.setLayout(layout)

    def hide(self, event):
        if self.content.isHidden():
            self.content.show()
            self.hideBtn.setIcon(self.hideIcon)
            self.setMaximumHeight(16777215)
        else:
            self.content.hide()
            self.hideBtn.setIcon(self.showIcon)
            self.setFixedHeight(30)
