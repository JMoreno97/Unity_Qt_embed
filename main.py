import sys
import time

from PySide2.QtCore import Qt, QProcess
from PySide2.QtGui import QWindow
from PySide2.QtQuick import QQuickView
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        vl = QVBoxLayout()
        self.setWindowTitle("My App")
        widget = QWidget()
        widget.setLayout(vl)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    # Create unique QApplication instance
    app = QApplication(sys.argv)

    # Create a QWidget
    window = QWidget()
    vl = QVBoxLayout()
    window.setLayout(vl)

    # Create QProcess that runs Unity .exe
    unity = QProcess()
    unity.setProgram("C:\\Users\\UJA\\Documents\\Unity\\Ejecutable Proyecto GJ (bandera)\\Proyecto GJ.exe")
    unity.start()
    unity.waitForStarted()

    print("Unity id: " + unity.processId().__str__())

    # Create the Unity widget that contains the Unity window
    UnitySceneWindow = QWindow.fromWinId(unity.processId())
    unityWidget = QWidget.createWindowContainer(UnitySceneWindow, window, Qt.FramelessWindowHint)
    unityWidget.setFocusPolicy(Qt.TabFocus)

    vl.addWidget(unityWidget)
    window.show()

    # Start the event loop.
    app.exec_()

    # Your application won't reach here until you exit and the event
    # loop has stopped.
