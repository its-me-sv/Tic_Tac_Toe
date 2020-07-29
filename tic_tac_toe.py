from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
import sys
import random

computer = -1
player = 1
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def Available_Pos():
    global board
    return [x for x in board if isinstance(x, int)]

def Computer_Play():
    global ui2, board
    pos = random.choice(Available_Pos())
    if board[3-1]==board[2-1]=='X' or board[7-1]==board[4-1]=='X' or board[9-1]==board[5-1]=='X':
        if 1 in Available_Pos():
            pos = 1
    elif board[8-1]==board[5-1]=='X':
        if 2 in Available_Pos():
            pos = 2
    elif board[1-1]==board[2-1]=='X' or board[9-1]==board[6-1]=='X' or board[7-1]==board[5-1]=='X':
        if 3 in Available_Pos():
            pos = 3
    elif board[6-1]==board[5-1]=='X':
        if 4 in Available_Pos():
            pos = 4
    elif board[4-1]==board[5-1]=='X':
        if 6 in Available_Pos():
            pos = 6
    elif board[1-1]==board[4-1]=='X' or board[3-1]==board[5-1]=='X' or board[9-1]==board[8-1]=='X':
        if 7 in Available_Pos():
            pos = 7
    elif board[2-1]==board[5-1]=='X':
        if 8 in Available_Pos():
            pos = 8
    elif board[1-1]==board[5-1]=='X' or board[3-1]==board[6-1]=='X' or board[7-1]==board[8-1]=='X':
        if 9 in Available_Pos():
            pos = 9
    else:
        if 5 in Available_Pos():
            pos = 5
    if pos == 1:
        ui2.b1.click()
    elif pos == 2:
        ui2.b2.click()
    elif pos == 3:
        ui2.b3.click()
    elif pos == 4:
        ui2.b4.click()
    elif pos == 5:
        ui2.b5.click()
    elif pos == 6:
        ui2.b6.click()
    elif pos == 7:
        ui2.b7.click()
    elif pos == 8:
        ui2.b8.click()
    elif pos == 9:
        ui2.b9.click()

class Game_End(Exception):
    '''This Exception Is Raised When The Game Comes
    To End.'''
    pass

def Check_For_Game_Results():
    '''1 - Player X | 2 - Player O | 3 - Draw | 4 - Continue.'''
    global board
    if board[1-1] == board[2-1] == board[3-1]:
        return 1 if board[1-1] == "X" else 2
    elif board[4-1] == board[5-1] == board[6-1]:
        return 1 if board[4-1] == "X" else 2
    elif board[7-1] == board[8-1] == board[9-1]:
        return 1 if board[7-1] == "X" else 2
    elif board[1-1] == board[4-1] == board[7-1]:
        return 1 if board[1-1] == "X" else 2
    elif board[2-1] == board[5-1] == board[8-1]:
        return 1 if board[2-1] == "X" else 2
    elif board[3-1] == board[6-1] == board[9-1]:
        return 1 if board[3-1] == "X" else 2
    elif board[1-1] == board[5-1] == board[9-1]:
        return 1 if board[1-1] == "X" else 2
    elif board[3-1] == board[5-1] == board[7-1]:
        return 1 if board[3-1] == "X" else 2
    else:
        for i in board:
            if isinstance(i, int):
                return 4
        return 3

def Victory_Message(code):
    global computer
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowTitle(" ")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    if code == 1:
        msg.setText("X Won The Game")
    elif code == 2:
        msg.setText("O Won The Game")
    elif code == 3:
        msg.setText("Match Draw")
    elif code == 4:
        msg.setText("Your Chance")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()

def Display_Message(code):
    global computer
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowTitle(" ")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    if code == 1:
        if not computer:
            msg.setText("Player 1 Chance")
        else:
            msg.setText("Your Chance")
    elif code == 2:
        msg.setText("Player 2 Chance")
    elif code == 3:
        msg.setText("Computer Chance")
    elif code == 4:
        msg.setText("Your Chance")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


