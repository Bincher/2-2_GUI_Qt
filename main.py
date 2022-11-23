from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class MainFrame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.x, self.y = None, None

    def setupUi(self):
        self.setWindowTitle('Main')
        self.setFixedSize(1280, 720)
        self.resize(1280, 720)
        #self.setStyleSheet('background-color : black')
        #self.setMouseTracking(True) #드래깅 없이도 마우스 움직임 이벤트 발생

        #self.btnClick = QtWidgets.QPushButton('Click', self)
        #self.btnClick.setGeometry(3, 3, 200, 100)
        #self.btnClick.clicked.connect(self.btnClick_clicked)
        #self.show()

        """
        self.canvas = Canvas(self)
        self.canvas.setGeometry(0, 300, self.width(), self.height() - 300)
        self.canvas.setStyleSheet('background-color : white;')
        self.canvas.show()

        self.canvas.mousePressEvent = self.canvas_mousePressEvent
        """
        """
        self.canvas = QtWidgets.QLabel(self)
        self.canvas.setGeometry(0,300,self.width(),self.height()-300)
        self.canvas.setStyleSheet('background-color : white;')
        self.canvas.show()
        self.pixmap = QtGui.QPixmap(self.canvas.width(), self.canvas.height())
        self.pixmap.fill(Qt.white)
        self.canvas.setPixmap(self.pixmap)
        self.canvas.mousePressEvent = self.canvas_mousePressEvent
        """
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.setContentsMargins(10,10,10,10)
        self.setLayout(mainLayout)
        """
        topLabel = QtWidgets.QLabel()
        topLabel.setStyleSheet('background-color : drakgray')
        bottomLabel = QtWidgets.QLabel()
        bottomLabel.setStyleSheet('background-color:white;border:2px solid lightgray;')

        self.bottomLabel = QtWidgets.QLabel()
        self.bottomLabel.setStyleSheet('background-color: white;')
        self.bottomLabel.paintEvent = self.bottomLabel_paintEvent
        self.bottomLabel.mousePressEvent = self.bottomLabel_mousePressEvent
        """
        """
        topWidget = QtWidgets.QWidget()
        topWidget.setStyleSheet('background-color : drakgray')
        bottomWidget = QtWidgets.QStatusBar()
        #bottomLabel.setStyleSheet('background-color:darkgray;')
        bottomWidget.showMessage('Ready')

        mainLayout.addWidget(topWidget)
        #mainLayout.addWidget(self.bottomLabel)
        mainLayout.addWidget(bottomWidget)

        mainLayout.setStretchFactor(topWidget, 1)
        mainLayout.setStretchFactor(bottomWidget, 0)
        """

        topLayout = QtWidgets.QHBoxLayout()
        midWidget = QtWidgets.QWidget()
        statusBar = QtWidgets.QStatusBar()
        statusBar.showMessage('statusBar')
        midWidget.setStyleSheet('background-color:darkgray')

        mainLayout.addLayout(topLayout)
        # mainLayout.addWidget(self.bottomLabel)
        mainLayout.addWidget(midWidget)
        mainLayout.addWidget(statusBar)

        mainLayout.setStretchFactor(topLayout, 0)
        mainLayout.setStretchFactor(midWidget, 1)
        mainLayout.setStretchFactor(statusBar, 0)

        iconLabel = ClickLabel()
        pixmap = QtGui.QPixmap("C:\\Users\\seongbin\\Downloads\\Martz90-Circle-Books.ico").scaled(32,32)
        iconLabel.setPixmap(pixmap)
        topLayout.addWidget(iconLabel)
        topLayout.addStrut(1)
        #topLayout.addStretch(1)

        iconAction = QtWidgets.QAction()
        iconLabel.action = iconAction
        iconAction.triggered.connect(self.iconLabel_Triggered)

        midWidget.mouseMoveEvent = self.midWidget_mouseMoveEvent
        midWidget.paintEvent = self.midWidget_paintEvent

        self.midWidget = midWidget
        self.midWidget.setMouseTracking(True)
        self.statusBar = statusBar

    def iconLabel_Triggered(self):
        print("action triggered")

    def midWidget_mouseMoveEvent(self,e):
        self.x = e.x()
        self.y = e.y()
        self.statusBar.showMessage('{} {}'.format(self.x, self.y))
        self.midWidget.update()

    def midWidget_paintEvent(self, e):
        if self.x is None:
            return

        qp = QtGui.QPainter()
        qp.begin(self.midWidget)
        qp.drawLine(0,0,self.x,self.y)
        qp.end()


    """
    def bottomLabel_paintEvent(self,e):
        if self.x is None:
            return

        qp = QtGui.QPainter()
        qp.begin(self.bottomLabel)
        qp.drawLine(0,0,self.x, self.y)
        qp.end()

    def bottomLabel_mousePressEvent(self,e ):
        self.x = e.x()
        self.y = e.y()
        self.bottomLabel.update()
    """
    """
    def canvas_mousePressEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self.canvas.pixmap())
        qp.drawLine(0, 0, e.x(), e.y())
        qp.end()

        self.canvas.update()
    """
    """
    def mouseMoveEvent(self, e):
        print(e.globalX(), e.globalY(), e.x(), e.y())
        return None
    """
    """
    def mousePressEvent(self, e):
        if e.button() == Qt.RightButton:
            print('RIGHT-Press at', e.globalX(), e.globalY(), e.x(), e.y())
        if e.button() == Qt.LeftButton:
            print('LEFT-Press at', e.globalX(), e.globalY(), e.x(), e.y())
        self.x = e.x()
        self.y = e.y()
        self.update()
    """
    """
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.RightButton:
            print('RIGHT-Release at', e.globalX(), e.globalY(), e.x(), e.y())
        if e.button() == Qt.LeftButton:
            print('LEFT-Release at', e.globalX(), e.globalY(), e.x(), e.y())
    """
    """
    def btnClick_clicked(self):
        QtWidgets.QMessageBox.about(self, 'Main', 'exit')
        app.exit()
    """
    """
    def keyPressEvent(self, e):
        print(e.key(), e.text())
        if e.key() == Qt.Key_Return:
            print("enter key")
        if e.modifiers() & Qt.CTRL:
            print('ctrl key')
    """
    """
    def paintEvent(self, e):
        if self.x == None:
            return

        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawLine(0,0,self.x, self.y)
        pos = '{0:04d} {1:04d}'.format(self.x, self.y)
        qp.drawText(0,32,pos)
        qp.end()
        self.update()
    """
"""
class Canvas(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setupUi()

    def setupUi(self):
        pixmap = QtGui.QPixmap(self.width(), self.height())
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)
"""

class ClickLabel(QtWidgets.QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        self.action.triggered.emit()

    def mouseMoveEvent(self, event):
        pass

app = QtWidgets.QApplication([])
MainFrame = MainFrame()
MainFrame.show()
app.exec_()
