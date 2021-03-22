import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import weapon

class MyWindow(QMainWindow):
    mesoTotal=format(1234567890, ",")
    star=12
    timer=0
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 300, 220, 403)
        self.setFixedSize(220, 403)
        self.setWindowTitle("Starforce Simulator")
        # self.setWindowIcon(QIcon("starIcon.png"))

        
        labelItemName = QLabel("아케인셰이드 투핸드소드 ★"+str(self.star),self)
        labelItemName.setGeometry(5, 2, 300, 20)
        labelItemName.show()

        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        widget.appendPlainText(str(self.star))
        widget.show()
        

        
        
        labelItemImage = QLabel(weapon.twoHandSword,self)
        labelItemImage.setGeometry(10,15,200,250)

        my_font = QFont("Lucida Console", 1)
        labelItemImage.setFont(my_font)


        
        labelMesoTotal = QLabel("총 사용 메소 : "+str(self.mesoTotal), self)
        
        labelMesoTotal.setGeometry(8, 219, 300, 100)

        btnStar = QPushButton("강화하기", self)
        btnStar.setGeometry(5, 280, 210, 38)
        btnStar.clicked.connect(self.btnStar_clicked)

        btnStarReset = QPushButton("강화 초기화", self)
        btnStarReset.setGeometry(5, 320, 103, 38)
        btnStarReset.clicked.connect(self.btnStarReset_clicked)

        btnMesoReset = QPushButton("메소 초기화", self)
        btnMesoReset.setGeometry(112, 320, 103, 38)
        btnMesoReset.clicked.connect(self.btnMesoReset_clicked)

        btnQuit = QPushButton("종료하기", self)
        btnQuit.setGeometry(5, 360, 210, 38)
        btnQuit.clicked.connect(self.btnQuit_clicked)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        
    
    def btnStar_clicked(self):
        print(self.star)
        self.star += 1
        print("강화하기 클릭")
        print(self.star)
        
        
        
    def btnStarReset_clicked(self):
        self.star = 0
        print("강화 초기회 클릭")
    
    def btnMesoReset_clicked(self):
        print("메소 초기화 클릭"+self.mesoTotal)
        self.mesoTotal="1000"
        print("메소 초기화 클릭"+self.mesoTotal)
    
    def btnQuit_clicked(self):
        print("종료하기 클릭")
        sys.exit()
        

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()
