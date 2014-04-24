from PyQt4 import uic

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""

    def __init__ (self, parent = None):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.connect_slots()

    def __del__ (self):
        self.ui = None
        
    def connect_slots(self):
        self.ui.pushButton_2.clicked.connect(self.pushButton_slot)
        print self.ui.pushButton.clicked.connect
    
    def pushButton_slot(self):
        print "pushButton_slot called"