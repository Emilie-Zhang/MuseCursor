# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MuseLauncher.ui'
#
# Created: Sun Aug 16 12:17:24 2015
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_launcher_dialog(object):
    def setupUi(self, launcher_dialog):
        launcher_dialog.setObjectName(_fromUtf8("launcher_dialog"))
        launcher_dialog.resize(371, 160)
        launcher_dialog.setMinimumSize(QtCore.QSize(371, 160))
        launcher_dialog.setMaximumSize(QtCore.QSize(371, 160))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Cursor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        launcher_dialog.setWindowIcon(icon)
        self.muse_and_maze_push_button = QtGui.QPushButton(launcher_dialog)
        self.muse_and_maze_push_button.setGeometry(QtCore.QRect(190, 10, 171, 141))
        self.muse_and_maze_push_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.muse_and_maze_push_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Maze.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.muse_and_maze_push_button.setIcon(icon1)
        self.muse_and_maze_push_button.setIconSize(QtCore.QSize(100, 100))
        self.muse_and_maze_push_button.setObjectName(_fromUtf8("muse_and_maze_push_button"))
        self.muse_push_button = QtGui.QPushButton(launcher_dialog)
        self.muse_push_button.setGeometry(QtCore.QRect(10, 10, 171, 141))
        self.muse_push_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.muse_push_button.setText(_fromUtf8(""))
        self.muse_push_button.setIcon(icon)
        self.muse_push_button.setIconSize(QtCore.QSize(100, 100))
        self.muse_push_button.setObjectName(_fromUtf8("muse_push_button"))

        self.retranslateUi(launcher_dialog)
        QtCore.QMetaObject.connectSlotsByName(launcher_dialog)

    def retranslateUi(self, launcher_dialog):
        launcher_dialog.setWindowTitle(_translate("launcher_dialog", "Muse Launcher", None))

import icons_rc
