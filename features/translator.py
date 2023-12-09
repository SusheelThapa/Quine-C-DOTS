import sys
import threading
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QSplitter,
    QTextBrowser,
    QComboBox,
)
from PyQt5.QtCore import QTimer, pyqtSignal, QObject
from PyQt5.QtGui import QFont, QTextCursor

from api import translator


class Worker(QObject):
    finished = pyqtSignal(str)

    def __init__(self, source_language, target_language, code):
        super().__init__()
        self.source_language = source_language
        self.target_language = target_language
        self.code = code

    def run(self):
        processed_text = translator(
            self.code, self.source_language, self.target_language
        )
        self.finished.emit(processed_text)


class CodeTranslator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.typing_timer = QTimer(self)
        self.typing_timer.timeout.connect(self.type_next_character)
        self.current_typing_position = 0
        self.processed_text = "" 

    def init_ui(self):
        self.setWindowTitle("Code Translator")
        self.setGeometry(100, 100, 1500, 900)
        self.setStyleSheet("background-color: #FFFFFF; color: #000000;")

        main_layout = QHBoxLayout()
        self.setup_main_layout(main_layout)
        self.setLayout(main_layout)

    def setup_main_layout(self, main_layout):
        main_layout.setContentsMargins(20, 20, 20, 20)
        left_layout = self.setup_left_layout()
        right_layout = self.setup_right_layout()

        splitter = QSplitter()
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        splitter.setSizes([400, 800])

        main_layout.addWidget(splitter)

    def setup_left_layout(self):
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(10, 20, 10, 20)
        left_layout.setSpacing(20)

        source_lang_label = self.create_label("Select Source Programming Language:")
        self.source_lang_selection = self.create_combobox(
            ["Python", "Java", "C++", "JavaScript", "C"]
        )
        target_lang_label = self.create_label("Select Target Programming Language:")
        self.target_lang_selection = self.create_combobox(
            ["Python", "Java", "C++", "JavaScript", "C"]
        )
        code_label = self.create_label("Code Snippets:")
        self.code_entry = self.create_text_edit()
        translate_button = self.create_button(
            "Translate Code", self.generate_translate_code
        )

        left_layout.addWidget(source_lang_label)
        left_layout.addWidget(self.source_lang_selection)
        left_layout.addWidget(target_lang_label)
        left_layout.addWidget(self.target_lang_selection)
        left_layout.addWidget(code_label)
        left_layout.addWidget(self.code_entry)
        left_layout.addWidget(translate_button)

        return left_layout

    def setup_right_layout(self):
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(10, 10, 10, 10)
        self.generated_text_area = self.create_text_browser()
        right_layout.addWidget(self.generated_text_area)

        return right_layout

    def create_label(self, text):
        label = QLabel(text)
        label.setFont(QFont("Arial", 16))
        return label

    def create_combobox(self, items):
        combobox = QComboBox()
        combobox.setFont(QFont("Arial", 16))
        combobox.addItems(items)
        combobox.setStyleSheet(
            "padding: 5px; background-color: #F0E6F4; color: #303030;"
        )
        return combobox

    def create_text_edit(self):
        text_edit = QTextEdit()
        text_edit.setFont(QFont("Arial", 16))
        text_edit.setStyleSheet(
            "border-radius: 5px; padding: 5px; background-color: #F0E6F4; color: #303030;"
        )
        return text_edit

    def create_button(self, text, callback):
        button = QPushButton(text)
        button.setFont(QFont("Arial", 18))
        button.clicked.connect(callback)
        button.setStyleSheet(
            """
                QPushButton {
                    border-radius: 10px;
                    padding: 10px;
                    background-color: #6A1B9A;
                    color: #FFFFFF;
                    font-weight:600;
                }
                QPushButton:hover {
                    background-color: #6A1B9A;
                }
            """
        )
        return button

    def create_text_browser(self):
        text_browser = QTextBrowser()
        text_browser.setReadOnly(True)
        text_browser.setFont(QFont("Arial", 16))
        text_browser.setStyleSheet(
            "border-radius: 5px; padding: 5px; background-color: #F0E6F4; color: #303030;"
        )
        return text_browser

    def generate_translate_code(self):
        source_lang = self.source_lang_selection.currentText()
        target_lang = self.target_lang_selection.currentText()
        code = self.code_entry.toPlainText()

        self.generated_text_area.setText(
            f"Translating Code Snippet from {source_lang} to {target_lang}..."
        )

        self.worker = Worker(source_lang, target_lang, code)
        self.thread = threading.Thread(target=self.worker.run)
        self.worker.finished.connect(self.on_finished)
        self.thread.start()

    def on_finished(self, processed_text):
        self.processed_text = processed_text
        self.current_typing_position = 0
        self.typing_timer.start(20)

    def type_next_character(self):
        if self.current_typing_position < len(self.processed_text):
            if self.current_typing_position == 0:
                self.generated_text_area.clear()

            current_text = self.processed_text[self.current_typing_position]
            self.generated_text_area.moveCursor(QTextCursor.End)
            self.generated_text_area.insertPlainText(current_text)
            self.current_typing_position += 1
        else:
            self.typing_timer.stop()  


def main():
    app = QApplication(sys.argv)
    translator = CodeTranslator()
    translator.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
