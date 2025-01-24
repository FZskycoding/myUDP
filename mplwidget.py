# ------------------------------------------------- ----- 
# -------------------- mplwidget.py -------------------- 
# -------------------------------------------------- ---- 
from  PyQt5.QtWidgets  import * 
from  matplotlib.backends.backend_qt5agg  import  FigureCanvas 
from  matplotlib.figure  import  Figure 
    
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class  MplWidget (QWidget): 
    def  __init__ ( self,  parent=None): 
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure()) 
        
        vertical_layout =  QVBoxLayout () 
        self.toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas) 
        '''
        self.canvas.axes0 = self.canvas.figure.add_subplot(331)
        self.canvas.axes1 = self.canvas.figure.add_subplot(332)
        self.canvas.axes2 = self.canvas.figure.add_subplot(333)
        self.canvas.axes3 = self.canvas.figure.add_subplot(334)
        self.canvas.axes4 = self.canvas.figure.add_subplot(335)
        self.canvas.axes5 = self.canvas.figure.add_subplot(336)
        self.canvas.axes6 = self.canvas.figure.add_subplot(337)
        self.canvas.axes7 = self.canvas.figure.add_subplot(338)
        
        self.canvas.axes8 = self.canvas.figure.add_subplot(311)
        self.canvas.axes9 = self.canvas.figure.add_subplot(312)
        self.canvas.axes10 = self.canvas.figure.add_subplot(313) 
        '''
        self.canvas.figure.clf()
        self.canvas.figure.tight_layout() #隔開兩個圖
        self.setLayout(vertical_layout)