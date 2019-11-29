from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import shutil
import pickle
from datetime import datetime
from settings import Ui_SettingsWindow
import threading
from time import sleep


class Ui_MainWindow(object):
    def __init__(self):
        self.popup_status = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 235)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 400))
        MainWindow.setMaximumSize(QtCore.QSize(100000, 50000))
        font = QtGui.QFont()
        font.setFamily("MS Reference Specialty")
        font.setPointSize(17)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("* {\n"
                                 "    color: white;\n"
                                 "}\n"
                                 "\n"
                                 ".QMainWindow, QScrollArea {\n"
                                 "    background-color: rgb(40, 40, 40);\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 ".QLineEdit, #scrollAreaWidgetContents {\n"
                                 "    background-color: rgb(60, 60, 60);\n"
                                 "    border-radius: 5px;\n"
                                 "    padding: 0 6;\n"
                                 "}\n"
                                 "\n"
                                 ".QPushButton{\n"
                                 "    border-radius: 7px;\n"
                                 "    background-color: rgb(60, 60, 60);\n"
                                 "    padding: 0 5;\n"
                                 "    color: rgb(255, 44, 44);\n"
                                 "}\n"
                                 "\n"
                                 ".QPushButton:hover {\n"
                                 "    background-color: rgb(50, 50, 50);\n"
                                 "}\n"
                                 "\n"
                                 "#clearButton, #browserButton {\n"
                                 "    color: white;\n"
                                 "    border-radius: 20px;\n"
                                 "}\n"
                                 "\n"
                                 "#browserButton {\n"
                                 "    border-radius: 7px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar {\n"
                                 "    background-color: rgb(40, 40, 40);\n"
                                 "}\n"
                                 "\n"
                                 "#settingsButton {\n"
                                 "    background-color: none;\n"
                                 "    margin-top: -7px;\n"
                                 "    margin-left: -10px;\n"
                                 "}")

        # centralWidget

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")

        # topWidget

        self.topWidget = QtWidgets.QHBoxLayout()
        self.topWidget.setContentsMargins(-1, -1, -1, 0)
        self.topWidget.setSpacing(0)
        self.topWidget.setObjectName("topWidget")

        # mainLabel

        self.mainLabel = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainLabel.sizePolicy().hasHeightForWidth())
        self.mainLabel.setSizePolicy(sizePolicy)
        self.mainLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("8BIT WONDER")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.mainLabel.setFont(font)
        self.mainLabel.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.mainLabel.setStyleSheet("")
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setObjectName("mainLabel")
        self.topWidget.addWidget(self.mainLabel)

        # settingsButton

        self.settingsButton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy)
        self.settingsButton.setMinimumSize(QtCore.QSize(30, 0))
        self.settingsButton.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.settingsButton.setFont(font)
        self.settingsButton.setObjectName("settingsButton")
        self.topWidget.addWidget(self.settingsButton)
        self.verticalLayout.addLayout(self.topWidget)
        self.settingsButton.clicked.connect(self.open_settings)

        # middleWidget

        self.middleWidget = QtWidgets.QHBoxLayout()
        self.middleWidget.setSpacing(20)
        self.middleWidget.setObjectName("middleWidget")

        # dirLineEdit

        self.dirLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dirLineEdit.sizePolicy().hasHeightForWidth())
        self.dirLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.dirLineEdit.setFont(font)
        self.dirLineEdit.setObjectName("dirLineEdit")
        self.middleWidget.addWidget(self.dirLineEdit)

        # addButton

        self.addButton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("8BIT WONDER")
        self.addButton.setFont(font)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.add_button_clicked)
        self.middleWidget.addWidget(self.addButton)


        # browserButton

        self.browserButton = QtWidgets.QPushButton(self.centralWidget)
        self.browserButton.setSizePolicy(sizePolicy)
        self.browserButton.setMinimumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("8BIT WONDER")
        self.browserButton.setFont(font)
        self.browserButton.setAutoDefault(False)
        self.browserButton.setObjectName("browserButton")
        self.browserButton.clicked.connect(self.open_file_browser)
        self.middleWidget.addWidget(self.browserButton)

        self.verticalLayout.addLayout(self.middleWidget)

        # bottomWidget

        self.bottomWidget = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy)
        self.bottomWidget.setMaximumSize(QtCore.QSize(16777215, 400))
        self.bottomWidget.setStyleSheet("")
        self.bottomWidget.setObjectName("bottomWidget")

        # horizontalLayout

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottomWidget)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # scrollArea

        self.scrollArea = QtWidgets.QScrollArea(self.bottomWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # scrollAreaWidgetContents

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 300, 69))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # formLayout

        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")

        # scrollArea

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        # clearButton

        self.clearButton = QtWidgets.QPushButton(self.bottomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(150, 0))
        self.clearButton.setMaximumSize(QtCore.QSize(16777215, 400))
        font = QtGui.QFont()
        font.setFamily("8BIT WONDER")
        font.setPointSize(13)
        self.clearButton.setFont(font)
        self.clearButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clearButton.setStyleSheet("")
        self.clearButton.setAutoDefault(False)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.clearButton.clicked.connect(self.clear_button_clicked)

        # ------------------

        self.verticalLayout.addWidget(self.bottomWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # trayIcon

        self.trayIcon = QtWidgets.QSystemTrayIcon()
        self.trayIcon.setIcon(MainWindow.style().standardIcon(QtWidgets.QStyle.SP_DialogResetButton))
        show_action = QtWidgets.QAction("Show", MainWindow)
        quit_action = QtWidgets.QAction("Exit", MainWindow)
        hide_action = QtWidgets.QAction("Hide", MainWindow)
        show_action.triggered.connect(MainWindow.show)
        hide_action.triggered.connect(MainWindow.hide)
        quit_action.triggered.connect(MainWindow.close)
        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.trayIcon.setContextMenu(tray_menu)
        self.trayIcon.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Cleaner"))
        self.mainLabel.setText(_translate("MainWindow", "Enter directory for cleaning"))
        self.settingsButton.setText(_translate("MainWindow", "⚙"))
        self.addButton.setText(_translate("MainWindow", "ADD"))
        self.browserButton.setText(_translate("MainWindow", "Browse"))
        self.clearButton.setText(_translate("MainWindow", "START"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

    def clear_button_clicked(self, skip_alert=False):

        user_data = self.get_user_data()
        if not user_data['dirs']:
            self.mainLabel.setText('No paths added')
        else:
            if not skip_alert:
                self.show_popup()
            if self.popup_status or skip_alert:
                files_deleted = 0
                files_size = 0
                for path in user_data['dirs']:
                    if os.path.isdir(path):
                        files = os.listdir(path)
                        for file in files:
                            try:
                                file_path = os.path.join(path, file)
                                files_size += int(os.path.getsize(file_path))
                                if os.path.isfile(file_path):
                                    os.remove(file_path)
                                    files_deleted += 1
                                else:
                                    shutil.rmtree(file_path)
                            except PermissionError:
                                pass
                    else:
                        self.mainLabel.setText('Invalid Path')

                # Label changing

                if files_deleted == 0:
                    self.mainLabel.setText('No files deleted')
                elif files_deleted == 1:
                    self.mainLabel.setText(str(files_deleted) + ' file deleted (' +
                                           self.get_file_size(files_size) + ')')
                else:
                    self.mainLabel.setText(str(files_deleted) + ' files deleted ( ' +
                                           self.get_file_size(files_size) + ' )')

                user_data['last_clean'] = datetime.now()
                self.load_user_data(user_data)
            else:
                self.mainLabel.setText("Enter directory for cleaning")

    def add_button_clicked(self):
        path = self.dirLineEdit.text()

        if os.path.isdir(path):
            user_data = self.get_user_data()
            user_data['dirs'].append(path)
            self.load_user_data(user_data)

            self.mainLabel.setText("Enter directory for cleaning")
            self.update_scroll_area()
        else:
            self.mainLabel.setText('Invalid Path')
        self.dirLineEdit.setText("")

    def update_scroll_area(self):

        while self.formLayout.count() != 0:
            self.formLayout.removeRow(0)

        for n in range(0, len(self.get_user_data()['dirs'])):

            # xButton

            self.x_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.x_button.sizePolicy().hasHeightForWidth())
            self.x_button.setSizePolicy(sizePolicy)
            self.x_button.setMinimumSize(QtCore.QSize(0, 0))
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setWeight(75)
            self.x_button.setFont(font)
            self.x_button.setObjectName('xButton_' + str(n))
            self.x_button.setText("X")
            self.x_button.clicked.connect(lambda: self.remove_dir(n))

            self.formLayout.setWidget(n, QtWidgets.QFormLayout.LabelRole, self.x_button)

            # checkBox

            self.check_box = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            font.setPointSize(7)
            self.check_box.setFont(font)
            self.check_box.setObjectName('checkBox_' + str(n))
            self.check_box.setText(self.get_user_data()['dirs'][n])

            self.formLayout.setWidget(n, QtWidgets.QFormLayout.FieldRole, self.check_box)

    def remove_dir(self, n):
        user_data = self.get_user_data()
        user_data['dirs'].pop(n)
        self.load_user_data(user_data)
        self.update_scroll_area()

    def get_user_data(self):
        with open('user.data', 'rb') as file:
            return pickle.load(file)

    def load_user_data(self, user_data):
        with open('user.data', 'wb') as file:
            pickle.dump(user_data, file)

    def reset_user_data(self):
        with open('user.data', 'wb') as file:
            pickle.dump({'dirs': [],
                         'settings': {'win_start': True,
                                      'auto_clean': 'week'},
                         'last_clean': {}}, file)

    def get_file_size(self, file_size):
        file_size = file_size/1024
        ending = 'KB'
        if file_size >= 1024:
            file_size /= 1024
            ending = 'MB'
        if file_size >= 1024:
            file_size /= 1024
            ending = 'GB'
        file_size = round(file_size, 2)

        return str(file_size) + ' ' + ending

    def show_popup(self):
        popup = QtWidgets.QMessageBox()
        popup.setWindowTitle('Warning!')
        popup.setText('Do you really want to start?')
        popup.setIcon(QtWidgets.QMessageBox.Warning)
        popup.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        popup.setDefaultButton(QtWidgets.QMessageBox.No)
        popup.buttonClicked.connect(self.popup_button_pressed)
        popup.exec_()

    def popup_button_pressed(self, button):
        if button.text() == '&No':
            self.popup_status = False
        else:
            self.popup_status = True

    def open_file_browser(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        filename = filename[0].split('/')
        filename.pop(-1)
        filename = '/'.join(filename)
        self.dirLineEdit.setText(filename)

    def open_settings(self):
        self.settingsWindow = QtWidgets.QMainWindow()
        self.settingsUi = Ui_SettingsWindow()
        self.settingsUi.setupUi(self.settingsWindow)
        self.settingsUi.update_ui()
        self.settingsWindow.show()

    def auto_cleaning(self):
        while True:
            interval = self.get_user_data()['settings']['auto_clean']
            last_clean = self.get_user_data()['last_clean']
            last_clean = datetime(2019, 11, 28)
            delta = datetime.now() - last_clean
            if (interval == 'hour' and (delta.seconds / 3600) >= 1) or \
                    (interval == 'day' and delta.days >= 1) or \
                    (interval == 'week' and delta.days >= 7) or \
                    (interval == '2weeks' and delta.days >= 14) or \
                    (interval == 'month' and delta.days >= 30):
                self.clear_button_clicked(True)
                print('auto cleared')
            print('checked')
            sleep(10)

    def start_threads(self):
        auto_cleaner = threading.Thread(target=self.auto_cleaning, name='auto_cleaner')
        auto_cleaner.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.update_scroll_area()
    ui.start_threads()
    MainWindow.show()
    sys.exit(app.exec_())
