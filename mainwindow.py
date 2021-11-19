import cv2
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QPushButton
import resource
# from model import Model
from out_window import Ui_OutputDialog


class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("mainwindow.ui", self)

        self.runButton.clicked.connect(self.runSlot)
        self.picButton.clicked.connect(self.savePicture)

        self._new_window = None
        self.Videocapture_ = None
        self.setWindowTitle("Face Recognition and Attendance")
        self.setWindowIcon(QtGui.QIcon("icon.jpg"))
        
    def savePicture(self):
        name = self.nameTextBox.text()
        if name != "":
        
            reply = QMessageBox.question(self, 'Welcome ' + name, 'You want to take a picture ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
        
                video_capture = cv2.VideoCapture(0)
                # Check success
                if not video_capture.isOpened():
                    raise Exception("Could not open video device")
                # Read picture. ret === True on success
                ret, frame = video_capture.read()
                # Close device
                video_capture.release()
                cv2.imwrite('ImagesAttendance/'+name+'.jpeg',frame)
                self.runSlot() 
                
            else:
                print('Not clicked')
         
        else:  
            reply2 = QMessageBox.information(self, 'Warning! ' + name , 'You have to write your name ', QMessageBox.Ok, QMessageBox.Ok)
            if reply2 == QMessageBox.Ok:          
                print('Skip')
    
    def refreshAll(self):
        """
        Set the text of lineEdit once it's valid
        """
        self.Videocapture_ = "0"

    @pyqtSlot()
    def runSlot(self):
        """
        Called when the user presses the Run button
        """
        print("Clicked Run")
        self.refreshAll()
        print(self.Videocapture_)
        ui.hide()  # hide the main window
        self.outputWindow_()  # Create and open new output window
            
    
    def outputWindow_(self):
        """
        Created new window for vidual output of the video in GUI
        """
        self._new_window = Ui_OutputDialog()
        self._new_window.show()
        self._new_window.startVideo(self.Videocapture_)
        print("Video Played")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
