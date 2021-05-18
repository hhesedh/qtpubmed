import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import QSize


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.click_method)
        pybutton.resize(200, 32)
        pybutton.move(80, 60)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.move(80, 100)
        self.pbar.setValue(50)

        self.setWindowTitle("QT Progressbar Example")
        self.setGeometry(32, 32, 320, 200)
        self.show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timer)
        self.timer.start(1000)

    def click_method(self):
        print(self.line.text())

    def handle_timer(self):
        value = self.pbar.value()
        if value < 100:
            value = value + 1
            self.pbar.setValue(value)
        else:
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