class Ui_game_board(object):
    def setupUi(self, game_board):
        game_board.setObjectName("game_board")
        game_board.resize(600, 600)
        game_board.setMinimumSize(QtCore.QSize(600, 600))
        game_board.setMaximumSize(QtCore.QSize(600, 600))
        game_board.setBaseSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        game_board.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(game_board)
        self.centralwidget.setObjectName("centralwidget")
        self.board_background = QtWidgets.QLabel(self.centralwidget)
        self.board_background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.board_background.setPixmap(QtGui.QPixmap(":/newPrefix/board.png"))
        self.board_background.setObjectName("board_background")
        self.pos1 = QtWidgets.QLabel(self.centralwidget)
        self.pos1.setGeometry(QtCore.QRect(0, 0, 171, 171))
        self.pos1.setPixmap(QtGui.QPixmap(":/newPrefix/1.png"))
        self.pos1.setScaledContents(True)
        self.pos1.setObjectName("pos1")
        self.pos2 = QtWidgets.QLabel(self.centralwidget)
        self.pos2.setGeometry(QtCore.QRect(210, 0, 171, 171))
        self.pos2.setPixmap(QtGui.QPixmap(":/newPrefix/2.png"))
        self.pos2.setScaledContents(True)
        self.pos2.setObjectName("pos2")
        self.pos3 = QtWidgets.QLabel(self.centralwidget)
        self.pos3.setGeometry(QtCore.QRect(420, 0, 181, 171))
        self.pos3.setPixmap(QtGui.QPixmap(":/newPrefix/3.png"))
        self.pos3.setScaledContents(True)
        self.pos3.setObjectName("pos3")
        self.pos4 = QtWidgets.QLabel(self.centralwidget)
        self.pos4.setGeometry(QtCore.QRect(0, 210, 171, 171))
        self.pos4.setPixmap(QtGui.QPixmap(":/newPrefix/4.png"))
        self.pos4.setScaledContents(True)
        self.pos4.setObjectName("pos4")
        self.pos5 = QtWidgets.QLabel(self.centralwidget)
        self.pos5.setGeometry(QtCore.QRect(210, 210, 171, 171))
        self.pos5.setPixmap(QtGui.QPixmap(":/newPrefix/5.png"))
        self.pos5.setScaledContents(True)
        self.pos5.setObjectName("pos5")
        self.pos6 = QtWidgets.QLabel(self.centralwidget)
        self.pos6.setGeometry(QtCore.QRect(420, 210, 181, 181))
        self.pos6.setPixmap(QtGui.QPixmap(":/newPrefix/6.png"))
        self.pos6.setScaledContents(True)
        self.pos6.setObjectName("pos6")
        self.pos7 = QtWidgets.QLabel(self.centralwidget)
        self.pos7.setGeometry(QtCore.QRect(0, 430, 171, 171))
        self.pos7.setPixmap(QtGui.QPixmap(":/newPrefix/7.png"))
        self.pos7.setScaledContents(True)
        self.pos7.setObjectName("pos7")
        self.pos8 = QtWidgets.QLabel(self.centralwidget)
        self.pos8.setGeometry(QtCore.QRect(210, 430, 171, 171))
        self.pos8.setPixmap(QtGui.QPixmap(":/newPrefix/8.png"))
        self.pos8.setScaledContents(True)
        self.pos8.setObjectName("pos8")
        self.pos9 = QtWidgets.QLabel(self.centralwidget)
        self.pos9.setGeometry(QtCore.QRect(420, 430, 181, 171))
        self.pos9.setPixmap(QtGui.QPixmap(":/newPrefix/9.png"))
        self.pos9.setScaledContents(True)
        self.pos9.setObjectName("pos9")
        self.b1 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(0, 0, 171, 171))
        self.b1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b1.setIcon(icon1)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(210, 0, 171, 171))
        self.b2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b2.setText("")
        self.b2.setIcon(icon1)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(420, 0, 181, 171))
        self.b3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b3.setText("")
        self.b3.setIcon(icon1)
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(0, 210, 171, 181))
        self.b4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b4.setText("")
        self.b4.setIcon(icon1)
        self.b4.setObjectName("b4")
        self.b5 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(210, 210, 171, 181))
        self.b5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b5.setText("")
        self.b5.setIcon(icon1)
        self.b5.setObjectName("b5")
        self.b6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(420, 220, 181, 171))
        self.b6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b6.setText("")
        self.b6.setIcon(icon1)
        self.b6.setObjectName("b6")
        self.b7 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(0, 430, 171, 171))
        self.b7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b7.setText("")
        self.b7.setIcon(icon1)
        self.b7.setObjectName("b7")
        self.b8 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(210, 420, 171, 181))
        self.b8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b8.setText("")
        self.b8.setIcon(icon1)
        self.b8.setObjectName("b8")
        self.b9 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(420, 430, 171, 171))
        self.b9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b9.setText("")
        self.b9.setIcon(icon1)
        self.b9.setObjectName("b9")
        game_board.setCentralWidget(self.centralwidget)

        self.retranslateUi(game_board)
        QtCore.QMetaObject.connectSlotsByName(game_board)

        self.b1.clicked.connect(self.Button1)
        self.b2.clicked.connect(self.Button2)
        self.b3.clicked.connect(self.Button3)
        self.b4.clicked.connect(self.Button4)
        self.b5.clicked.connect(self.Button5)
        self.b6.clicked.connect(self.Button6)
        self.b7.clicked.connect(self.Button7)
        self.b8.clicked.connect(self.Button8)
        self.b9.clicked.connect(self.Button9)

    def Button1(self):
        global player, board, computer
        result = Check_For_Game_Results()
        try:
            if result != 4:
                raise Game_End
        except Game_End:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        else:
            if player == 1:
                self.pos1.setPixmap(QtGui.QPixmap(":/newPrefix/X.png"))
                player, board[1-1] = 2, 'X'
                if computer == 1:
                    player = 3
            else:
                self.pos1.setPixmap(QtGui.QPixmap(":/newPrefix/O.png"))
                player, board[1-1] = 1, 'O'
            Display_Message(player)
            self.b1.setEnabled(False)
        result = Check_For_Game_Results()
        if result != 4:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        if player == 3:
            Computer_Play()

    def Button2(self):
        global player, board, computer
        result = Check_For_Game_Results()
        try:
            if result != 4:
                raise Game_End
        except Game_End:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        else:
            if player == 1:
                self.pos2.setPixmap(QtGui.QPixmap(":/newPrefix/X.png"))
                player, board[2-1] = 2, 'X'
                if computer == 1:
                    player = 3
            else:
                self.pos2.setPixmap(QtGui.QPixmap(":/newPrefix/O.png"))
                player, board[2-1] = 1, 'O'
            Display_Message(player)
            self.b2.setEnabled(False)
        result = Check_For_Game_Results()
        if result != 4:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        if player == 3:
            Computer_Play()

    def Button3(self):
        global player, board, computer
        result = Check_For_Game_Results()
        try:
            if result != 4:
                raise Game_End
        except Game_End:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        else:
            if player == 1:
                self.pos3.setPixmap(QtGui.QPixmap(":/newPrefix/X.png"))
                player, board[3-1] = 2, "X"
                if computer == 1:
                    player = 3
            else:
                self.pos3.setPixmap(QtGui.QPixmap(":/newPrefix/O.png"))
                player, board[3-1] = 1, "O"
            Display_Message(player)
            self.b3.setEnabled(False)
        result = Check_For_Game_Results()
        if result != 4:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        if player == 3:
            Computer_Play()

    def Button4(self):
        global player, board, computer
        result = Check_For_Game_Results()
        try:
            if result != 4:
                raise Game_End
        except Game_End:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        else:
            if player == 1:
                self.pos4.setPixmap(QtGui.QPixmap(":/newPrefix/X.png"))
                player, board[4-1] = 2, "X"
                if computer == 1:
                    player = 3
            else:
                self.pos4.setPixmap(QtGui.QPixmap(":/newPrefix/O.png"))
                player, board[4-1] = 1, "O"
            Display_Message(player)
            self.b4.setEnabled(False)
        result = Check_For_Game_Results()
        if result != 4:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        if player == 3:
            Computer_Play()

    def Button5(self):
        global player, board, computer
        result = Check_For_Game_Results()
        try:
            if result != 4:
                raise Game_End
        except Game_End:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        else:
            if player == 1:
                self.pos5.setPixmap(QtGui.QPixmap(":/newPrefix/X.png"))
                player, board[5-1] = 2, "X"
                if computer == 1:
                    player = 3
            else:
                self.pos5.setPixmap(QtGui.QPixmap(":/newPrefix/O.png"))
                player, board[5-1] = 1, "O"
            Display_Message(player)
            self.b5.setEnabled(False)
        result = Check_For_Game_Results()
        if result != 4:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        if player == 3:
            Computer_Play()

    def Button6(self):
        global player, board, computer
        result = Check_For_Game_Results()
        try:
            if result != 4:
                raise Game_End
        except Game_End:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        else:
            if player == 1:
                self.pos6.setPixmap(QtGui.QPixmap(":/newPrefix/X.png"))
                player, board[6-1] = 2, "X"
                if computer == 1:
                    player = 3
            else:
                self.pos6.setPixmap(QtGui.QPixmap(":/newPrefix/O.png"))
                player, board[6-1] = 1, "O"
            Display_Message(player)
            self.b6.setEnabled(False)
        result = Check_For_Game_Results()
        if result != 4:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        if player == 3:
            Computer_Play()

    def Button7(self):
        global player, board, computer
        result = Check_For_Game_Results()
        try:
            if result != 4:
                raise Game_End
        except Game_End:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        else:
            if player == 1:
                self.pos7.setPixmap(QtGui.QPixmap(":/newPrefix/X.png"))
                player, board[7-1] = 2, "X"
                if computer == 1:
                    player = 3
            else:
                self.pos7.setPixmap(QtGui.QPixmap(":/newPrefix/O.png"))
                player, board[7-1] = 1, "O"
            Display_Message(player)
            self.b7.setEnabled(False)
        result = Check_For_Game_Results()
        if result != 4:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        if player == 3:
            Computer_Play()

    def Button8(self):
        global player, board, computer
        result = Check_For_Game_Results()
        try:
            if result != 4:
                raise Game_End
        except Game_End:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        else:
            if player == 1:
                self.pos8.setPixmap(QtGui.QPixmap(":/newPrefix/X.png"))
                player, board[8-1] = 2, "X"
                if computer == 1:
                    player = 3
            else:
                self.pos8.setPixmap(QtGui.QPixmap(":/newPrefix/O.png"))
                player, board[8-1] = 1, "O"
            Display_Message(player)
            self.b8.setEnabled(False)
        result = Check_For_Game_Results()
        if result != 4:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        if player == 3:
            Computer_Play()

    def Button9(self):
        global player, board, computer
        result = Check_For_Game_Results()
        try:
            if result != 4:
                raise Game_End
        except Game_End:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        else:
            if player == 1:
                self.pos9.setPixmap(QtGui.QPixmap(":/newPrefix/X.png"))
                player, board[9-1] = 2, "X"
                if computer == 1:
                    player = 3
            else:
                self.pos9.setPixmap(QtGui.QPixmap(":/newPrefix/O.png"))
                player, board[9-1] = 1, "O"
            Display_Message(player)
            self.b9.setEnabled(False)
        result = Check_For_Game_Results()
        if result != 4:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            computer = -1
            player = 1
            Victory_Message(result)
            After_Splash.show()
            game_board.hide()
        if player == 3:
            Computer_Play()

    def retranslateUi(self, game_board):
        _translate = QtCore.QCoreApplication.translate
        game_board.setWindowTitle(_translate("game_board", "Game Board"))
        self.b1.setToolTip(_translate("game_board", "<html><head/><body><p><span style=\" font-weight:600;\">Position 1</span></p></body></html>"))
        self.b2.setToolTip(_translate("game_board", "<html><head/><body><p><span style=\" font-weight:600;\">Position 2</span></p></body></html>"))
        self.b3.setToolTip(_translate("game_board", "<html><head/><body><p><span style=\" font-weight:600;\">Position 3</span></p></body></html>"))
        self.b4.setToolTip(_translate("game_board", "<html><head/><body><p><span style=\" font-weight:600;\">Position 4</span></p></body></html>"))
        self.b5.setToolTip(_translate("game_board", "<html><head/><body><p><span style=\" font-weight:600;\">Position 5</span></p></body></html>"))
        self.b6.setToolTip(_translate("game_board", "<html><head/><body><p><span style=\" font-weight:600;\">Position 6</span></p></body></html>"))
        self.b7.setToolTip(_translate("game_board", "<html><head/><body><p><span style=\" font-weight:600;\">Position 7</span></p></body></html>"))
        self.b8.setToolTip(_translate("game_board", "<html><head/><body><p><span style=\" font-weight:600;\">Position 8</span></p></body></html>"))
        self.b9.setToolTip(_translate("game_board", "<html><head/><body><p><span style=\" font-weight:600;\">Position 9</span></p></body></html>"))


