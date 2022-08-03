from PyQt5 import QtCore, QtGui, QtWidgets
from Second import Ui_Second_page
from random import choice


class Ui_First_page(object):

    def Second_Window(self):
        self.windowbig = QtWidgets.QMainWindow()
        self.next = Ui_Second_page()
        self.next.setupUi(self.windowbig)
        self.windowbig.show()
            
    def setupUi(self, First_page):
        First_page.setObjectName("First_page")
        First_page.resize(500, 630)
        self.centralwidget = QtWidgets.QWidget(First_page)
        self.centralwidget.setObjectName("centralwidget")

        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(10, 10, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.welcome_label.setFont(font)
        self.welcome_label.setFrameShape(QtWidgets.QFrame.Box)
        self.welcome_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")

        self.warn_label = QtWidgets.QLabel(self.centralwidget)
        self.warn_label.setGeometry(QtCore.QRect(10, 400, 481, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.warn_label.setFont(font)
        self.warn_label.setFrameShape(QtWidgets.QFrame.Box)
        self.warn_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.warn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warn_label.setWordWrap(True)
        self.warn_label.setObjectName("warn_label")
        
        self.photo_label = QtWidgets.QLabel(self.centralwidget)
        self.photo_label.setGeometry(QtCore.QRect(10, 70, 481, 321))
        self.photo_label.setFrameShape(QtWidgets.QFrame.Box)
        self.photo_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.photo_label.setText("")
        self.photo_label.setPixmap(QtGui.QPixmap("ttt.jpg"))
        self.photo_label.setScaledContents(True)
        self.photo_label.setObjectName("photo_label")
        
        self.choose_xo_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_xo_label.setGeometry(QtCore.QRect(10, 465, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_xo_label.setFont(font)
        self.choose_xo_label.setFrameShape(QtWidgets.QFrame.Box)
        self.choose_xo_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.choose_xo_label.setObjectName("choose_xo_label")
        
        self.choose_pc_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_pc_label.setGeometry(QtCore.QRect(10, 515, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_pc_label.setFont(font)
        self.choose_pc_label.setFrameShape(QtWidgets.QFrame.Box)
        self.choose_pc_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.choose_pc_label.setObjectName("choose_pc_label")
        
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(10, 565, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.start_button.setObjectName("start_button")

        self.xo_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.xo_combo_box.setGeometry(QtCore.QRect(260, 465, 230, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.xo_combo_box.setFont(font)
        self.xo_combo_box.setObjectName("xo_combo_box")
        self.xo_combo_box.addItem("")
        self.xo_combo_box.addItem("")

        self.pc_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.pc_combo_box.setGeometry(QtCore.QRect(260, 515, 230, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pc_combo_box.setFont(font)
        self.pc_combo_box.setObjectName("pc_combo_box")
        self.pc_combo_box.addItem("")
        self.pc_combo_box.addItem("")
        
        First_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(First_page)
        self.statusbar.setObjectName("statusbar")
        First_page.setStatusBar(self.statusbar)

        self.retranslateUi(First_page)
        QtCore.QMetaObject.connectSlotsByName(First_page)

# ----------------------------------- LOGIC ---------------------------------------- #
        self.start_button.clicked.connect(self.Second_Window)
        self.start_button.clicked.connect(self.Write_Chosen)
        self.start_button.clicked.connect(First_page.close)

    
    # define method to write on the next page:
    def Write_Chosen(self):
        xo = self.xo_combo_box.currentText()
        pc = self.pc_combo_box.currentText()
        if pc == "Computer" and xo == "X":
            self.next.info_label.setText(f"Starts Computer, you are X")
            self.next.chosen = choice(self.next.boom)
            self.next.chosen.setText("O")
            self.next.chosen.setEnabled(False)
        elif pc == "Computer" and xo == "O":
            self.next.info_label.setText(f"Starts Computer, you are O")
            self.next.chosen = choice(self.next.boom)
            self.next.chosen.setText("X")
            self.next.chosen.setEnabled(False)
        elif pc == "Player" and xo == "X":
            self.next.info_label.setText(f"Starts Player, you are X")
        elif pc == "Player" and xo == "O":
            self.next.info_label.setText(f"Starts Player, you are O")
            


            

# ------------------------------------ END ----------------------------------------- #

    def retranslateUi(self, First_page):
        _translate = QtCore.QCoreApplication.translate
        First_page.setWindowTitle(_translate("First_page", "MainWindow"))
        self.welcome_label.setText(_translate("First_page", "Welcome to Tic-Tac-Toe Game!"))
        self.choose_xo_label.setText(_translate("First_page", "Which One You will be?"))
        self.choose_pc_label.setText(_translate("First_page", "Choose Who Starts the Game!"))
        self.start_button.setText(_translate("First_page", "Start Game"))
        self.warn_label.setText(_translate("First_page", ""))
        self.xo_combo_box.setItemText(0, _translate("WrongFormat_page", "X"))
        self.xo_combo_box.setItemText(1, _translate("WrongFormat_page", "O"))
        self.pc_combo_box.setItemText(0, _translate("WrongFormat_page", "Player"))
        self.pc_combo_box.setItemText(1, _translate("WrongFormat_page", "Computer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    First_page = QtWidgets.QMainWindow()
    ui = Ui_First_page()
    ui.setupUi(First_page)
    First_page.show()
    sys.exit(app.exec_())
