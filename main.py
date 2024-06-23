import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.uic import loadUi


class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("design.ui", self)  # შემოვიტანეთ დიზაინის ფაილი

        self.image_files = []
        self.folder.clicked.connect(self.open_folder)
        self.current_folder = ""

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "აირჩიეთ ფოლდერი")
        if folder:
            self.current_folder = folder
            self.image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            self.file_list.clear()
            self.file_list.addItems(self.image_files)


app = QApplication([])
window = EditorWindow()
window.show()
app.exec_()
