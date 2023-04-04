# type: ignore
import os
import shutil
import sys

from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove Title bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.clearBtn.clicked.connect(self.buttonClick)
        self.ui.logBtn.clicked.connect(self.buttonClick)
        self.ui.exitBtn.clicked.connect(self.buttonClick)

        self.show()

# /////////////////////////////////////////////////////////////////////////////
# Allows the application to be dragged around the screen
# /////////////////////////////////////////////////////////////////////////////

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(), event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(
                self.pos() + QPoint(event.scenePosition().x(),
                                    event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

# /////////////////////////////////////////////////////////////////////////////
# # Program Logic
# /////////////////////////////////////////////////////////////////////////////

    def flushDNS(self):
        try:
            os.system('ipconfig/flushdns')

        except Exception as e:
            exc_type = type(e)
            return QMessageBox.warning(self, f'ERRO: {exc_type.__name__}',
                                       f'Description: {e}.')
        finally:
            QMessageBox.information(self, 'Success.', 'DNS flushed.')
            sys.exit()

    def displayDNS(self):
        try:
            os.system('ipconfig /displaydns > Log.txt')

        except Exception as e:
            exc_type = type(e)
            return QMessageBox.warning(self, f'ERRO: {exc_type.__name__}',
                                       f'Description: {e}.')
        finally:
            QMessageBox.information(self, 'Success.', 'Log has been created.')
            # self.moveLog()
            sys.exit()

    def moveLog(self):
        try:
            user = os.environ['USERNAME']
            pcName = os.environ['COMPUTERNAME']
            sourcePath = r'C:\\Users\\{}\\Log.txt'.format(user)
            destPath = r'C:\\Users\\{}\\Desktop\\{}.txt'.format(user, pcName)
            shutil.move(sourcePath, destPath)

        except Exception as e:
            exc_type = type(e)
            return QMessageBox.warning(self, f'ERRO: {exc_type.__name__}',
                                       f'Description: {e}.')

# /////////////////////////////////////////////////////////////////////////////
# Execute something if any button was pressed.
# /////////////////////////////////////////////////////////////////////////////

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'clearBtn':
            self.flushDNS()

        if btnName == 'logBtn':
            self.displayDNS()

        if btnName == 'exitBtn':
            sys.exit()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec())
