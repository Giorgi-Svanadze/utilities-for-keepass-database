from fpdf import FPDF
from pykeepass import PyKeePass
from cryptography.fernet import Fernet
from PyQt5 import QtCore, QtGui, QtWidgets
import os, shutil, json, winreg, sys, random, string, configparser, base64

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(305, 395)
        window.setMinimumSize(QtCore.QSize(305, 395))
        window.setStyleSheet("")
        self.widget = QtWidgets.QWidget(window)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.gr_util = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.gr_util.sizePolicy().hasHeightForWidth())
        self.gr_util.setSizePolicy(sizePolicy)
        self.gr_util.setAlignment(QtCore.Qt.AlignCenter)
        self.gr_util.setObjectName("gr_util")
        self.gr_grid = QtWidgets.QGridLayout(self.gr_util)
        self.gr_grid.setObjectName("gr_grid")
        self.gr_name = QtWidgets.QTextEdit(self.gr_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gr_name.sizePolicy().hasHeightForWidth())
        self.gr_name.setSizePolicy(sizePolicy)
        self.gr_name.setMinimumSize(QtCore.QSize(0, 25))
        self.gr_name.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.gr_name.setFont(font)
        self.gr_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gr_name.setFrameShape(QtWidgets.QFrame.Box)
        self.gr_name.setLineWidth(1)
        self.gr_name.setMidLineWidth(0)
        self.gr_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gr_name.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.gr_name.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.gr_name.setAcceptRichText(True)
        self.gr_name.setObjectName("gr_name")
        self.gr_grid.addWidget(self.gr_name, 0, 0, 1, 1)
        self.gr_parent = QtWidgets.QTextEdit(self.gr_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gr_parent.sizePolicy().hasHeightForWidth())
        self.gr_parent.setSizePolicy(sizePolicy)
        self.gr_parent.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.gr_parent.setFont(font)
        self.gr_parent.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gr_parent.setFrameShape(QtWidgets.QFrame.Box)
        self.gr_parent.setLineWidth(1)
        self.gr_parent.setMidLineWidth(0)
        self.gr_parent.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gr_parent.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.gr_parent.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.gr_parent.setAcceptRichText(True)
        self.gr_parent.setObjectName("gr_parent")
        self.gr_grid.addWidget(self.gr_parent, 0, 1, 1, 1)
        self.gr_note = QtWidgets.QTextEdit(self.gr_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gr_note.sizePolicy().hasHeightForWidth())
        self.gr_note.setSizePolicy(sizePolicy)
        self.gr_note.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.gr_note.setFont(font)
        self.gr_note.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gr_note.setFrameShape(QtWidgets.QFrame.Box)
        self.gr_note.setLineWidth(1)
        self.gr_note.setMidLineWidth(0)
        self.gr_note.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gr_note.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.gr_note.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.gr_note.setAcceptRichText(True)
        self.gr_note.setObjectName("gr_note")
        self.gr_grid.addWidget(self.gr_note, 1, 0, 1, 1)
        self.gr_ico = QtWidgets.QTextEdit(self.gr_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gr_ico.sizePolicy().hasHeightForWidth())
        self.gr_ico.setSizePolicy(sizePolicy)
        self.gr_ico.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.gr_ico.setFont(font)
        self.gr_ico.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gr_ico.setFrameShape(QtWidgets.QFrame.Box)
        self.gr_ico.setLineWidth(1)
        self.gr_ico.setMidLineWidth(0)
        self.gr_ico.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gr_ico.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.gr_ico.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.gr_ico.setAcceptRichText(True)
        self.gr_ico.setObjectName("gr_ico")
        self.gr_grid.addWidget(self.gr_ico, 1, 1, 1, 1)
        self.gr_add = QtWidgets.QPushButton(self.gr_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gr_add.sizePolicy().hasHeightForWidth())
        self.gr_add.setSizePolicy(sizePolicy)
        self.gr_add.setMinimumSize(QtCore.QSize(75, 25))
        self.gr_add.setObjectName("gr_add")
        self.gr_grid.addWidget(self.gr_add, 3, 0, 1, 1)
        self.gr_remove = QtWidgets.QPushButton(self.gr_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gr_remove.sizePolicy().hasHeightForWidth())
        self.gr_remove.setSizePolicy(sizePolicy)
        self.gr_remove.setMinimumSize(QtCore.QSize(75, 25))
        self.gr_remove.setObjectName("gr_remove")
        self.gr_grid.addWidget(self.gr_remove, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.gr_util, 2, 0, 1, 1)
        self.db_util = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.db_util.sizePolicy().hasHeightForWidth())
        self.db_util.setSizePolicy(sizePolicy)
        self.db_util.setAlignment(QtCore.Qt.AlignCenter)
        self.db_util.setObjectName("db_util")
        self.db_grid = QtWidgets.QGridLayout(self.db_util)
        self.db_grid.setObjectName("db_grid")
        self.db_print = QtWidgets.QPushButton(self.db_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.db_print.sizePolicy().hasHeightForWidth())
        self.db_print.setSizePolicy(sizePolicy)
        self.db_print.setMinimumSize(QtCore.QSize(75, 25))
        self.db_print.setObjectName("db_print")
        self.db_grid.addWidget(self.db_print, 0, 0, 1, 1)
        self.db_remove = QtWidgets.QPushButton(self.db_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.db_remove.sizePolicy().hasHeightForWidth())
        self.db_remove.setSizePolicy(sizePolicy)
        self.db_remove.setMinimumSize(QtCore.QSize(75, 25))
        self.db_remove.setObjectName("db_remove")
        self.db_grid.addWidget(self.db_remove, 3, 1, 1, 1)
        self.db_create = QtWidgets.QPushButton(self.db_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.db_create.sizePolicy().hasHeightForWidth())
        self.db_create.setSizePolicy(sizePolicy)
        self.db_create.setMinimumSize(QtCore.QSize(75, 25))
        self.db_create.setObjectName("db_create")
        self.db_grid.addWidget(self.db_create, 3, 0, 1, 1)
        self.mode = QtWidgets.QComboBox(self.db_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mode.sizePolicy().hasHeightForWidth())
        self.mode.setSizePolicy(sizePolicy)
        self.mode.setMinimumSize(QtCore.QSize(75, 25))
        self.mode.setFrame(True)
        self.mode.setObjectName("mode")
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.addItem("")
        self.db_grid.addWidget(self.mode, 3, 2, 1, 1)
        self.db_choice = QtWidgets.QTextEdit(self.db_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.db_choice.sizePolicy().hasHeightForWidth())
        self.db_choice.setSizePolicy(sizePolicy)
        self.db_choice.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.db_choice.setFont(font)
        self.db_choice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.db_choice.setFrameShape(QtWidgets.QFrame.Box)
        self.db_choice.setLineWidth(1)
        self.db_choice.setMidLineWidth(0)
        self.db_choice.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.db_choice.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.db_choice.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.db_choice.setAcceptRichText(True)
        self.db_choice.setObjectName("db_choice")
        self.db_grid.addWidget(self.db_choice, 0, 1, 1, 2)
        self.db_auto = QtWidgets.QPushButton(self.db_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.db_auto.sizePolicy().hasHeightForWidth())
        self.db_auto.setSizePolicy(sizePolicy)
        self.db_auto.setMinimumSize(QtCore.QSize(75, 25))
        self.db_auto.setObjectName("db_auto")
        self.db_grid.addWidget(self.db_auto, 1, 0, 1, 1)
        self.status = QtWidgets.QLabel(self.db_util)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setMinimumSize(QtCore.QSize(0, 25))
        self.status.setFrameShape(QtWidgets.QFrame.Box)
        self.status.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.status.setText("")
        self.status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.status.setObjectName("status")
        self.db_grid.addWidget(self.status, 1, 1, 1, 2)
        self.gridLayout.addWidget(self.db_util, 1, 0, 1, 1)
        self.messages = QtWidgets.QTextEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messages.sizePolicy().hasHeightForWidth())
        self.messages.setSizePolicy(sizePolicy)
        self.messages.setMinimumSize(QtCore.QSize(0, 25))
        self.messages.setMaximumSize(QtCore.QSize(16777215, 100))
        self.messages.setFrameShape(QtWidgets.QFrame.Box)
        self.messages.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messages.setReadOnly(True)
        self.messages.setObjectName("messages")
        self.gridLayout.addWidget(self.messages, 3, 0, 1, 1)
        self.main = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setAlignment(QtCore.Qt.AlignCenter)
        self.main.setObjectName("main")
        self.main_grid = QtWidgets.QGridLayout(self.main)
        self.main_grid.setObjectName("main_grid")
        self.db_connect = QtWidgets.QPushButton(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.db_connect.sizePolicy().hasHeightForWidth())
        self.db_connect.setSizePolicy(sizePolicy)
        self.db_connect.setMinimumSize(QtCore.QSize(75, 25))
        self.db_connect.setObjectName("db_connect")
        self.main_grid.addWidget(self.db_connect, 3, 1, 1, 1)
        self.db_clear = QtWidgets.QPushButton(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.db_clear.sizePolicy().hasHeightForWidth())
        self.db_clear.setSizePolicy(sizePolicy)
        self.db_clear.setMinimumSize(QtCore.QSize(75, 25))
        self.db_clear.setObjectName("db_clear")
        self.main_grid.addWidget(self.db_clear, 3, 2, 1, 1)
        self.main_dir = QtWidgets.QTextEdit(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.main_dir.sizePolicy().hasHeightForWidth())
        self.main_dir.setSizePolicy(sizePolicy)
        self.main_dir.setMinimumSize(QtCore.QSize(75, 25))
        self.main_dir.setStyleSheet("")
        self.main_dir.setFrameShape(QtWidgets.QFrame.Box)
        self.main_dir.setLineWidth(1)
        self.main_dir.setMidLineWidth(0)
        self.main_dir.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.main_dir.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.main_dir.setReadOnly(False)
        self.main_dir.setObjectName("main_dir")
        self.main_grid.addWidget(self.main_dir, 3, 0, 1, 1)
        self.main_db = QtWidgets.QTextEdit(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.main_db.sizePolicy().hasHeightForWidth())
        self.main_db.setSizePolicy(sizePolicy)
        self.main_db.setMinimumSize(QtCore.QSize(75, 25))
        self.main_db.setAcceptDrops(True)
        self.main_db.setAutoFillBackground(False)
        self.main_db.setStyleSheet("")
        self.main_db.setFrameShape(QtWidgets.QFrame.Box)
        self.main_db.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.main_db.setMidLineWidth(0)
        self.main_db.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.main_db.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.main_db.setReadOnly(False)
        self.main_db.setObjectName("main_db")
        self.main_grid.addWidget(self.main_db, 0, 0, 1, 1)
        self.main_pass = QtWidgets.QLineEdit(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_pass.sizePolicy().hasHeightForWidth())
        self.main_pass.setSizePolicy(sizePolicy)
        self.main_pass.setMinimumSize(QtCore.QSize(75, 25))
        self.main_pass.setFrame(True)
        self.main_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.main_pass.setCursorPosition(0)
        self.main_pass.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_pass.setDragEnabled(True)
        self.main_pass.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.main_pass.setClearButtonEnabled(True)
        self.main_pass.setObjectName("main_pass")
        self.main_grid.addWidget(self.main_pass, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.main, 0, 0, 1, 1)
        window.setCentralWidget(self.widget)
        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)
    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "MainWindow"))
        self.gr_util.setTitle(_translate("window", "Group Utility"))
        self.gr_name.setPlaceholderText(_translate("window", "input group name"))
        self.gr_parent.setPlaceholderText(_translate("window", "input parent"))
        self.gr_note.setPlaceholderText(_translate("window", "input notes"))
        self.gr_ico.setPlaceholderText(_translate("window", "input icon"))
        self.gr_add.setText(_translate("window", "Add"))
        self.gr_remove.setText(_translate("window", "Remove"))
        self.db_util.setTitle(_translate("window", "Database Utilities"))
        self.db_print.setText(_translate("window", "Print"))
        self.db_remove.setText(_translate("window", "Remove Copy"))
        self.db_create.setText(_translate("window", "Create Copy"))
        self.mode.setItemText(0, _translate("window", "Database"))
        self.mode.setItemText(1, _translate("window", "Group (Subitem)"))
        self.mode.setItemText(2, _translate("window", "Group"))
        self.mode.setItemText(3, _translate("window", "Entry"))
        self.db_choice.setPlaceholderText(_translate("window", "input item(s) to print"))
        self.db_auto.setText(_translate("window", "Auto Copy"))
        self.messages.setHtml(_translate("window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "\
        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "\
"text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">INFORMATION</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; "\
"-qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"\
"<span style=\" font-weight:600;\">Main </span>- used to input database, folder and password. droping items is also acceptable. "\
"database and password are required to work with their utilities. folder is required to work with groups. connect is useful "\
"for printing multiple items or generally working with one database only. clear removes connection or clears all fields.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"\
"<span style=\" font-weight:600;\">Database Utilities</span> - tools for databases. copy tools are creating/removing database "\
"copy with other password. new databases are located in /documents/multipass/user databases. to use autosync firstly sync "\
"manually even once. to sync manually use create. after turning on or off autosync, restart pc. To remove new database and "\
"stop sync only name is required. (Please do not remove manually). to print choose mode in combobox and input items (separated "\
"by &quot;, &quot; if there are multiple items). prints are located in are located in /documents/multipass/prints.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"\
"<span style=\" font-weight:600;\">Group Utility</span> - adds or removes group in all databases. name is only required fields, "\
"others are additionls. if parent is not inputed group will be added to the root group.</p></body></html>"))
        self.main.setTitle(_translate("window", "Main"))
        self.db_connect.setText(_translate("window", "Connect"))
        self.db_clear.setText(_translate("window", "Clear"))
        self.main_dir.setPlaceholderText(_translate("window", "Folder"))
        self.main_db.setPlaceholderText(_translate("window", "Database"))
        self.main_pass.setPlaceholderText(_translate("window", "Input password"))
