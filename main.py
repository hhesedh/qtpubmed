import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import QSize
from pymed import PubMed


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.pubmed = PubMed(tool="MyTool", email="my@email.address")

        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        self.pybutton = QPushButton('OK', self)
        self.pybutton.clicked.connect(self.click_method)
        self.pybutton.resize(200, 32)
        self.pybutton.move(80, 60)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.move(80, 100)
        self.pbar.setValue(0)

        self.setWindowTitle("QT Progressbar Example")
        self.setGeometry(32, 32, 320, 200)
        self.show()

    def click_method(self):
        results = self.pubmed.getTotalResultsCount(self.line.text())
        print(results)
        self.handle_timer(results)

    def handle_timer(self, results):
        self.pbar.setValue(results)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
