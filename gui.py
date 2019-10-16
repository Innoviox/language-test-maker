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

        self.translations = []
        
        for i, word in enumerate(gen_words(n=5), start=1):
            w, (tw, *_) = word
            lang = src_lang
            # if random() < 0.5:
            #     w, tw, lang = tw, w, dest_lang
            self.translations.append(tw)

            getattr(self.form, f"textBrowser_{i}").setText(w)
            getattr(self.form, f"commandLinkButton_{i}").clicked.connect(partial(sentence_to_audio, w, lang, i))

        self.form.check.clicked.connect(self.accept)
        self.form.show.clicked.connect(self.show_)

        log.info("Set up UI")

    def accept(self):
        for i in range(5):
            line = getattr(self.form, f"lineEdit_{i + 1}")
            ans, corr = line.text(), self.translations[i]
            
            if ans == corr:
                line.setStyleSheet("background-color: #00FF00")
            else:
                line.setStyleSheet("background-color: #FF0000")

            line.style().unpolish(line)
            line.style().polish(line)
            line.update()

    def show_(self):
        for i in range(5):
            line = getattr(self.form, f"lineEdit_{i + 1}")

            line.setText(self.translations[i])
            
            line.setStyleSheet("background-color: #FFFFFF")
            line.style().unpolish(line)
            line.style().polish(line)
            line.update()

        

if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec_())