class Ui_After_Splash(object):
    def setupUi(self, After_Splash):
        After_Splash.setObjectName("After_Splash")
        After_Splash.resize(600, 600)
        After_Splash.setMinimumSize(QtCore.QSize(600, 600))
        After_Splash.setMaximumSize(QtCore.QSize(600, 600))
        After_Splash.setBaseSize(QtCore.QSize(600, 600))
        After_Splash.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        After_Splash.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(After_Splash)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 200, 200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/robot.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 210, 200, 200))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/players.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 30, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(42)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comp_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.comp_button.setGeometry(QtCore.QRect(74, 220, 161, 171))
        self.comp_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comp_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comp_button.setIcon(icon1)
        self.comp_button.setObjectName("comp_button")
        self.human_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.human_button.setGeometry(QtCore.QRect(340, 210, 191, 201))
        self.human_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.human_button.setText("")
        self.human_button.setIcon(icon1)
        self.human_button.setObjectName("human_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 530, 51, 51))
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.exit_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(530, 530, 51, 51))
        self.exit_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_button.setIcon(icon1)
        self.exit_button.setObjectName("exit_button")
        After_Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(After_Splash)
        QtCore.QMetaObject.connectSlotsByName(After_Splash)
        self.exit_button.clicked.connect(self.Take_To_Main_Page)
        self.comp_button.clicked.connect(self.Display_Board1)
        self.human_button.clicked.connect(self.Display_Board2)

    def Display_Board1(self):
        global ui2, computer, player, board
        computer = 1
        player = 1
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ui2.setupUi(game_board)
        game_board.show()
        Display_Message(4)

    def Display_Board2(self):
        global ui2, computer, player, board
        computer = 0
        player = 1
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ui2.setupUi(game_board)
        game_board.show()
        Display_Message(1)

    def Take_To_Main_Page(self):
        TTT.show()
        After_Splash.hide()

    def retranslateUi(self, After_Splash):
        _translate = QtCore.QCoreApplication.translate
        After_Splash.setWindowTitle(_translate("After_Splash", "Tic Tac Toe"))
        self.label_3.setText(_translate("After_Splash", "<html><head/><body><p><span style=\" color:#ffffff;\">Game Mode</span></p></body></html>"))
        self.comp_button.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-weight:600;\">Play With Computer</span></p></body></html>"))
        self.human_button.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-weight:600;\">Play With Friend</span></p></body></html>"))
        self.exit_button.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-weight:600;\">Exit To Main Page</span></p></body></html>"))


