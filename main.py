from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

def window_mousePressEvent(e):
    print(e.globalX(), e.globalY())
    print(e.x(), e.y())
def window_mouseMoveEvent(e):
    print(e.globalX(), e.globalY())
    print(e.x(), e.y())

"""0
def btn_click_clicked():
    print('btn_click is clicked')
    #app.exit()
    QtWidgets.QMessageBox.about(window, 'App', 'Hello')
"""

def window_mouseMoveEvent(e):
    pos = '{} {}'.format(e.x(), e.y())
    lb_txt.setText(pos)

def btn_click_clicked():
    lb_txt.setText(edt_line.text())

def edt_line_textChamged():
    lb_txt.setText(edt_line.text())
    print(edt_line.text())

def edt_box_textChanged():
    edt2_box.setText(edt_box.toPlainText())
    print(edt_box.toPlainText())

def window_keyPressEvent(e):
    print(e.key(), e.text())
    if e.key() == Qt.Key_Return:
        print('Enter')
    if e.modifiers() & Qt.CTRL:
        print('CTRL key')
    if e.modifiers() & Qt.SHIFT:
        print('SHIFT key')
    if e.modifiers() & Qt.ALT:
        print('ALT key')



# 어플리케이션 생성
app = QtWidgets.QApplication([])

window = QtWidgets.QWidget() # 윈도우 생성
window.resize(1280, 720) # 윈도우 크기 설정
#window.setFixedSize(1280, 800) # 윈도우 크기 변경 불가
window.setWindowTitle('MyFirstQt') # 윈도우 타이틀 설정
window.setStyleSheet('background-color : white; border: 1px solid black')
window.show() # 화면에 윈도우 나타내기

frameRt = window.frameGeometry() # 틀 포함 좌표
clientRt = window.geometry() # 틀 제외 좌표

# window.mouseMoveEvent = window_mouseMoveEvent
# window.mousePressEvent = window_mousePressEvent
# mouserReleaseEvent

btn_click = QtWidgets.QPushButton('click', window)
btn_click.setGeometry(0,0,200,150)
btn_click.show()
btn_click.clicked.connect(btn_click_clicked)

lb_txt = QtWidgets.QLabel('text here', window)
lb_txt.setGeometry(200, 0, 200, 150)
lb_txt.show()

window.mouseMoveEvent = window_mouseMoveEvent

edt_line = QtWidgets.QLineEdit('text here', window)
edt_line.setGeometry(0,150,200,64)
edt_line.show()

edt_line.textChanged.connect(edt_line_textChamged)

edt_box = QtWidgets.QTextEdit('text here', window)
edt_box.setGeometry(0, 200, 200, 150)
edt_box.show()

edt2_box = QtWidgets.QTextEdit('text here', window)
edt2_box.setGeometry(200, 200, 200, 150)
edt2_box.setReadOnly(True)
#edt2_box.setDisabled(True)
edt2_box.show()

edt_box.textChanged.connect(edt_box_textChanged)

window.keyPressEvent = window_keyPressEvent
"""
#window2 = QtWidgets.QWidget()
window2 = QtWidgets.QMdiSubWindow()
window2.setParent(window) # == Qt.SubWindow 설정효과
window2.setWindowFlags(Qt.Window) # Qt.Window 별도 창으로 띄운다
#window2.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint) #뭘해도 윈도우 타이틀을 못가짐
#window2.setWindowFlags(Qt.FramelessWindowHint) # 타이틀/테두리 없는 윈도우
window2.setStyleSheet('background-color: gray;')
window2.setWindowTitle('child')
window2.resize(800, 600)
window2.move(100,100)
#window2.move(frameRt.right(), frameRt.top())
window2.show()
"""

# 메시지 루프: 프로그램 종료할 때까지 메시지 반복 처리
app.exec_()
