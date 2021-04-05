import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QVBoxLayout, QLineEdit, QPushButton

from speech import Stt, Tts

app = QApplication(sys.argv)


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.recognised_text_box = QLineEdit()
        self.recognised_text_box.setReadOnly(True)
        self.start_listening = QPushButton('Start Listening')
        self.dictate_text = QPushButton('Dictate Text')
        self.layout.addWidget(self.recognised_text_box)
        self.layout.addWidget(self.start_listening)
        self.layout.addWidget(self.dictate_text)
        self.setLayout(self.layout)
        self.start_listening.clicked.connect(self.on_start_listening)
        self.dictate_text.clicked.connect(self.on_dictate_text_clicked)

    def on_start_listening(self):
        self.start_listening.setDisabled(True)
        stt = Stt()
        stt.signals.finished.connect(self.on_speech_recognized)
        stt.start()

    def on_speech_recognized(self, text):
        self.start_listening.setDisabled(False)
        self.recognised_text_box.setText(text)

    def on_dictate_text_clicked(self):
        self.dictate_text.setDisabled(True)
        tts = Tts(self.recognised_text_box.text())
        tts.signals.finished.connect(lambda: self.dictate_text.setDisabled(False))
        tts.start()


ui = UI()
ui.show()
sys.exit(app.exec_())
