import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from converted.translate import Ui_Dialog

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.form = Ui_Dialog()
        self.form.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
