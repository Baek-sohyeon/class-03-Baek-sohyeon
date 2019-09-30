import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        Name = QLabel("Name:", self)
        Age = QLabel("Age:", self)
        Score = QLabel("Score:", self)
        Result = QLabel("Result:", self)
        Key = QLabel("Key:", self)
        Amount = QLabel("Amount: ", self)

        self.NameEdit = QLineEdit()
        self.AgeEdit = QLineEdit()
        self.ScoreEdit = QLineEdit()
        self.AmountEdit = QLineEdit()
        self.ResultEdit = QTextEdit(self)
        self.KeyCombo = QComboBox()
        self.KeyCombo.addItems(["Name", "Age", "Score"])

        Add = QPushButton('Add', self)
        Add.clicked.connect(self.do_add)       #각각의 버튼 클릭시 해당하는 함수로 이동

        Del = QPushButton('Del', self)
        Del.clicked.connect(self.do_del)

        Find = QPushButton('Find', self)
        Find.clicked.connect(self.do_find)

        Inc = QPushButton('Inc', self)
        Inc.clicked.connect(self.do_inc)

        Show = QPushButton('Show', self)
        Show.clicked.connect(self.do_show)

        hbox = [QHBoxLayout() for x in range(5)]        #5개의 hbox 레이아웃 생성
        hbox[0].addStretch(1)
        hbox[0].addWidget(Name)
        hbox[0].addWidget(self.NameEdit)
        hbox[0].addWidget(Age)
        hbox[0].addWidget(self.AgeEdit)
        hbox[0].addWidget(Score)
        hbox[0].addWidget(self.ScoreEdit)

        hbox[1].stretch(1)
        hbox[1].addWidget(Amount)
        hbox[1].addWidget(self.AmountEdit)
        hbox[1].addWidget(Key)
        hbox[1].addWidget(self.KeyCombo)

        hbox[2].stretch(1)
        hbox[2].addWidget(Add)
        hbox[2].addWidget(Del)
        hbox[2].addWidget(Find)
        hbox[2].addWidget(Inc)
        hbox[2].addWidget(Show)

        hbox[4].stretch(1)
        hbox[4].addWidget(Result)
        hbox[4].addWidget(self.ResultEdit)

        vbox = QVBoxLayout()            #레이아웃을 묶을 메인 레이아웃 생성
        vbox.addStretch(1)
        vbox.addLayout(hbox[0])
        vbox.addLayout(hbox[1])
        vbox.addLayout(hbox[2])
        vbox.addLayout(hbox[4])

        self.setLayout(vbox)            #메인 레이아웃 호출

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname="Name"):      #showScoreDB의 초기 키 기준을 Name으로 설정, 들어오는 ket에 따라 다르게 적용
        string = ''
        for p in sorted(self.scoredb, key=lambda person: person[keyname]): #keyname 기준으로 내림차순, scoredb 배열에 접근
            for attr in sorted(p):      #각각의 배열에서 name, age, score에 접근
                string += attr + "=" + str(p[attr]) + '\t'      #name의 value, age의 value, socre의 value를 모두 string에 추가
            string += "\n"  #스트링에 다 추가했으면 개행
        self.ResultEdit.setText(string)     #결과창에 string 출력

    def do_add(self):
        name = self.NameEdit.text()
        age = self.AgeEdit.text()
        score = self.ScoreEdit.text()
        record = {'Name': name, 'Age': int(age), 'Score': int(score)}
        self.scoredb += [record]
        self.showScoreDB()

    def do_del(self):
        name = self.NameEdit.text()
        a = self.scoredb[:]     #a 변수에 scoredb 배열 전체 저장
        for p in a:
            if p['Name'] == name:
                self.scoredb.remove(p)
        self.showScoreDB()

    def do_find(self):
        name = self.NameEdit.text()     #name에 적혀있는 text 받음
        string = ""
        for a in self.scoredb:          #scoredb 배열에 접근
            if a['Name'] == name:       #배열 각각의 Name이 받아온 name과 같다면
                string += 'Name=' + str(a['Name']) + "\t" + 'Age=' + str(a["Age"]) + "\t" + 'Score=' + str(a['Score'])      #해당 배열의 name, age, score 출력
                string += '\n'
        self.ResultEdit.setText(string)

    def do_inc(self):
        name = self.NameEdit.text()
        score = self.AmountEdit.text()
        for i in self.scoredb:
            if i['Name'] == name:
                i['Score'] = int(i['Score']) + int(score)
        self.showScoreDB()

    def do_show(self):
        self.showScoreDB(self.KeyCombo.currentText())       #키콤보에서 선택된 키 showScoreDB 함수의 인자로 보낸다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())