from PySide2.QtWidgets   import QApplication, QMainWindow, QDialog
from converted.translate import Ui_Dialog
from base                import gen_words, sentence_to_audio, partial, src_lang, dest_lang, log
from random              import random
from sys                 import argv

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.form = Ui_Dialog()
        self.form.setupUi(self)

        self._initialize()
        
        log.info("Set up UI")

    def _initialize(self):
        self.translations = []
        
        for i, word in enumerate(gen_words(n=5), start=1):
            w, (tw, *_) = word
            lang = src_lang
            # if random() < 0.5:
            #     w, tw, lang = tw, w, dest_lang
            self.translations.append(tw)

            tb = getattr(self.form, f"label_{i}")
            tb.setText(w)
            tb.repaint()

            btn = getattr(self.form, f"commandLinkButton_{i}")
            try: btn.clicked.disconnect()
            except: pass
            btn.clicked.connect(partial(sentence_to_audio, w, lang))

            line = self.get_line(i - 1)
            line.setText("")
            self.set_color(line, "#FFFFFF")

        self.form.check.setText("Check")
        self.form.check.repaint()
        
        self._reconn(self.check)
        
        self.form.show.clicked.connect(self.show_)

    def check(self):
        log.debug("Received check")
        for i in range(5):
            line = self.get_line(i)
            ans, corr = line.text(), self.translations[i]

            self.set_color(line, "#00FF00" if ans == corr else "#FF0000")

        self.set_next()

    def show_(self):
        log.debug("Received show")
        for i in range(5):
            line = self.get_line(i)

            line.setText(self.translations[i])
            self.set_color(line, "#FFFFFF")

        self.set_next()

    def set_next(self):
        if all(self.get_line(i).text() == self.translations[i] for i in range(5)):
            self.form.check.setText("Next")
            self.form.check.repaint()
            self._reconn(self._initialize)
            log.info("All correct!")

    def get_line(self, i):
        return getattr(self.form, f"lineEdit_{i + 1}")
    
    def set_color(self, line, color):
        line.setStyleSheet(f"background-color: {color}")
        line.repaint()

    def _reconn(self, new):
        try: self.form.check.clicked.disconnect()
        except: pass
        self.form.check.clicked.connect(new)

        

if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec_())
