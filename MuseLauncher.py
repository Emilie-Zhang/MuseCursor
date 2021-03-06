from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import MuseLauncher_ui
import MuseCursor
import MuseMaze

class MuseLauncher(QDialog, MuseLauncher_ui.Ui_launcher_dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.muse_push_button.clicked.connect(self.launch_cursor)
        self.muse_and_maze_push_button.clicked.connect(self.launch_maze)

        self.setFocus()

    def launch_cursor(self):
        self.close()
        MuseCursor.main()

    def launch_maze(self):
        self.close()
        MuseCursor.main()
        MuseMaze.main()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MuseLauncher_ = MuseLauncher()
    MuseLauncher_.show()
    app.exec_()