class multipass(QtWidgets.QMainWindow):
    def __init__(self):
        super(multipass, self).__init__()
        self.conn_db = None
        self.database = None
        self.folder = None
        self.ui = Ui_window()
        self.ui.setupUi(self)
        self.ui.db_util.setEnabled(False)
        self.ui.gr_util.setEnabled(False)
        self.status()
        self.click()
    def click(self):
        self.ui.main_db.mousePressEvent = self.find_db
        self.ui.main_db.dropEvent = self.overwrite_db
        self.ui.main_dir.mousePressEvent = self.find_dir
        self.ui.main_dir.dropEvent = self.overwrite_dir
        self.ui.db_connect.clicked.connect(self.db_connector)
        self.ui.db_clear.clicked.connect(self.db_clearer)
        self.ui.db_create.clicked.connect(self.db_copier)
        self.ui.db_remove.clicked.connect(self.db_remover)
        self.ui.db_auto.clicked.connect(self.startup)
        self.ui.db_print.clicked.connect(self.print)
        self.ui.gr_add.clicked.connect(self.group_add)
        self.ui.gr_remove.clicked.connect(self.group_remove)
    def clear(self):
        if self.conn_db == None:
            self.ui.main_db.setEnabled(True)
            self.ui.main_dir.setEnabled(True)
            self.ui.db_util.setEnabled(False)
            self.ui.gr_util.setEnabled(False)
            self.ui.main_pass.clear()
            self.ui.main_db.setPlainText("")
            self.ui.main_dir.setPlainText("")
            self.ui.gr_name.setPlainText("")
            self.ui.gr_parent.setPlainText("")
            self.ui.gr_ico.setPlainText("")
            self.ui.gr_note.setPlainText("")
            self.ui.db_choice.setPlainText("")
            self.ui.messages.setPlainText("")
            self.database = None
            self.folder = None
        else:
            self.ui.main_db.setEnabled(False)
            self.ui.main_dir.setEnabled(False)
            self.ui.main_pass.setEnabled(False)
            self.ui.db_util.setEnabled(True)
            self.ui.gr_util.setEnabled(False)
            self.ui.main_pass.clear()
            self.ui.main_db.setPlainText("")
            self.ui.main_dir.setPlainText("")
            self.ui.gr_name.setPlainText("")
            self.ui.gr_parent.setPlainText("")
            self.ui.gr_ico.setPlainText("")
            self.ui.gr_note.setPlainText("")
            self.ui.db_choice.setPlainText("")
            self.ui.messages.setPlainText("")
            self.database = None
            self.folder = None
    def db_connector(self):
        db = self.database
        db_pass = self.ui.main_pass.text()
        if db == None or db_pass == "":
            self.ui.messages.setText("Database and password are required")
            return
        else:
            try: open_db = PyKeePass(db, password=db_pass)
            except: 
                self.ui.messages.setText(f"Password is inorrect") 
                return
            self.conn_db = open_db
            self.clear()
            self.ui.db_util.setEnabled(True)
            self.ui.gr_util.setEnabled(False)
            self.ui.main_db.setEnabled(False)
            self.ui.main_dir.setEnabled(False)
            self.ui.main_pass.setEnabled(False)
            self.ui.messages.setText(f"Database {self.conn_db.root_group.name} is connected")
    def db_clearer(self):
        if self.conn_db != None:
            self.clear()
            self.ui.messages.setText(f"Database {self.conn_db.root_group.name} is disconnected")
            self.conn_db = None
            self.ui.main_db.setEnabled(True)
            self.ui.main_dir.setEnabled(True)
            self.ui.main_pass.setEnabled(True)
        else:
            self.clear()
            self.ui.messages.setText("There is no connection to clear")
        self.ui.main_db.setEnabled(True)
        self.ui.main_dir.setEnabled(True)
        self.ui.db_util.setEnabled(False)
        self.ui.gr_util.setEnabled(False)
    def db_open(self):
        if self.conn_db != None: db = self.conn_db
        else:
            db_pass = self.ui.main_pass.text()
            if self.database == None or db_pass == "":
                self.ui.messages.setText("Database and password are required")
                return None
            else:
                try: db = PyKeePass(self.database, db_pass)
                except:
                    self.ui.messages.setText(f"Password is inorrect") 
                    return None
        return db
    def find_db(self, event):
        self.clear()
        if event.button() == 1:
            options = QtWidgets.QFileDialog.Options()
            file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose a File", 
            QtCore.QDir.homePath(), "KDBX Files (*.kdbx);;All Files (*)", options=options)
            if file_name:
                self.ui.messages.setText(f"File {file_name} is chosen")
                self.ui.main_db.setText(f"{file_name}")
                self.database = file_name
                self.ui.main_db.clearFocus()
                self.ui.db_util.setEnabled(True)
                self.ui.main_dir.setEnabled(False)
            else:
                self.ui.messages.setText("File was not chosen")
                self.ui.main_db.clearFocus()
                return
    def find_dir(self, event):
        self.clear()
        if event.button() == 1:
            options = QtWidgets.QFileDialog.Options()
            self.folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose a Folder", 
            QtCore.QDir.homePath(), options=options)
            if self.folder:
                self.ui.messages.setText(f"Folder {self.folder} is chosen")
                self.ui.main_dir.setText(f"{self.folder}")
                self.ui.main_dir.clearFocus()
                self.ui.gr_util.setEnabled(True)
                self.ui.main_db.setEnabled(False)
            else:
                self.ui.messages.setText("Folder was not chosen")
                self.ui.main_dir.clearFocus()
                return
    def overwrite_db(self, event):
        self.clear()
        if event.mimeData().hasUrls() and all(url.toLocalFile().lower().endswith(".kdbx") for url in event.mimeData().urls()):
            self.database = event.mimeData().urls()[0].toLocalFile()
            self.ui.messages.setText(f"Database {self.database} is chosen")
            self.ui.main_db.setPlainText(f"{self.database}")
            self.ui.db_util.setEnabled(True)
            self.ui.main_dir.setEnabled(False)
        else:
            self.ui.messages.setText("Only .kdbx files are allowed to be dropped.")
        self.ui.main_db.clearFocus()
    def overwrite_dir(self, event):
        self.clear()
        if event.mimeData().hasUrls():
            self.folder = event.mimeData().urls()[0].toLocalFile()
            self.ui.messages.setText(f"Folder {self.folder} is chosen")
            self.ui.main_dir.setPlainText(f"{self.folder}")
            self.ui.gr_util.setEnabled(True)
            self.ui.main_db.setEnabled(False)
        self.ui.main_dir.clearFocus()
    def status(self):
        if check(): self.ui.status.setText("Auto: on")
        else: self.ui.status.setText("Auto: off")
    def startup(self):
        json_path = os.path.join(os.getenv('LOCALAPPDATA'), "Multipass", "db_info.json")
        if not os.path.exists(json_path):
            self.ui.messages.setText("Please sync manually at least once")
            return
        m_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        for root, dirs, files in os.walk(m_dir):
            if "auto.exe" in files:
                script_path = os.path.abspath(os.path.join(root, "auto.exe"))
        startup_key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        if check():
            try:
                run_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, startup_key_path, 0, winreg.KEY_SET_VALUE)
                winreg.DeleteValue(run_key, "auto.exe")
                winreg.CloseKey(run_key)
                self.ui.status.setText("Auto: off")
                self.ui.messages.setText("Script removed from startup, please restart pc")
                return
            except Exception as e:
                self.ui.messages.setText("Error removing script from startup:\n" + str(e))
                return
        else:
            try:
                run_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, startup_key_path, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(run_key, "auto.exe", 0, winreg.REG_SZ, f'"{script_path}"')
                winreg.CloseKey(run_key)
                self.ui.status.setText("Auto: on")
                self.ui.messages.setText("Script added to startup, please restart pc")
                return
            except Exception as e:
                self.ui.messages.setText("Error adding script to startup:\n" + str(e))
                return
    def group_add(self):
        if self.folder == None:
            self.ui.messages.setText("Chosing folder is required")
            return
        files = os.listdir(self.folder)
        if not any(file.lower().endswith(".kdbx") for file in files):
            self.ui.messages.setText("Folder does not contains .kdbx files")
            return
        db_pass = self.ui.main_pass.text()
        name = self.ui.gr_name.toPlainText()
        parent = self.ui.gr_parent.toPlainText()
        icon = self.ui.gr_ico.toPlainText()
        note = self.ui.gr_note.toPlainText()
        if db_pass == "" or name == "":
            self.ui.messages.setText("Name and password are required")
            return
        else:
            if icon == "": icon = "48"
            if parent == "": parent = None
            for file in files:
                path = os.path.join(self.folder, file)
                if path.endswith(".kdbx"):
                    try: db = PyKeePass(filename=path, password=db_pass)
                    except:
                        self.ui.messages.setText("Password is incorrect")
                        return
                    par = db.find_groups(name=parent, first=True)
                    if par == None: par = db.root_group
                    db.add_group(par, name, icon, note)
                    db.save()            
            self.clear()
            self.ui.messages.setText(f"Group with name '{name}' was created in all databases")
    def group_remove(self):
        if self.folder == None:
            self.ui.messages.setText("Chosing folder is required")
            return
        files = os.listdir(self.folder)
        if not any(file.lower().endswith(".kdbx") for file in files):
            self.ui.messages.setText("Folder does not contains .kdbx files")
            return
        db_pass = self.ui.main_pass.text()
        gr_name = self.ui.gr_name.toPlainText()
        counter = 0
        if db_pass == "" or gr_name== "":
            self.ui.messages.setText("Name and password are required")
            return
        else:
            for file in files:
                path = os.path.join(self.folder, file)
                if path.endswith(".kdbx"):
                    try: db = PyKeePass(filename=path, password=db_pass)
                    except:
                        self.ui.messages.setText("Password is incorrect")
                        return
                    r_group = db.find_groups(name=gr_name, first=True)
                    if r_group == None: continue
                    else:
                        db.delete_group(r_group)
                        db.save()
                        counter += 1
            if counter == 0:
                self.ui.messages.setText("Group with such name doesn't exists")
                return
            self.clear()
            self.ui.messages.setText(f"Group with name '{gr_name}' was deleted from all databases")
    def db_copier(self):
        db = self.db_open() 
        if db == None: return
        result = pathes(db)
        if not os.path.exists(result[3]):
            shutil.copy2(result[4], result[2])
            n_db = PyKeePass(filename=result[5], password=db.password)
            n_db_pass = rand_pass()
            n_db.password = n_db_pass
            n_db.save()
            os.rename(result[5], result[3])
            pass_file = os.path.join(result[2], (result[7] + "_user_password.txt"))
            update_passwords(result[6], result[7], result[4], result[3], db.password, n_db_pass)
            with open(pass_file, 'w', encoding='utf-8') as f: f.write(f"User database password: {n_db_pass}")
            self.clear()
            self.ui.messages.setText("Database copy created")
        else:
            info = read_passwords(result[7], result[6])
            os.remove(info[2])
            shutil.copy2(info[1], result[2])
            n_db = PyKeePass(filename=result[5], password=info[3])
            n_db.password = info[4]
            n_db.save()
            os.rename(result[5], info[2])
            self.clear()
            self.ui.messages.setText("Database copy updated")
    def db_remover(self):
        db_name = self.database
        if db_name == None: 
            self.ui.messages.setText("Input database")
            return
        if "_user.kdbx" not in db_name:
            self.ui.messages.setText("Use this function to remove copies only")
            return
        db_json =  os.path.basename(db_name).replace("_user.kdbx", "")
        dir = os.path.dirname(db_name)
        remove_passwords(db_json)
        shutil.rmtree(dir)
        self.clear()
        self.ui.messages.setText("Database copy deleted")
    def print(self):
        db = self.db_open() 
        if db == None: return
        mode = self.ui.mode.currentText()
        item_name = self.ui.db_choice.toPlainText()
        check = print_helper(db, mode, item_name)
        if check == "0":
            self.clear()
            self.ui.messages.setText("Printed successfully")
        elif check == "1":
            self.ui.messages.setText("Item(s) are invalid")
        elif check == "2":
            self.ui.messages.setText("PDF with such name exists. to overwrite it please close it")
