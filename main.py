import sys
import os
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PySide6.QtCore import QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon
from ui.ui_station_add_file import Ui_MainWindow
from PySide6 import QtCore

from Function import AppFunction

# ---------------------------------------------------------------------------------------------------------------------------------------------------
from PySide6.QtWidgets import QFileDialog,QTableWidgetItem,  QTableWidget, QVBoxLayout, QWidget, QLabel
import pandas as pd
# ---------------------------------------------------------------------------------------------------------------------------------------------------


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.styles = self.load_styles("json/style.json")#

        self.apply_global_styles()

        self.button_group = QButtonGroup(self)
        for button_name in self.styles["QPushButtonGroup"]["Buttons"]:
            button = getattr(self.ui, button_name, None)
            if button:
                self.button_group.addButton(button)

        self.button_group.buttonClicked.connect(self.on_button_clicked)

        self.apply_default_styles()


        self.ui.menu_btn.clicked.connect(lambda:self.slide_left_menu())

        # ---------------------------------------------------------------------------------------------------------------------------------------------------
        self.ui.pushButton.clicked.connect(self.open_file_dialog)

# ---------------------------------------------------------------------------------------------------------------------------------------------------


        # self.ui.pushback.clicked.connect(lambda:self.slide_right_menu())

        
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page)
        # Подключаем кнопки к методам
        self.ui.home_btn.clicked.connect(self.show_home_page)
        self.ui.reports_btn.clicked.connect(self.show_report_page)
        self.ui.settings_btn.clicked.connect(self.show_settings_page)


        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'DB/s.db'))
        AppFunction.main(dbFolder)
        # AppFunction.displayUsers(self, AppFunction.getAllUsers(dbFolder))
        # self.ui.add_user_btn.clicked.connect(lambda: AppFunction.addUser(self, dbFolder))


# ---------------------------------------------------------------------------------------------------------------------------------------------------
    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        if not file_name:
            return 
        self.ui.label_10.setText(f"Selected file: {file_name}")

        # Чтение CSV-файла с помощью pandas
        df = pd.read_csv(file_name)

        # Отображение данных в таблице
        self.ui.tableWidget.setRowCount(df.shape[0])  # Количество строк
        self.ui.tableWidget.setColumnCount(df.shape[1])  # Количество столбцов
        self.ui.tableWidget.setHorizontalHeaderLabels(df.columns)  # Заголовки столбцов

        # Заполнение таблицы данными
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))
# ---------------------------------------------------------------------------------------------------------------------------------------------------




    def slide_left_menu(self):
        width = self.ui.left_menu.width()
        if width == 0:
            new_width = 200
        else:
            new_width = 0

        # Создаем анимацию для minimumWidth
        self.animation_min = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation_min.setDuration(250)
        self.animation_min.setStartValue(width)
        self.animation_min.setEndValue(new_width)
        self.animation_min.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # Создаем анимацию для maximumWidth
        self.animation_max = QPropertyAnimation(self.ui.left_menu, b"maximumWidth")
        self.animation_max.setDuration(250)
        self.animation_max.setStartValue(width)
        self.animation_max.setEndValue(new_width)
        self.animation_max.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # Запускаем анимации последовательно
        self.animation_min.start()
        self.animation_max.start()

        
    def slide_right_menu(self):
        width = self.ui.right_menu.width()
        if width == 0:
            new_width = 200
        else:
            new_width = 0

        # Создаем анимацию для minimumWidth
        self.animation_min = QPropertyAnimation(self.ui.right_menu, b"minimumWidth")
        self.animation_min.setDuration(250)
        self.animation_min.setStartValue(width)
        self.animation_min.setEndValue(new_width)
        self.animation_min.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # Создаем анимацию для maximumWidth
        self.animation_max = QPropertyAnimation(self.ui.right_menu, b"maximumWidth")
        self.animation_max.setDuration(250)
        self.animation_max.setStartValue(width)
        self.animation_max.setEndValue(new_width)
        self.animation_max.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # Запускаем анимации последовательно
        self.animation_min.start()
        self.animation_max.start()

        
    def load_styles(self, style_file):
        with open(style_file, 'r') as f:
            return json.load(f)
        
    def apply_global_styles(self):
        style_string = ""
        for widget, properties in self.styles.items():
            if widget != "QPushButtonGroup":
                style_string += f"{widget} {{"
                for property, value in properties.items():
                    style_string += f"{property}: {value}; "
                style_string += "}"
        self.setStyleSheet(style_string)

    def apply_default_styles(self):
        not_active_style = self.styles["QPushButtonGroup"]["Style"]["NotActive"]
        for button_name in self.styles["QPushButtonGroup"]["Buttons"]:
            button = getattr(self.ui, button_name, None)
            if button:
                button.setStyleSheet(not_active_style)

    def on_button_clicked(self, button):
        active_style = self.styles["QPushButtonGroup"]["Style"]["Active"]
        not_active_style = self.styles["QPushButtonGroup"]["Style"]["NotActive"]

        for btn in self.button_group.buttons():
            btn.setStyleSheet(not_active_style)
        button.setStyleSheet(active_style)  


    def show_home_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)  # Показать первую страницу

    def show_report_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)  # Показать вторую страницу

    def show_settings_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)  # Показать страницу настроек


  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
