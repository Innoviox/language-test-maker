from sys       import argv
from functools import partial
from random    import shuffle
from PySide2   import QtCore, QtGui, QtWidgets
from base      import get_challenges, Challenge, log, play, sentence_to_audio

implemented = ["form", "select", "judge"]

class GuiChallenge(Challenge):
    def setupUi(self, Dialog):
        self.widgets = []
        self.master = Dialog
        
        self.title = f"Challenge: {self.type}"
        Dialog.setObjectName(self.title)
        Dialog.resize(400, 300)

        self.check = QtWidgets.QPushButton(Dialog)
        self.check.setGeometry(QtCore.QRect(140, 250, 112, 32))
        self.check.setObjectName("check")
        self.check.setChecked(False)
        self.check.clicked.connect(self.check_answer)
        self.widgets.append([self.check, "Check"])

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 340, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widgets.append([self.label, self.prompt])

        if self.type in implemented:
            x, y = 100, 75
            for i, c in enumerate(self.choices, start=1):
                a = f"radioBox_{i}"
                setattr(self, a, QtWidgets.QRadioButton(Dialog))
                o = getattr(self, a)
                o.setGeometry(QtCore.QRect(x, y, 300, 20))
                o.setObjectName(a)

                if self.type == "form":
                    o.clicked.connect(partial(sentence_to_audio, c))
                elif self.type == 'select':
                    o.clicked.connect(partial(play, self.tts[i - 1]))
                
                self.widgets.append([o, c])
                
                y += 30
            

        self.feedback = QtWidgets.QLabel(Dialog)
        self.feedback.setGeometry(QtCore.QRect(30, 230, 340, 16))
        self.feedback.setObjectName("feedback")
        self.feedback.setAlignment(QtCore.Qt.AlignCenter)
        self.widgets.append([self.feedback, ""])
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        log.info(f"Loaded {self.type} challenge")
        
    def check_answer(self):
        if self.type in ["form", "select", "judge"] and getattr(self, f"radioBox_{self.corr + 1}").isChecked():
            self.check.setText("Next")
            self.check.clicked.disconnect()
            self.check.clicked.connect(self.master.next)
            self.check.repaint()

            self.feedback.setStyleSheet("background-color: #00FF00")
            self.feedback.setText(f"Translation: {self.trans}")
        else:
            self.feedback.setStyleSheet("background-color: #fc4103")
            self.feedback.setText(f"Nope!")
            
        self.feedback.repaint()

    def retranslateUi(self, Dialog):
        t = QtWidgets.QApplication.translate
        Dialog.setWindowTitle(t(self.title, self.title, None, -1))
        for w, s in self.widgets:
            w.setText(t("Dialog", s, None, -1))

class Challenges:
    def __init__(self):
        self.qs = [i for i in get_challenges(cls=GuiChallenge) if i.type in implemented]
        shuffle(self.qs)
        self.idx = 0
    
    def setupUi(self, Dialog):
        self.widgets = []
        self.master = Dialog
        
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.stackedWidget.setObjectName("stackedWidget")

        self.windows = []
        for q in self.qs:
            self.windows.append(QtWidgets.QWidget(Dialog))
            q.setupUi(self.windows[-1])
            q.master = self

            self.stackedWidget.addWidget(self.windows[-1]) 

    def next(self):
        if self.idx < len(self.qs):
            self.stackedWidget.setCurrentIndex(self.idx + 1)
            self.idx += 1
        
class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.c = Challenges()
        self.c.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec_())
