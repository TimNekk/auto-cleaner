from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import shutil


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 235)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(510, 235))
        MainWindow.setMaximumSize(QtCore.QSize(510, 235))
        font = QtGui.QFont()
        font.setFamily("MS Reference Specialty")
        font.setPointSize(17)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("* {\n"
                                 "    color: white;\n"
                                 "}\n"
                                 "\n"
                                 ".QMainWindow {\n"
                                 "    background-color: rgb(40, 40, 40);\n"
                                 "}\n"
                                 "\n"
                                 ".QLabel {\n"
                                 "}\n"
                                 "\n"
                                 ".QLineEdit {\n"
                                 "    background-color: rgb(60, 60, 60);\n"
                                 "    border-radius: 5px;\n"
                                 "    padding: 0 6;\n"
                                 "}\n"
                                 "\n"
                                 ".QPushButton {\n"
                                 "    border-radius: 20px;\n"
                                 "    background-color: rgb(60, 60, 60);\n"
                                 "    transition-duration: 1s;\n"
                                 "}\n"
                                 "\n"
                                 ".QPushButton:hover {\n"
                                 "    background-color: rgb(50, 50, 50);\n"
                                 "}\n"
                                 "")

        # centralWidget

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")

        # verticalLayout

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        # mainLabel

        self.mainLabel = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("8BIT WONDER")
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.mainLabel.setFont(font)
        self.mainLabel.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.mainLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainLabel.setStyleSheet("")
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setObjectName("mainLabel")
        self.verticalLayout.addWidget(self.mainLabel)

        # dirLineEdit

        self.dirLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dirLineEdit.sizePolicy().hasHeightForWidth())
        self.dirLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.dirLineEdit.setFont(font)
        self.dirLineEdit.setObjectName("dirLineEdit")
        self.verticalLayout.addWidget(self.dirLineEdit)

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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottomWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # clearButton

        self.clearButton = QtWidgets.QPushButton(self.bottomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(200, 0))
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
        self.verticalLayout.addWidget(self.bottomWidget)
        self.clearButton.clicked.connect(self.clear_button_clicked)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainLabel.setText(_translate("MainWindow", "Enter directory for cleaning"))
        self.clearButton.setText(_translate("MainWindow", "START"))

    def clear_button_clicked(self):
        path = self.dirLineEdit.text()

        if os.path.isdir(path):
            files_deleted = 0
            files_amount = len(os.listdir(path))
            print('Очистка ' + str(files_amount) + ' файлов в дериктории:\n' + path)

            files = os.listdir(path)
            for file in files:
                try:
                    file_path = os.path.join(path, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        files_deleted += 1
                    else:
                        shutil.rmtree(file_path)
                except PermissionError:
                    pass

            print('\nУдаленно          ' + str(files_deleted) + ' файлов\nПроигнорированно  ' + str(
                files_amount - files_deleted) + ' файлов')
            self.mainLabel.setText('Done')

        else:
            self.mainLabel.setText('Invalid Path')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
