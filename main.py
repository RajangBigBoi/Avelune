import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Night Audit Copilot")
        self.resize(1000, 700)

        label = QLabel("Night Audit Copilot\nMVP starting point")
        label.setStyleSheet("font-size: 24px; padding: 30px;")
        self.setCentralWidget(label)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