def check():
    m_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    for root, dirs, files in os.walk(m_dir):
        if "auto.exe" in files:
            script_path = os.path.abspath(os.path.join(root, "auto.exe"))
    startup_key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        run_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, startup_key_path, 0, winreg.KEY_READ)
        try:
            script_value, _ = winreg.QueryValueEx(run_key, "auto.exe")
            winreg.CloseKey(run_key)
            if script_value == f'"{script_path}"': return True
        except FileNotFoundError: pass
        winreg.CloseKey(run_key)
    except FileNotFoundError: pass
    return False
def update_passwords(filename, db_name, o_name, n_name, old_pass, new_pass):
    db_dict = {db_name: [o_name, n_name, old_pass, new_pass]}
    config = os.path.join(os.getenv('LOCALAPPDATA'), 'Multipass', 'config.ini')
    if os.path.exists(config): key = read_config()
    else:
        key = Fernet.generate_key()
        create_config(key)
    if os.path.exists(filename): data = decrypt(filename, key)
    else: data = {}
    data.update(db_dict)
    encrypt(data, filename, key)
def read_passwords(db_name, file):
    key = read_config()
    data = decrypt(file, key)
    db_info = data.get(db_name)
    result = [db_name]
    result.extend(db_info)
    return result
def remove_passwords(db_name):
    key = read_config()
    file = os.path.join(os.getenv('LOCALAPPDATA'), "Multipass", "db_info.json")
    data = decrypt(file, key)
    if db_name in data.keys():
        data.pop(db_name)
        encrypt(data, file, key)
