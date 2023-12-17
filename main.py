import sys
import typing
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget
import resource_rc
import random
class DataOperations():
    def selectChoice(self):
        self.COMPUTER_CHOICE = random.choice(["Rock","Paper","Scissor"])
        return self.COMPUTER_CHOICE
    def rockProcess(self):
        self.PLAYER_CHOICE == "Rock"
        self.COMPUTER_CHOICE = self.selectChoice()
        if self.COMPUTER_CHOICE == "Rock":
            self.stackedWidget_2.setCurrentIndex(1)
            self.stackedWidget.setCurrentIndex(0)
        elif self.COMPUTER_CHOICE == "Paper":
            self.stackedWidget_2.setCurrentIndex(0)
            self.COMPUTER_SCORE +=1
            self.stackedWidget.setCurrentIndex(1)
            self.computerScore.setText(str(self.COMPUTER_SCORE))
        elif self.COMPUTER_CHOICE == "Scissor":
            self.stackedWidget_2.setCurrentIndex(3)
            self.PLAYER_SCORE +=1
            self.stackedWidget.setCurrentIndex(2)
            self.playerScore.setText(str(self.PLAYER_SCORE))
        
    def paperProcess(self):
        self.PLAYER_CHOICE == "Paper"
        self.COMPUTER_CHOICE = self.selectChoice()
        if self.COMPUTER_CHOICE == "Paper":
            self.stackedWidget_2.setCurrentIndex(1)
            self.stackedWidget.setCurrentIndex(1)
        elif self.COMPUTER_CHOICE == "Scissor":
            self.stackedWidget_2.setCurrentIndex(0)
            self.COMPUTER_SCORE +=1
            self.stackedWidget.setCurrentIndex(2)
            self.computerScore.setText(str(self.COMPUTER_SCORE))
        elif self.COMPUTER_CHOICE == "Rock":
            self.stackedWidget_2.setCurrentIndex(3)
            self.PLAYER_SCORE +=1
            self.stackedWidget.setCurrentIndex(0)
            self.playerScore.setText(str(self.PLAYER_SCORE))
    
    def scissorProcess(self):
        self.PLAYER_CHOICE == "Scissor"
        self.COMPUTER_CHOICE = self.selectChoice()
        if self.COMPUTER_CHOICE == "Scissor":
            self.stackedWidget_2.setCurrentIndex(1)
            self.stackedWidget.setCurrentIndex(2)
        elif self.COMPUTER_CHOICE == "Rock":
            self.stackedWidget_2.setCurrentIndex(0)
            self.COMPUTER_SCORE +=1
            self.stackedWidget.setCurrentIndex(0)
            self.computerScore.setText(str(self.COMPUTER_SCORE))
        elif self.COMPUTER_CHOICE == "Paper":
            self.stackedWidget_2.setCurrentIndex(3)
            self.PLAYER_SCORE +=1
            self.stackedWidget.setCurrentIndex(1)
            self.playerScore.setText(str(self.PLAYER_SCORE))
        
        
    def __init__(self):
        global PLAYER_SCORE
        global COMPUTER_SCORE
        global PLAYER_CHOICE
        global COMPUTER_CHOICE
        self.PLAYER_SCORE = 0
        self.COMPUTER_SCORE = 0
        self.PLAYER_CHOICE = ""
        self.COMPUTER_CHOICE = ""

class HowToPlay(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        uic.loadUi("./Resources/User Interfaces/howtoPlay.ui",self)
    
class AboutDeveloper(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        uic.loadUi("./Resources/User Interfaces/aboutGame.ui",self)
class MainWindow(QMainWindow,DataOperations):
    def resetButton(self):
        r = QMessageBox()
        r.setIcon(QMessageBox.Question)
        r.setWindowTitle("Reset and Start New Game?")
        r.setText("Do you want to start a new Game?")
        r.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        x = r.exec_()
        if x == QMessageBox.Yes:
            self.PLAYER_SCORE,self.COMPUTER_SCORE = 0,0
            self.playerScore.setText(str(self.PLAYER_SCORE))
            self.computerScore.setText(str(self.COMPUTER_SCORE))
            self.stackedWidget_2.setCurrentIndex(2)
        else:
            pass
    def closeApplication(self):
        r = QMessageBox()
        r.setIcon(QMessageBox.Question)
        r.setWindowTitle("Close the Application?")
        r.setText("Do you really want to close the Application?")
        r.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        x = r.exec_()
        if x == QMessageBox.Yes:
            window.close()
            sys.exit
        else:
            pass
    def __init__(self):
        
        super(QMainWindow,self).__init__()
        uic.loadUi("./Resources/User Interfaces/mainWindow.ui",self)
        self.playerRock.clicked.connect(self.rockProcess)
        self.playerPaper.clicked.connect(self.paperProcess)
        self.playerScissor.clicked.connect(self.scissorProcess)
        self.actionNew_Game.triggered.connect(self.resetButton)
        self.actionExit.triggered.connect(self.closeApplication)
        self.actionHow_to_play.triggered.connect(window2.show)
        self.actionAbout_Developer.triggered.connect(window3.show)
if __name__ == "__main__":

    app =  QApplication(sys.argv)
    window2 = HowToPlay()
    window3 = AboutDeveloper()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())