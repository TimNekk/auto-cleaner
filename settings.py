from PyQt5 import QtCore, QtGui, QtWidgets
import pickle

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(214, 169)
        SettingsWindow.setMinimumSize(QtCore.QSize(214, 200))
        SettingsWindow.setMaximumSize(QtCore.QSize(214, 200))
        SettingsWindow.setStyleSheet("* {\n"
                                     "    color: white;\n"
                                     "}\n"
                                     "\n"
                                     ".QMainWindow {\n"
                                     "    background-color: rgb(40, 40, 40);\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "\n"
                                     ".QPushButton {\n"
                                     "    border-radius: 7px;\n"
                                     "    background-color: rgb(60, 60, 60);\n"
                                     "    transition-duration: 1s;\n"
                                     "    padding: 0 5;\n"
                                     "    color: rgb(255, 44, 44);\n"
                                     "}\n"
                                     "\n"
                                     ".QPushButton:hover {\n"
                                     "    background-color: rgb(50, 50, 50);\n"
                                     "}")

        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.startCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.startCheckbox.setGeometry(QtCore.QRect(18, 9, 114, 17))
        self.startCheckbox.setObjectName("startCheckbox")
        self.startCheckbox.setChecked(True)

        self.minimizedCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.minimizedCheckbox.setGeometry(QtCore.QRect(18, 30, 130, 17))
        self.minimizedCheckbox.setObjectName("minimizedCheckbox")
        self.minimizedCheckbox.setChecked(True)

        self.hourButton = QtWidgets.QRadioButton(self.centralwidget)
        self.hourButton.setGeometry(QtCore.QRect(18, 75, 82, 17))
        self.hourButton.setObjectName("HourButton")

        self.dayButton = QtWidgets.QRadioButton(self.centralwidget)
        self.dayButton.setGeometry(QtCore.QRect(18, 93, 82, 17))
        self.dayButton.setObjectName("DayButton")

        self.weekButton = QtWidgets.QRadioButton(self.centralwidget)
        self.weekButton.setGeometry(QtCore.QRect(18, 111, 82, 17))
        self.weekButton.setChecked(True)
        self.weekButton.setObjectName("weekButton")

        self.twoWeeksButton = QtWidgets.QRadioButton(self.centralwidget)
        self.twoWeeksButton.setGeometry(QtCore.QRect(18, 129, 82, 17))
        self.twoWeeksButton.setObjectName("twoWeeksButton")

        self.monthButton = QtWidgets.QRadioButton(self.centralwidget)
        self.monthButton.setGeometry(QtCore.QRect(18, 147, 82, 17))
        self.monthButton.setObjectName("MonthButton")

        self.disableButton = QtWidgets.QRadioButton(self.centralwidget)
        self.disableButton.setGeometry(QtCore.QRect(18, 165, 82, 17))
        self.disableButton.setObjectName("DisableButton")

        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(18, 57, 83, 13))
        self.mainLabel.setObjectName("mainLabel")

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(126, 156, 75, 23))
        font = QtGui.QFont()
        font.setFamily("8BIT WONDER")
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("resetButton")
        self.saveButton.clicked.connect(self.save_settings)

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.startCheckbox.setText(_translate("SettingsWindow", "Start with windows"))
        self.minimizedCheckbox.setText(_translate("SettingsWindow", "Start minimized to tray"))
        self.hourButton.setText(_translate("SettingsWindow", "Hour"))
        self.dayButton.setText(_translate("SettingsWindow", "Day"))
        self.weekButton.setText(_translate("SettingsWindow", "Week"))
        self.twoWeeksButton.setText(_translate("SettingsWindow", "2 Weeks"))
        self.monthButton.setText(_translate("SettingsWindow", "Month"))
        self.mainLabel.setText(_translate("SettingsWindow", "Auto-clean every:"))
        self.disableButton.setText(_translate("SettingsWindow", "Disable"))
        self.saveButton.setText(_translate("SettingsWindow", "Save"))

    def save_settings(self):
        user_data = self.get_user_data()
        if self.hourButton.isChecked():
            user_data['settings']['auto_clean'] = 'hour'
        elif self.dayButton.isChecked():
            user_data['settings']['auto_clean'] = 'day'
        elif self.weekButton.isChecked():
            user_data['settings']['auto_clean'] = 'week'
        elif self.twoWeeksButton.isChecked():
            user_data['settings']['auto_clean'] = '2weeks'
        elif self.monthButton.isChecked():
            user_data['settings']['auto_clean'] = 'month'
        elif self.disableButton.isChecked():
            user_data['settings']['auto_clean'] = 'disable'
        if self.startCheckbox.isChecked():
            user_data['settings']['win_start'] = True
        else:
            user_data['settings']['win_start'] = False
        if self.minimizedCheckbox.isChecked():
            user_data['settings']['min_start'] = True
        else:
            user_data['settings']['min_start'] = False
        self.load_user_data(user_data)

    def update_ui(self):
        user_data = self.get_user_data()
        if user_data['settings']['auto_clean'] == 'day':
            self.dayButton.setChecked(True)
        elif user_data['settings']['auto_clean'] == 'week':
            self.weekButton.setChecked(True)
        elif user_data['settings']['auto_clean'] == '2weeks':
            self.twoWeeksButton.setChecked(True)
        elif user_data['settings']['auto_clean'] == 'month':
            self.monthButton.setChecked(True)
        elif user_data['settings']['auto_clean'] == 'hour':
            self.hourButton.setChecked(True)
        elif user_data['settings']['auto_clean'] == 'disable':
            self.disableButton.setChecked(True)
        if user_data['settings']['win_start']:
            self.startCheckbox.setChecked(True)
        else:
            self.startCheckbox.setChecked(False)
        if user_data['settings']['min_start']:
            self.minimizedCheckbox.setChecked(True)
        else:
            self.minimizedCheckbox.setChecked(False)

    def load_user_data(self, user_data):
        with open('user.data', 'wb') as file:
            pickle.dump(user_data, file)

    def get_user_data(self):
        with open('user.data', 'rb') as file:
            return pickle.load(file)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    ui.update_ui()
    SettingsWindow.show()
    sys.exit(app.exec_())
