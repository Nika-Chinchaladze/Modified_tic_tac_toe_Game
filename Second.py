from PyQt5 import QtCore, QtGui, QtWidgets
from random import choice


class Ui_Second_page(object):

    def Restart_Game(self):
        from First import Ui_First_page

        self.window2pac = QtWidgets.QMainWindow()
        self.again = Ui_First_page()
        self.again.setupUi(self.window2pac)
        self.window2pac.show()

    def setupUi(self, Second_page):
        Second_page.setObjectName("Second_page")
        Second_page.resize(432, 578)
        self.centralwidget = QtWidgets.QWidget(Second_page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(10, 10, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.info_label.setFont(font)
        self.info_label.setFrameShape(QtWidgets.QFrame.Box)
        self.info_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.info_label.setText("")
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setWordWrap(True)
        self.info_label.setObjectName("info_label")
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 411, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(1)
        self.grid_layout.setObjectName("grid_layout")
        
        self.button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button_4.setFont(font)
        self.button_4.setText("")
        self.button_4.setObjectName("button_4")
        
        self.grid_layout.addWidget(self.button_4, 0, 1, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button_5.setFont(font)
        self.button_5.setText("")
        self.button_5.setObjectName("button_5")
        
        self.grid_layout.addWidget(self.button_5, 1, 1, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setMinimumSize(QtCore.QSize(100, 102))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button_9.setFont(font)
        self.button_9.setText("")
        self.button_9.setObjectName("button_9")
        
        self.grid_layout.addWidget(self.button_9, 2, 2, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button_2.setFont(font)
        self.button_2.setText("")
        self.button_2.setObjectName("button_2")
        
        self.grid_layout.addWidget(self.button_2, 1, 0, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button_8.setFont(font)
        self.button_8.setText("")
        self.button_8.setObjectName("button_8")
        
        self.grid_layout.addWidget(self.button_8, 1, 2, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setMinimumSize(QtCore.QSize(100, 102))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button_3.setFont(font)
        self.button_3.setText("")
        self.button_3.setObjectName("button_3")
        
        self.grid_layout.addWidget(self.button_3, 2, 0, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button_7.setFont(font)
        self.button_7.setText("")
        self.button_7.setObjectName("button_7")
        
        self.grid_layout.addWidget(self.button_7, 0, 2, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setMinimumSize(QtCore.QSize(100, 102))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button_6.setFont(font)
        self.button_6.setText("")
        self.button_6.setObjectName("button_6")
        
        self.grid_layout.addWidget(self.button_6, 2, 1, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button_1.setFont(font)
        self.button_1.setText("")
        self.button_1.setObjectName("button_1")
        self.grid_layout.addWidget(self.button_1, 0, 0, 1, 1)
        
        self.restart_button = QtWidgets.QPushButton(self.centralwidget)
        self.restart_button.setGeometry(QtCore.QRect(10, 510, 191, 41))
        self.restart_button.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.restart_button.setObjectName("restart_button")
        
        self.end_button = QtWidgets.QPushButton(self.centralwidget)
        self.end_button.setGeometry(QtCore.QRect(230, 510, 191, 41))
        self.end_button.setStyleSheet("background-color: rgb(222, 222, 166);")
        self.end_button.setObjectName("end_button")
        
        self.answer_label = QtWidgets.QLabel(self.centralwidget)
        self.answer_label.setGeometry(QtCore.QRect(10, 390, 411, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer_label.setFont(font)
        self.answer_label.setFrameShape(QtWidgets.QFrame.Box)
        self.answer_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.answer_label.setText("")
        self.answer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_label.setWordWrap(True)
        self.answer_label.setObjectName("answer_label")
# ------------------------------------------------------------------------- #
        self.secret_label = QtWidgets.QLabel(self.centralwidget)
        self.secret_label.setGeometry(QtCore.QRect(5, 380, 15, 10))
        self.secret_label.setStyleSheet("color: rgb(240, 240, 240);")
        self.secret_label.setObjectName("secret_label")
# ------------------------------------------------------------------------- #
        Second_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Second_page)
        self.statusbar.setObjectName("statusbar")
        Second_page.setStatusBar(self.statusbar)

        self.retranslateUi(Second_page)
        QtCore.QMetaObject.connectSlotsByName(Second_page)

# ---------------------------------------- LOGIC -------------------------------------- #
        # define useful variables:
        self.boom = [self.button_1, self.button_2, self.button_3, self.button_4, self.button_5,
        self.button_6, self.button_7, self.button_8, self.button_9]

        self.xp_counter = 0
        self.op_counter = 0
        self.xc_counter = 0
        self.oc_counter = 0

        # call methods from here:
        self.button_1.clicked.connect(lambda: self.If_Clicked(self.button_1))
        self.button_2.clicked.connect(lambda: self.If_Clicked(self.button_2))
        self.button_3.clicked.connect(lambda: self.If_Clicked(self.button_3))
        self.button_4.clicked.connect(lambda: self.If_Clicked(self.button_4))
        self.button_5.clicked.connect(lambda: self.If_Clicked(self.button_5))
        self.button_6.clicked.connect(lambda: self.If_Clicked(self.button_6))
        self.button_7.clicked.connect(lambda: self.If_Clicked(self.button_7))
        self.button_8.clicked.connect(lambda: self.If_Clicked(self.button_8))
        self.button_9.clicked.connect(lambda: self.If_Clicked(self.button_9))

        self.restart_button.clicked.connect(self.Restart_Game)
        self.restart_button.clicked.connect(Second_page.close)
        self.end_button.clicked.connect(Second_page.close)

    # define method for Player:Computer
    def If_Clicked(self, button):
        if self.info_label.text() == "Starts Player, you are X":
            button.setText("X")
            button.setEnabled(False)
            self.xp_counter += 1

            self.Who_Won()
            if self.secret_label.text() != "w":
                self.Computer_Answer()

        #--------------------------------------------------------------
        if self.info_label.text() == "Starts Player, you are O":
            button.setText("O")
            button.setEnabled(False)
            self.op_counter += 1

            self.Who_Won()
            if self.secret_label.text() != "w":
                self.Computer_Answer()

        #--------------------------------------------------------------
        if self.info_label.text() == "Starts Computer, you are X":
            button.setText("X")
            button.setEnabled(False)
            self.xc_counter += 1

            self.Who_Won()
            if self.secret_label.text() != "w":
                self.Computer_Answer()

        #--------------------------------------------------------------
        if self.info_label.text() == "Starts Computer, you are O":
            button.setText("O")
            button.setEnabled(False)
            self.oc_counter += 1

            self.Who_Won()
            if self.secret_label.text() != "w":
                self.Computer_Answer()
        

    # define method for computer answer:
    def Computer_Answer(self):
        self.Buttons_list = [self.button_1, self.button_2, self.button_3, self.button_4, self.button_5,
        self.button_6, self.button_7, self.button_8, self.button_9]
        
        self.Clean_list = []
        for i in self.Buttons_list:
            if i.text() != "X" and i.text() != "O":
                self.Clean_list.append(i)
        # ----------------------------------------------------------------------------------
        if len(self.Clean_list) > 0 and self.info_label.text() == "Starts Player, you are X":
            computer_answer = choice(self.Clean_list)
            computer_answer.setText("O")
            computer_answer.setEnabled(False)
            self.xp_counter += 1
        
            self.Who_Won()
        # ----------------------------------------------------------------------------------
        if len(self.Clean_list) > 0 and self.info_label.text() == "Starts Player, you are O":
            computer_answer = choice(self.Clean_list)
            computer_answer.setText("X")
            computer_answer.setEnabled(False)
            self.op_counter += 1
        
            self.Who_Won()
        # ----------------------------------------------------------------------------------
        if len(self.Clean_list) > 0 and self.info_label.text() == "Starts Computer, you are X":
            computer_answer = choice(self.Clean_list)
            computer_answer.setText("O")
            computer_answer.setEnabled(False)
            self.xc_counter += 1
        
            self.Who_Won()
        # ----------------------------------------------------------------------------------
        if len(self.Clean_list) > 0 and self.info_label.text() == "Starts Computer, you are O":
            computer_answer = choice(self.Clean_list)
            computer_answer.setText("X")
            computer_answer.setEnabled(False)
            self.oc_counter += 1
        
            self.Who_Won()
        
    # define Who_won method:
    def Who_Won(self):
        first = self.button_1.text()
        second = self.button_2.text()
        third = self.button_3.text()
        fourth = self.button_4.text()
        fifth = self.button_5.text()
        sixth = self.button_6.text()
        seventh = self.button_7.text()
        eighth = self.button_8.text()
        nineth = self.button_9.text()

        my_list = []
        for i in self.boom:
            if len(i.text()) > 0:
                my_list.append(i)
        length = len(my_list)

        if first != "" and first == second and first == third:
            self.button_1.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_2.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_3.setStyleSheet("color: rgb(255, 0, 0);")
            self.secret_label.setText("w")
            self.Disable()
            self.Winner_For_xp()

        elif fourth != "" and fourth == fifth and fourth == sixth:
            self.button_4.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_5.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_6.setStyleSheet("color: rgb(255, 0, 0);")
            self.secret_label.setText("w")
            self.Disable()
            self.Winner_For_xp()

        elif seventh != "" and seventh == eighth and seventh == nineth:
            self.button_7.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_8.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_9.setStyleSheet("color: rgb(255, 0, 0);")
            self.secret_label.setText("w")
            self.Disable()
            self.Winner_For_xp()

        elif first != "" and first == fourth and first == seventh:
            self.button_1.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_4.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_7.setStyleSheet("color: rgb(255, 0, 0);")
            self.secret_label.setText("w")
            self.Disable()
            self.Winner_For_xp()

        elif second != "" and second == fifth and second == eighth:
            self.button_2.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_5.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_8.setStyleSheet("color: rgb(255, 0, 0);")
            self.secret_label.setText("w")
            self.Disable()
            self.Winner_For_xp()

        elif third != "" and third == sixth and third == nineth:
            self.button_3.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_6.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_9.setStyleSheet("color: rgb(255, 0, 0);")
            self.secret_label.setText("w")
            self.Disable()
            self.Winner_For_xp()

        elif first != "" and first == fifth and first == nineth:
            self.button_1.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_5.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_9.setStyleSheet("color: rgb(255, 0, 0);")
            self.secret_label.setText("w")
            self.Disable()
            self.Winner_For_xp()

        elif third != "" and third == fifth and third == seventh:
            self.button_3.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_5.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_7.setStyleSheet("color: rgb(255, 0, 0);")
            self.secret_label.setText("w")
            self.Disable()
            self.Winner_For_xp()
        
        elif length == 9:
            self.answer_label.setText("Unfortunately, Noone Won the Game, Be Focus!")
        
    
    # define method to disable buttons:
    def Disable(self):
        self.button_1.setEnabled(False)
        self.button_2.setEnabled(False)
        self.button_3.setEnabled(False)
        self.button_4.setEnabled(False)
        self.button_5.setEnabled(False)
        self.button_6.setEnabled(False)
        self.button_7.setEnabled(False)
        self.button_8.setEnabled(False)
        self.button_9.setEnabled(False)

    
    # define winner:
    def Winner_For_xp(self):
        if self.info_label.text() == "Starts Player, you are X":
            if self.xp_counter % 2 == 1:
                self.answer_label.setText("Congratulations, Player Won The GAME!")
                self.answer_label.setStyleSheet("background-color: rgb(85, 255, 127);")
            elif self.xp_counter % 2 == 0:
                self.answer_label.setText("Unfortunately, Computer Won The GAME, Try Again!")
                self.answer_label.setStyleSheet("background-color: rgb(255, 75, 44);")
        
        if self.info_label.text() == "Starts Player, you are O":
            if self.op_counter % 2 == 1:
                self.answer_label.setText("Congratulations, Player Won The GAME!")
                self.answer_label.setStyleSheet("background-color: rgb(85, 255, 127);")
            elif self.op_counter % 2 == 0:
                self.answer_label.setText("Unfortunately, Computer Won The GAME, Try Again!")
                self.answer_label.setStyleSheet("background-color: rgb(255, 75, 44);")
        
        if self.info_label.text() == "Starts Computer, you are X":
            if self.xc_counter % 2 == 1:
                self.answer_label.setText("Congratulations, Player Won The GAME!")
                self.answer_label.setStyleSheet("background-color: rgb(85, 255, 127);")
            elif self.xc_counter % 2 == 0:
                self.answer_label.setText("Unfortunately, Computer Won The GAME, Try Again!")
                self.answer_label.setStyleSheet("background-color: rgb(255, 75, 44);")
        
        if self.info_label.text() == "Starts Computer, you are O":
            if self.oc_counter % 2 == 1:
                self.answer_label.setText("Congratulations, Player Won The GAME!")
                self.answer_label.setStyleSheet("background-color: rgb(85, 255, 127);")
            elif self.oc_counter % 2 == 0:
                self.answer_label.setText("Unfortunately, Computer Won The GAME, Try Again!")
                self.answer_label.setStyleSheet("background-color: rgb(255, 75, 44);")
        

# ----------------------------------------- END --------------------------------------- #

    def retranslateUi(self, Second_page):
        _translate = QtCore.QCoreApplication.translate
        Second_page.setWindowTitle(_translate("Second_page", "MainWindow"))
        self.restart_button.setText(_translate("Second_page", "Restart Game"))
        self.end_button.setText(_translate("Second_page", "End Game"))
        self.secret_label.setText(_translate("Second_page", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Second_page = QtWidgets.QMainWindow()
    ui = Ui_Second_page()
    ui.setupUi(Second_page)
    Second_page.show()
    sys.exit(app.exec_())
