from PySide2.QtWidgets   import QApplication, QMainWindow, QDialog
from converted.translate import Ui_Dialog as translate_question
from converted.sentence  import Ui_Dialog as sentence_question
from base                import gen_words, sentence_to_audio, partial, src_lang, dest_lang, log
from random              import random
from sys                 import argv

class TransQ(translate_question):
    def initialize(self, master=None):
        if master: self.setupUi(master)
        
        selflations = []
        
        for i, word in enumerate(gen_words(n=5), start=1):
            w, (tw, *_) = word
            lang = src_lang
            # if random() < 0.5:
            #     w, tw, lang = tw, w, dest_lang
            selflations.append(tw)

            tb = getattr(self, f"label_{i}")
            tb.setText(w)
            tb.repaint()

            btn = getattr(self, f"commandLinkButton_{i}")
            try: btn.clicked.disconnect()
            except: pass
            btn.clicked.connect(partial(sentence_to_audio, w, lang))

            line = self.get_line(i - 1)
            line.setText("")
            self.set_color(line, "#FFFFFF")

        self.check.setText("Check")
        self.check.repaint()
        
        self._reconn(self.check_)
        
        self.show.clicked.connect(self.show_)

    def check_(self):
        log.debug("Received check")
        for i in range(5):
            line = self.get_line(i)
            ans, corr = line.text(), selflations[i]

            self.set_color(line, "#00FF00" if ans == corr else "#FF0000")

        self.set_next()

    def show_(self):
        log.debug("Received show")
        for i in range(5):
            line = self.get_line(i)

            line.setText(selflations[i])
            self.set_color(line, "#FFFFFF")

        self.set_next()

    def set_next(self):
        if all(self.get_line(i).text() == selflations[i] for i in range(5)):
            self.check.setText("Next")
            self.check.repaint()
            self._reconn(self.initialize)
            log.info("All correct!")

    def get_line(self, i):
        return getattr(self, f"lineEdit_{i + 1}")
    
    def set_color(self, line, color):
        line.setStyleSheet(f"background-color: {color}")
        line.repaint()

    def _reconn(self, new):
        try: self.check.clicked.disconnect()
        except: pass
        self.check.clicked.connect(new)

class SentQ(sentence_question):
    def initialize(self, master=None):
        if master: self.setupUi(master)

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.trans = TransQ()
        self.trans.initialize(master=self)

        log.info("Set up UI")

if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec_())
