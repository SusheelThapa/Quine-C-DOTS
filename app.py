import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QTabBar


from features.documenter import CodeDocumenter
from features.optimizer import CodeOptimizer
from features.summarizer import CodeSummarizer
from features.translator import CodeTranslator


class StretchedTabBar(QTabBar):
    def __init__(self, parent=None):
        super().__init__(parent)

    def tabSizeHint(self, index):
        size = super().tabSizeHint(index)
        if self.count() > 0:
            size.setWidth(self.parent().width() // self.count())
        return size


class CDOTSApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("C-DOTS: Your Coding Assistance")
        self.setGeometry(100, 100, 1600, 900)

        # Create the tab widget with a stretched tab bar
        tab_widget = QTabWidget()
        tab_widget.setTabBar(StretchedTabBar(tab_widget))
        tab_widget.setStyleSheet(
            """
            QTabBar::tab {
                background-color: #333333;
                color: #CCCCCC;
                padding: 15px;
                font-size:20px;
                font-weight:500;                
            }

            QTabBar::tab:selected {
                background: #007BFF;
                color: #FFFFFF;
            }

            QTabBar::tab:hover {
                background: #555555;
                color:#FFFFFF;
            }
        """
        )

        # Add tabs
        tab_widget.addTab(CodeDocumenter(), "Documenter")
        tab_widget.addTab(CodeOptimizer(), "Optimizer")
        tab_widget.addTab(CodeTranslator(), "Translator")
        tab_widget.addTab(CodeSummarizer(), "Summarizer")

        self.setCentralWidget(tab_widget)


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(
        "QMainWindow { background-color: #121212; } QWidget {  color: #FFFFFF; }"
    )
    ex = CDOTSApp()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
