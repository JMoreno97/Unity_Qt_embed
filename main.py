import sys
import time
import win32gui

from PySide2.QtCore import Qt, QProcess
from PySide2.QtGui import QWindow
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        vl = QVBoxLayout()
        self.setWindowTitle("Project UI")
        widget = QWidget()
        widget.setLayout(vl)
        self.setCentralWidget(widget)

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible(hwnd):
        print (hex(hwnd), win32gui.GetWindowText( hwnd ))

if __name__ == '__main__':
    # Create unique QApplication instance
    app = QApplication(sys.argv)

    # Create a QMainWindow
    # I have also tested it with a QWidget instead of QMainWindow and it works as well
    main_window = MainWindow()

    # Create QProcess that runs the unity .exe
    unity = QProcess()
    unity.setProgram("C:\\Users\\UJA\\Documents\\Unity\\Ejecutable Proyecto GJ (bandera)\\Proyecto GJ.exe")
    unity.start()
    unity.waitForStarted()
    time.sleep(5)

    #I used this method to print the active windows and see unity's window name.
    #win32gui.EnumWindows(winEnumHandler, 0)
    hwnd = win32gui.FindWindow(0, "Proyecto GJ")

    #Get the unity window from the hwnd
    UnitySceneWindow = QWindow.fromWinId(hwnd)
    # Create the Unity widget that contains the Unity window
    unityWidget = QWidget.createWindowContainer(UnitySceneWindow)
    unityWidget.setFocusPolicy(Qt.TabFocus)

    #Set the the unity widget to the QMainWindow central widget
    main_window.setCentralWidget(unityWidget)
    #Show the window
    main_window.show()

    # Start the event loop.
    app.exec_()

    # Your application won't reach here until you exit and the event
    # loop has stopped.
