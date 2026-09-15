from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidget, QTableWidgetItem
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Organizacion de Alumnos")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        file_menu_item = self.menuBar().addMenu("&Archivo")
        help_menu_item = self.menuBar().addMenu("&Ayuda")

        add_student_action = QAction("Añadir Estdiante", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("Acerca de...", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Nombre", "Curso", "Numero"))
        self.setCentralWidget(self.table)

    def load_data(self):
        self.table

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())