def create_config(key):
    config = configparser.ConfigParser()
    key_str = base64.urlsafe_b64encode(key).rstrip(b'=').decode()
    config['security'] = {'key': key_str}
    file = os.path.join(os.getenv('LOCALAPPDATA'), 'Multipass', 'config.ini')
    with open(file, 'w') as ff:
        config.write(ff)
def read_config():
    file = os.path.join(os.getenv('LOCALAPPDATA'), 'Multipass', 'config.ini')
    config = configparser.ConfigParser()
    config.read(file)
    if 'security' in config and 'key' in config['security']:
        key_str = config['security']['key'].encode()
        key_bytes = base64.b64decode(key_str + b'=' * (4 - len(key_str) % 4))
        return key_bytes
def encrypt(json_data, file, key):
    json_string = json.dumps(json_data)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(json_string.encode())
    with open(file, 'wb') as file:
        file.write(encrypted)
def decrypt(file, key):
    with open(file, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    json_data = json.loads(decrypted.decode())
    return json_data
def rand_pass():
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)
    part1 = round(16 * (30/100))
    part2 = round(16 * (20/100))
    result = []
    for x in range(part1):
        result.append(s1[x])
        result.append(s2[x])
    for x in range(part2):
        result.append(s3[x])
        result.append(s4[x])
    random.shuffle(result)
    password = "".join(result)
    return password
