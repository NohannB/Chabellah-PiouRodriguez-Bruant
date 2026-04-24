from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Clavier PyQt")

    def keyPressEvent(self, event):
        # Détecte la touche pressée
        if event.key() == Qt.Key_Z:
            print("Touche Z appuyée")

        # Détecte les combinaisons (ex: Ctrl + Z)
        if event.key() == Qt.Key_Z and event.modifiers() == Qt.ControlModifier:
            print("Ctrl + Z appuyé")

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Z:
            print("Touche Z relâchée")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
