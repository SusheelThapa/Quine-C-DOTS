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
    QGroupBox,
    QScrollArea,
    QComboBox,
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont, QTextCursor

from PyQt5.QtGui import QFont
from api import summarizer


class CodeSummarizer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.typing_timer = QTimer(self)
        self.typing_timer.timeout.connect(self.type_next_character)
        self.current_typing_position = 0

    def init_ui(self):
        self.setWindowTitle("Code Summarizer")
        self.setGeometry(100, 100, 1500, 900)
        self.setStyleSheet("background-color: #FFFFFF; color: #000000;")

        # Main layout setup
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Left layout for inputs
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(10, 20, 10, 20)
        left_layout.setSpacing(20)

        # Right layout for output
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(10, 10, 10, 10)

        splitter = QSplitter()

        # Programming Language Selection with styled dropdown
        language_label = QLabel("Select Programming Language:")
        language_label.setFont(QFont("Arial", 16))

        self.language_selection = QComboBox()
        self.language_selection.setFont(QFont("Arial", 16))
        self.language_selection.setStyleSheet(
            "QComboBox {  padding: 8px; background-color: #F2EFEF; color: #202020; }"
        )
        self.language_selection.addItems(["Python", "Java", "C++", "JavaScript", "C"])

        # Code Entry with styled text box
        code_label = QLabel("Code to Summarize")
        code_label.setFont(QFont("Arial", 16))

        self.code_entry = QTextEdit()
        self.code_entry.setFont(QFont("Arial", 16))
        self.code_entry.setStyleSheet(
            "QTextEdit { border-radius: 5px; padding: 5px; background-color: #F2EFEF; color: #202020; }"
        )

        # Generate Documentation Button with styled button
        generate_summarize_button = QPushButton("Summarize Code")
        generate_summarize_button.setFont(QFont("Arial", 18))
        generate_summarize_button.setStyleSheet(
            "QPushButton { border-radius: 10px; padding: 10px; background-color: #601527; color: #FFFFFF; font-weight:600; } QPushButton:hover { background-color: #601527; }"
        )
        generate_summarize_button.clicked.connect(self.summarize_code)

        # Add widgets to left layout
        left_layout.addWidget(language_label)
        left_layout.addWidget(self.language_selection)
        left_layout.addWidget(code_label)
        left_layout.addWidget(self.code_entry)
        left_layout.addWidget(generate_summarize_button)

        # Right side: group box to hold generated article text area with styled text browser
        self.generated_text_area = QTextBrowser()
        self.generated_text_area.setReadOnly(True)
        self.generated_text_area.setFont(QFont("Arial", 16))
        self.generated_text_area.setStyleSheet(
            "QTextBrowser { border-radius: 5px; padding: 5px; background-color: #F2EFEF; color: #202020; }"
        )

        
        right_layout.addWidget(self.generated_text_area)

        # Assembling the main layout
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        right_widget = QWidget()
        right_widget.setLayout(right_layout)

        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        splitter.setSizes([400, 800])

        main_layout.addWidget(splitter)
        self.setLayout(main_layout)

    def summarize_code(self):
        language = self.language_selection.currentText()
        code = self.code_entry.toPlainText()
        self.processed_text = self.process_code_for_summarizing_code(language, code)
        self.generated_text_area.clear()  # Clear the text area before starting
        self.current_typing_position = 0
        self.typing_timer.start(20)  # Adjust speed as needed

    def type_next_character(self):
        if self.current_typing_position < len(self.processed_text):
            current_text = self.processed_text[self.current_typing_position]
            self.generated_text_area.moveCursor(
                QTextCursor.End
            )  # Move cursor to the end
            self.generated_text_area.insertPlainText(current_text)
            self.current_typing_position += 1
        else:
            self.typing_timer.stop()  # Stop typing when done

    def process_code_for_summarizing_code(self, language, code):
        response = summarizer(code, language)

        # This is a placeholder for your code processing logic
        return f"{response}"  # Example output


def main():
    app = QApplication(sys.argv)
    generator = CodeSummarizer()
    generator.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
