from PyQt4 import uic, QtGui

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""

    def __init__ (self, parent = None):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.shortcuts = {} #dict with all the shortcuts

    def __del__ (self):
        self.ui = None

    def connect_slots(self):
        # 'Strc dolu' button adds lineEdit text to textBrowser 
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_slot)
        # pressing enter in lineEdit adds to textBrowser
        self.ui.lineEdit.returnPressed.connect(self.pushButton_2_slot)

        for shortcut in self.shortcuts.keys():
            self.shortcuts[shortcut].activated.connect(self.quit_on_esc)

    def create_shortcuts(self):
        self.shortcuts['esc'] = QtGui.QShortcut(self)
        self.shortcuts['esc'].setKey("Esc")

    def pushButton_2_slot(self):
        ''' Append text from lineEdit field if it is not empty '''
        print 'appending self.ui.lineEdit.text()'
        if self.ui.lineEdit != '':
            self.ui.textBrowser.setPlainText(
                self.ui.textBrowser.toPlainText()+self.ui.lineEdit.text()
            )
            self.ui.lineEdit.clear()

    def quit_on_esc(self):
        print 'closing on esc key press'
        self.close()