def pathes(db):
    filename = db.root_group.name
    of_file = db.filename
    file_dir = os.path.dirname(of_file)
    nf_path = os.path.join(os.path.expanduser("~"), "Documents", "Multipass", "User databases")
    if not os.path.exists(nf_path): os.makedirs(nf_path, exist_ok=True)
    nfu_path = os.path.join(nf_path, f"{filename}")
    if not os.path.exists(nfu_path): os.makedirs(nfu_path)
    local_appdata_dir = os.path.join(os.getenv('LOCALAPPDATA'), "Multipass")
    if not os.path.exists(local_appdata_dir): os.makedirs(local_appdata_dir)
    old_name = os.path.join(nfu_path, filename + ".kdbx")
    new_name = os.path.join(nfu_path, filename + "_user.kdbx")
    json_file = os.path.join(local_appdata_dir, "db_info.json")
    return file_dir, nf_path, nfu_path, new_name, of_file, old_name, json_file, filename
def print_helper(db, mode, item):
    def print_notes(note, ind):
        if note is None: return "None"
        ind += "          "
        max = 30
        f_string = ""
        length = 0
        for char in note:
            if length == max:
                if char != " ":
                    f_string += f'-\n{ind}-'
                    length = 1
                else:
                    f_string += f'\n{ind}'
                    length = 0
            f_string += char
            length += 1
        return f_string
    def print_entry(stream, entry, last, mode, indent_level=0):
        if mode:
            indent = "    (E)"
            ind_en = "       "
        elif last: 
            indent = "     " + ("│    " * indent_level) + "└───(E)"
            ind_en = "     " + ("│    " * indent_level) + "       "
        else: 
            indent = "     " + ("│    " * indent_level) + "├───(E)"
            ind_en = "     " + ("│    " * indent_level) + "│      "
        entry_str = (f"{indent}┬─Title - {entry.title};\n{ind_en}│ User Name - {entry.username};\n"
        f"{ind_en}│ Password - {entry.password};\n{ind_en}│ URL - {entry.url};"
        f"\n{ind_en}└─Notes - \"{print_notes(entry.notes, ind_en)}\";\n")
        stream.write(entry_str)
    def print_group(stream, group, first, gr_only, indent_level=-1):
        indent = "     " + ("│    " * indent_level) + "├───(G)"
        if group.is_root_group: stream.write(f"    (B) {group.name}:\n")
        elif first: stream.write(f"    (G) {group.name}:\n")
        else: stream.write(f"{indent}{group.name}:\n")
        if not gr_only:
            for subgroup in group.subgroups:
                print_group(stream, subgroup, False, False, indent_level + 1)
        else:
            for subgroup in group.subgroups:
                stream.write(f"{indent}{subgroup.name}\n")
        ent_cnt = len(group.entries)
        for i, entry in enumerate(group.entries):
            is_last = i == ent_cnt - 1
            print_entry(stream, entry, is_last, False, indent_level + 1)
    item_arr = item.split(", ")
    if mode == "Group" or mode == "Group (Subitem)":
        for i in item_arr:
            if db.find_groups(name=i, first=True) == None: return "1"
    elif mode == "Entry":
        for i in item_arr:
            if db.find_entries(title=i, first=True) == None: return "1"
    db_name = db.root_group.name
    nf_path = os.path.join(os.path.expanduser("~"), "Documents",
    "Multipass", "Prints", db_name, mode)
    if not os.path.exists(nf_path): os.makedirs(nf_path, exist_ok=True)
    name = item.replace(", ", "_")
    if mode == "Database": 
        txt_file = os.path.join(nf_path, f"{db_name}.txt")
        pdf_file = os.path.join(nf_path, f"{db_name}.pdf")
    else: 
        txt_file = os.path.join(nf_path, f"{name}.txt")
        pdf_file = os.path.join(nf_path, f"{name}.pdf")
    with open(txt_file, 'w', encoding='utf-8') as stream:
        if mode == "Database":
            stream.write(f"Database {db_name} Diagram:\n")
            print_group(stream, db.root_group, False, False)
            stream.write("(Notes: (B) - Database Name; (G) - Group; (E) - Entry;)")
        elif mode == "Group (Subitem)":
            for i in item_arr:
                stream.write(f"Group {i} Diagram (with subitems):\n")
                print_group(stream, db.find_groups(name=i, first=True), True, False)
            stream.write("(Notes: (G) - Group; (E) - Entry;)")
        elif mode == "Group":
            for i in item_arr:
                stream.write(f"Group {i} Diagram:\n")
                print_group(stream, db.find_groups(name=i, first=True), True, True)
            stream.write("(Notes: (G) - Group; (E) - Entry;)")
        elif mode == "Entry":
            for i in item_arr:
                stream.write(f"Entry {i}:\n")
                print_entry(stream, db.find_entries(title=i, first=True), False, True)
                stream.write("\n\n")
    to_pdf = txt_to_pdf(txt_file, pdf_file)
    os.remove(txt_file)
    if to_pdf == "1": return "2"
    return "0"
def txt_to_pdf(txt, pdf_p):
    if os.path.exists(pdf_p):
        try: os.remove(pdf_p)
        except: return "1"
    pdf = FPDF()
    pdf.add_font('Consolas', '', 'C:/Windows/Fonts/consola.ttf', uni=True)
    pdf.set_font("Consolas", size=10)
    pdf.add_page()
    with open(txt, "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        pdf.multi_cell(0, 4.1, line, 0, "L")
    pdf.output(pdf_p, "F")
app = QtWidgets.QApplication([])
application = multipass()
application.show()
sys.exit(app.exec())