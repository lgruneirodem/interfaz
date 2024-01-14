# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 01:49:21 2024

@author: leti
"""

# Nike desktop concept app
# Developed by Spinn Design
# website https://wwww.spinndesign.com
# Youtube : Spinn Tv https://www.youtube.com/channel/UCJVsWdUC3M8p-q67RXPujkg

# APP MAIN SCREEN

# APP Imports
import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# Import user interface file
from dla import *

# Global value for the windows status
WINDOW_SIZE = 0;
# This will help us determine if the window is minimized or maximized

# Main class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove window tittle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      
        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Button click events to our top bar buttons
        # 
        #Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        #Close window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        #Restore/Maximize window
        self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())
        # ###############################################


        # ###############################################
        # Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            # ###############################################

        
        # ###############################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        # ###############################################
        self.ui.main_header.mouseMoveEvent = moveWindow
        # ###############################################






        # STACKED PAGES (DEFAUT /CURRENT PAGE)/////////////////
        #Set the page that will be visible by default when the app is opened 
        self.ui.stackedWidget.setCurrentWidget(self.ui.equipo_page)
        # ###############################################
        # //////////////////////////////////////

        # STACKED PAGES NAVIGATION/////////////////
        #Using side menu buttons

        #navegar a la ventana Tu equipo
        self.ui.botonequipo.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.equipo_page))
        

        #navegar a la ventana predicciones
        self.ui.botonpredicciones.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.predicciones_page))
        

        # ###############################################
        # //////////////////////////////////////





        # ############################################
        # Show window
        self.show()
        # ###############################################




    # ###############################################
    # Add mouse events to the window
    # ###############################################
    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
        # ###############################################
    # ###############################################

# Execute app
# 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
else:
	print(__name__, "hh")

# press ctrl+b in sublime to run