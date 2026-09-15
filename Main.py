from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidget, QTableWidgetItem, QGridLayout, \
    QAbstractItemView
import sys
import sqlite3

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
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())