import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import weapon


class AutoStarDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.nowYouSeeMe=False
        self.goal = 0
        

    def setupUI(self):
        self.setGeometry(760, 380, 300, 100)
        self.setWindowTitle("자동 강화")

        label1 = QLabel("원하는 스타포스『10~22』 : \n 『23성 이상은 위험』\n\n파괴 1회 : 사용 메소 +20억")

        self.lineEdit1 = QLineEdit()
        self.pushButton1= QPushButton("Start")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        self.chBox = QCheckBox('Now you see me (20ms)',self)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(self.chBox,1,2)

        self.setLayout(layout)

    def pushButtonClicked(self):
        if(10 <= int(self.lineEdit1.text()) <= 25):
            self.goal = self.lineEdit1.text()
            self.nowYouSeeMe = self.chBox.isChecked()
            print(self.nowYouSeeMe)
            self.close()
        else:
            msg = QMessageBox.warning(self,'ERROR','잘못된 입력입니다.')
        
class MyWindow(QMainWindow):
    # 강화에 필요한 메소
    mesoRate=[321000, 641000, 961000, 1281000, 1601000,
            1921000, 2241000, 2561000, 2881000, 3201000,
            12966500, 16400100, 20356300, 24865300, 29956500,
            71316500, 83999600, 98016700, 113422300, 130270000,
            148612400, 168501500, 189988600, 213124000, 237957700]

    # 강화 성공 확률
    successRateNoStar=[0.95, 0.9, 0.85, 0.85, 0.8,
                    0.75, 0.7, 0.65, 0.6, 0.55,
                    0.5, 0.45, 0.4, 0.35, 0.3,
                    0.3, 0.3, 0.3, 0.3, 0.3,
                    0.3, 0.3, 0.03, 0.02, 0.01]

    # 파괴확률
    destroyRate=[0, 0, 0, 0, 0,
                0, 0, 0, 0, 0,
                0, 0, 0.006, 0.013, 0.014,
                0.021, 0.021, 0.021, 0.028, 0.028,
                0.07, 0.07, 0.2, 0.3, 0.4]

    mesoTotal=0
    star=0
    failRepeatCount = 0

    def __init__(self):
        super().__init__()
        self.setGeometry(800, 300, 220, 403)
        self.setFixedSize(220, 403)
        self.setWindowTitle("starforce")
        # self.setWindowIcon(QIcon("starIcon.png"))

        def autoStar_clicked():
            dlg = AutoStarDialog()
            dlg.exec_()
            self.goal = int(dlg.goal)
            nowYouSeeme = dlg.nowYouSeeMe
            print('star goal :',self.goal)
            
            if(nowYouSeeme == False):
                while(self.star < self.goal):
                    btnStar_clicked()
            else:
                self.timer = QTimer(self)
                self.timer.start(20)
                self.timer.timeout.connect(autoStar)
                     
        def autoStar():
            if(self.star >= self.goal):
                    self.timer.stop()
            else:
                btnStar_clicked()

        def btnStar_clicked():
            print("강화하기 클릭")
            
            rate = random.random()

            if(self.failRepeatCount==2):
                print("\n\n찬스타임 발동!! 강화 성공!!!")
                self.star+=1
                self.failRepeatCount=0

            elif(rate <= self.successRateNoStar[self.star]):
                print("\n\n강화 성공!!")
                self.star+=1
                self.failRepeatCount=0

            elif(rate <= self.successRateNoStar[self.star]+self.destroyRate[self.star]):
                print("\n\n장비가 파괴되었습니다!!!!!!!!")
                self.star=12
                self.mesoTotal+=2000000000 # 파괴시 아이템값 20억메소 

            else:
                if(self.star>10):
                    if(self.star != 15 and self.star != 20):
                        print("\n\n강화 실패!! ( 스타포스 하락 )")
                        self.star-=1
                        self.failRepeatCount+=1
                    else:
                        print("\n\n강화 실패!! ( 스타포스 유지 )")
                else:
                    print("\n\n강화 실패!! ( 스타포스 유지 )")
            
            self.mesoTotal += self.mesoRate[self.star]

            labelItemName.setText("아케인셰이드 투핸드소드 ★"+str(self.star))
            labelMesoTotal.setText("총 사용 메소 : "+format(self.mesoTotal, ","))

            if(self.star >= 20):
                labelItemImage.setStyleSheet("color: green")
            elif(self.star >= 15):
                labelItemImage.setStyleSheet("color: rgb(150,100,0)")
            elif(self.star >= 10):
                labelItemImage.setStyleSheet("color: rgb(200,0,255)")
            elif(self.star >= 5):
                labelItemImage.setStyleSheet("color: rgb(0,0,200)")

        def btnStarReset_clicked():
            print("강화 초기회 클릭")
            self.star = 0
            labelItemName.setText("아케인셰이드 투핸드소드 ★"+str(self.star))
            
        def btnMesoReset_clicked():
            print("메소 초기회 클릭")
            self.mesoTotal=0
            labelMesoTotal.setText("총 사용 메소 : "+format(self.mesoTotal, ","))
        
        def btnQuit_clicked():
            print("자동강화 클릭")
            autoStar_clicked()

    
        labelItemName = QLabel("아케인셰이드 투핸드소드 ★"+str(self.star),self)
        labelItemName.setGeometry(5, 2, 300, 20)
        labelItemName.show()

        labelItemImage = QLabel(weapon.twoHandSword,self)
        labelItemImage.setGeometry(10,15,200,250)
        my_font = QFont("Lucida Console", 1)
        labelItemImage.setFont(my_font)

        labelMesoTotal = QLabel("총 사용 메소 : "+str(self.mesoTotal), self)
        labelMesoTotal.setGeometry(8, 219, 300, 100)

        btnStar = QPushButton("강화하기", self)
        btnStar.setGeometry(5, 280, 210, 38)
        btnStar.clicked.connect(btnStar_clicked)

        btnStarReset = QPushButton("강화 초기화", self)
        btnStarReset.setGeometry(5, 320, 103, 38)
        btnStarReset.clicked.connect(btnStarReset_clicked)
        

        btnMesoReset = QPushButton("메소 초기화", self)
        btnMesoReset.setGeometry(112, 320, 103, 38)
        btnMesoReset.clicked.connect(btnMesoReset_clicked)

        btnQuit = QPushButton("자동강화", self)
        btnQuit.setGeometry(5, 360, 210, 38)
        btnQuit.clicked.connect(btnQuit_clicked)
        
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyWindow()
   sys.exit(app.exec_())

