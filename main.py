import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from view.home import Home

class MainWindow(QMainWindow, Home):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec()
