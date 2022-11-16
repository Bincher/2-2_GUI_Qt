from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

prevX, prevY = None, None

"""
def btnLoad_clicked():
    pixmap = QtGui.QPixmap("images\cat.jpg")
    lbImg.setPixmap(pixmap)
    #lbImg.resize(pixmap.width(), pixmap.height())
"""

def canvas_mouseMoveEvent(e):
    """
    painter = QtGui.QPainter(canvas.pixmap())
    pos = '{0:04d} {1:04d}'.format(e.x(),e.y())

    painter.setPen(Qt.NoPen)
    painter.setBrush(Qt.white)
    painter.drawRect(0,0,9*16,32)

    painter.setPen(Qt.black)
    painter.drawText(0, 32, pos)

    painter.end()
    canvas.update()
    """
    global prevX
    global prevY

    if prevX is None:
        prevX = e.x()
        prevY = e.y()
        return

    painter = QtGui.QPainter(canvas.pixmap())
    painter.drawLine(prevX, prevY, e.x(), e.y())
    painter.end()
    canvas.update()

    prevX = e.x()
    prevY = e.y()

def canvas_mouseReleaseEvent(e):
    global prevX
    global prevY
    prevX = None
    prevY = None

# 어플리케이션 생성
app = QtWidgets.QApplication([])
window = QtWidgets.QWidget() # 윈도우 생성
window.resize(1280, 800) # 윈도우 크기 설정
#window.setFixedSize(1280, 800) # 윈도우 크기 변경 불가
window.setWindowTitle('MyFirstQt') # 윈도우 타이틀 설정
window.show() # 화면에 윈도우 나타내기
width = window.width()
height = window.height()

"""
btnLoad = QtWidgets.QPushButton('Load', window)
btnLoad.setGeometry(10,10,100,50)
btnLoad.show()

btnLoad.clicked.connect(btnLoad_clicked)

lbImg = QtWidgets.QLabel('image', window)
lbImg.setGeometry(120, 10, 1280-120-10, 800-10-10)
lbImg.setStyleSheet("border: 1px solid black; background-color:lightgray; qproperty-alignment: AlignCenter")
lbImg.show()



canvas = QtWidgets.QLabel(window)
canvas.setGeometry(0,300,width,height-300)
pixmap = QtGui.QPixmap(canvas.width(), canvas.height())
pixmap.fill(Qt.white)
#pixmap.fill(QtGui.QColor(255,255,255))
#pixmap.fill(QtGui.QColor('#ffffff'))
canvas.setPixmap(pixmap)
canvas.show()

painter = QtGui.QPainter(canvas.pixmap())
painter.drawLine(100,100,300,300)
painter.drawText(0,32,'Hello Word in Canvas')
painter.end()
"""

"""
canvas = QtWidgets.QLabel(window)

painter = QtGui.QPainter(canvas.pixmap())
painter.drawRect(100,100,200,200) # x,y,width,height
painter.setPen(Qt.red)
painter.setPen(Qt.NoPen)
painter.setPen(Qt.black)

painter.setBrush(Qt.red)
painter.setBrush(Qt.NoBrush)

pen = QtGui.QPen()
pen.setWidth(3)
pen.setColor(QtGui.QColor(0,0,255))
brush = QtGui.QBrush(QtGui.QColor(255,0,0))
"""

"""
canvas = QtWidgets.QLabel(window)
canvas.setGeometry(0,300,width,height-300)
pixmap = QtGui.QPixmap(canvas.width(), canvas.height())
pixmap.fill(Qt.white)
#pixmap.fill(QtGui.QColor(255,255,255))
canvas.setPixmap(pixmap)
canvas.show()

pen = QtGui.QPen()
pen.setWidth(3)
pen.setColor(QtGui.QColor(0,0,255))

brush = QtGui.QBrush(QtGui.QColor(255,0,0))

painter = QtGui.QPainter(canvas.pixmap())
painter.setPen(pen)
painter.setBrush(brush)

painter.drawRect(100,100,200,200)

painter.setPen(Qt.black)
painter.setBrush(Qt.NoBrush)

painter.end()
"""
canvas = QtWidgets.QLabel(window)
canvas.setGeometry(0,300,width, height-300)
pixmap = QtGui.QPixmap(canvas.width(), canvas.height())
pixmap.fill(Qt.white)
canvas.setPixmap(pixmap)
canvas.show()

#canvas.setMouseTracking(True)
canvas.mouseMoveEvent = canvas_mouseMoveEvent
canvas.mouseReleaseEvent = canvas_mouseReleaseEvent
# 메시지 루프: 프로그램 종료할 때까지 메시지 반복 처리
app.exec_()
