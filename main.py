from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

def btnLoad_clicked():
    pixmap = QtGui.QPixmap("images\cat3.png")
    lbImg.setPixmap(pixmap)
    #lbImg.resize(pixmap.width(), pixmap.height())


# 어플리케이션 생성
app = QtWidgets.QApplication([])
window = QtWidgets.QWidget() # 윈도우 생성
window.resize(1280, 800) # 윈도우 크기 설정
#window.setFixedSize(1280, 800) # 윈도우 크기 변경 불가
window.setWindowTitle('MyFirstQt') # 윈도우 타이틀 설정
window.show() # 화면에 윈도우 나타내기

btnLoad = QtWidgets.QPushButton('Load', window)
btnLoad.setGeometry(10,10,100,50)
btnLoad.show()

btnLoad.clicked.connect(btnLoad_clicked)

lbImg = QtWidgets.QLabel('image', window)
lbImg.setGeometry(120, 10, 1280-120-10, 800-10-10)
lbImg.setStyleSheet("border: 1px solid black; background-color:lightgray; qproperty-alignment: AlignCenter")
lbImg.show()

# 메시지 루프: 프로그램 종료할 때까지 메시지 반복 처리
app.exec_()