class Ui_TTT(object):
    def setupUi(self, TTT):
        TTT.setObjectName("TTT")
        TTT.resize(600, 600)
        TTT.setMinimumSize(QtCore.QSize(600, 600))
        TTT.setMaximumSize(QtCore.QSize(600, 600))
        TTT.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TTT.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TTT)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(150, 140, 300, 300))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.main_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.main_button.setGeometry(QtCore.QRect(214, 140, 191, 281))
        self.main_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button.setIcon(icon1)
        self.main_button.setObjectName("main_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 10, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.exit_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(540, 10, 51, 51))
        self.exit_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_button.setText("")
        self.exit_button.setIcon(icon1)
        self.exit_button.setObjectName("exit_button")
        TTT.setCentralWidget(self.centralwidget)

        self.retranslateUi(TTT)
        QtCore.QMetaObject.connectSlotsByName(TTT)
        self.exit_button.clicked.connect(self.Quit_Application)
        self.main_button.clicked.connect(self.Take_In)

    def Take_In(self):
        global ui1
        ui1.setupUi(After_Splash)
        After_Splash.show()
        TTT.hide()

    def Quit_Application(self):
        app.quit()

    def retranslateUi(self, TTT):
        _translate = QtCore.QCoreApplication.translate
        TTT.setWindowTitle(_translate("TTT", "Tic Tac Toe"))
        self.main_button.setToolTip(_translate("TTT", "<html><head/><body><p><span style=\" font-weight:600;\">Get In</span></p></body></html>"))
        self.exit_button.setToolTip(_translate("TTT", "<html><head/><body><p><span style=\" font-weight:600;\">Exit</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    game_board = QtWidgets.QMainWindow()
    ui2 = Ui_game_board()

    After_Splash = QtWidgets.QMainWindow()
    ui1 = Ui_After_Splash()

    TTT = QtWidgets.QMainWindow()
    ui = Ui_TTT()
    ui.setupUi(TTT)
    TTT.show()
    
    sys.exit(app.exec_())

#