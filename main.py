from AnthonyLaraTroche1 import *
from PyQt6.QtWidgets import QApplication
def main():
    application = QApplication([])
    window = Vote()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
