
import sys
import platform
import numpy as np

#import matplotlib
#matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import (QMainWindow, QApplication, QDialog, QLineEdit, 
                             QVBoxLayout, QAction, QMessageBox,QFileDialog,
                             QSizePolicy, QLabel, QListWidget, QComboBox)
from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap


from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure


import control 
from numpy.linalg import matrix_rank
import math
import scipy



"""""""""""""""""""""""""""  """""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
class Form(QMainWindow, QDialog) :

    def __init__(self, parent=None) :
        super(Form, self).__init__(parent)
       
#        self.men = MainWindow()
#       


        self.menuFile = self.menuBar().addMenu("&File")
        self.actionSaveAs = QAction("&Save As", self)
        self.actionSaveAs.triggered.connect(self.saveas)
        self.actionQuit = QAction("&Quit", self)
        self.actionQuit.triggered.connect(self.close)
        self.menuFile.addActions([self.actionSaveAs, self.actionQuit])
        
        # Create the Help menu
        self.menuHelp = self.menuBar().addMenu("&Help")
        self.actionAbout = QAction("&About",self)
        self.actionAbout.triggered.connect(self.about)
        self.menuHelp.addActions([self.actionAbout])
        """"""""""""""""""""""""""""""
        """"""""""""""""""""""""""""""
        """"""""""""""""""""""""""""""
        
        
        self.widget = QDialog()
        
         
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab1,"Controllability and Observability")         
        self.tabs.addTab(self.tab2,"Full state observer")                        
        
        
        
        """"""""""""""""""""""""""""""
        """"""""""""""""tab1"""""""""""""""
        
        pic1 = QLabel(self)
        picCT = QPixmap('ctob.PNG')
        pic1.setPixmap(picCT)
        
        self.ctrbA = QLineEdit("[[-3,-2],[1,0]]")
        self.ctrbB = QLineEdit("[[1],[0]]")
        self.ctrbC = QLineEdit("[1,1]")
        self.ctrbA.selectAll()
        self.ctrbB.selectAll()
        self.ctrbC.selectAll()
        self.outputC = QLineEdit("")
        self.outputC.selectAll()
        self.rankC = QLineEdit("rank of controllability matrix")
        self.rankC.selectAll()
        self.outputO = QLineEdit("")
        self.outputO.selectAll()
        self.rankO = QLineEdit("rank of controllability matrix")
        self.rankO.selectAll()
        self.labelA = QLabel("A matrix")
        self.labelB = QLabel("B matrix")
        self.labelC = QLabel("C matrix")
        self.labelCtrb = QLabel("Controllability of the system")
        self.labelObsv = QLabel("Observability of the system")
        self.labelIn = QLabel("Inputs")
        self.labelOut = QLabel("Result")
        
        self.push1 = QPushButton("Determine controllability and observability")
             
        
        self.tab1.layout = QGridLayout(self)
        
        """inputs"""
        self.tab1.layout.addWidget(pic1,0,3)       
        
        self.tab1.layout.addWidget(self.labelIn,5,0)  
        self.tab1.layout.addWidget(self.labelOut,5,2) 
        self.tab1.layout.addWidget(self.labelA,6,0) 
        self.tab1.layout.addWidget(self.ctrbA,6,1)  

        self.tab1.layout.addWidget(self.labelB,7,0)        
        self.tab1.layout.addWidget(self.ctrbB,7,1) 
        
        self.tab1.layout.addWidget(self.labelC,8,0)        
        self.tab1.layout.addWidget(self.ctrbC,8,1)
        
        """outputs"""
        self.tab1.layout.addWidget(self.labelCtrb,6,2) 
        self.tab1.layout.addWidget(self.outputC,6,3)
        
        self.tab1.layout.addWidget(self.labelObsv,7,2) 
        self.tab1.layout.addWidget(self.outputO,7,3)
        
        self.tab1.setLayout(self.tab1.layout)
                
        
        layout = QVBoxLayout() 
#        layout.addWidget(self.tabs)
                
        self.tab1.layout.addWidget(self.push1)
        
        """"""""""""""""""""""""""""""
        """"""""""""""""""""""""""""""
        
        
        """"""""""""""""""""""""""""""
        """"""""""""""""tab2"""""""""""""""
        
        pic2 = QLabel(self)
        picFSO = QPixmap('fullstate.PNG')
        pic2.setPixmap(picFSO)
        
        self.dF = QLineEdit("[[-1,-2,-2],[0,-1,1],[1,0,-1]]")
        self.dG = QLineEdit("[[2],[0],[1]]")
        self.dH = QLineEdit("[1,0,0]")
        self.dJ = QLineEdit("[0]")
        self.dos = QLineEdit("5")
        self.dts = QLineEdit("4")
        self.dintegral = QLineEdit("5")
        self.dPO = QLineEdit("[ -10, -11, -12 ]")
        
        self.dF.selectAll()
        self.dG.selectAll()
        self.dH.selectAll()
        self.dJ.selectAll()
        self.dos.selectAll()
        self.dts.selectAll()
        self.dintegral.selectAll()
        self.dPO.selectAll()
        
        self.dAm = QTextEdit("")
        self.dAm.selectAll()
        self.dBm = QLineEdit("")
        self.dBm.selectAll()
        self.dCm = QLineEdit("")
        self.dCm.selectAll()
        self.dDm = QLineEdit("")
        self.dDm.selectAll()
        
        self.labeldF = QLabel("F matrix\n(3X3)")
        self.labeldG = QLabel("G matrix\n(3X1)")
        self.labeldH = QLabel("H matrix\n(1X3)")
        self.labeldJ = QLabel("J matrix\n(1X1)")
        self.labeldos = QLabel("% overshoot")
        self.labeldts = QLabel("Settling time")
        self.labeldintegral = QLabel("Integral pole \n(in negetive sign)")
        self.labeldPO = QLabel("Obsersver poles \n (array)")
        
        self.labeldAm = QLabel("Am matrix\n(7X7)\n")
        self.labeldBm = QLabel("Bm matrix")
        self.labeldCm = QLabel("Cm matrix")
        self.labeldDm = QLabel("Dm matrix")
        
        
        self.labelIn2 = QLabel("Inputs")
        self.labelOut2 = QLabel("Result")
        
        self.push2 = QPushButton("Find desinged system")
             
        
        self.tab2.layout = QGridLayout(self)
        
        
        
        
        """inputs"""
        self.tab2.layout.addWidget(pic2,0,3)       
        
        self.tab2.layout.addWidget(self.labelIn2,5,0)  
        self.tab2.layout.addWidget(self.labelOut2,5,2)
        
        self.tab2.layout.addWidget(self.labeldF,6,0) 
        self.tab2.layout.addWidget(self.dF,6,1)  

        self.tab2.layout.addWidget(self.labeldG,7,0)        
        self.tab2.layout.addWidget(self.dG,7,1) 
        
        self.tab2.layout.addWidget(self.labeldH,8,0)        
        self.tab2.layout.addWidget(self.dH,8,1)
        
        self.tab2.layout.addWidget(self.labeldJ,9,0)        
        self.tab2.layout.addWidget(self.dJ,9,1)
        
        self.tab2.layout.addWidget(self.labeldos,10,0)        
        self.tab2.layout.addWidget(self.dos,10,1)
        
        self.tab2.layout.addWidget(self.labeldts,11,0)        
        self.tab2.layout.addWidget(self.dts,11,1)
        
        self.tab2.layout.addWidget(self.labeldintegral,12,0)        
        self.tab2.layout.addWidget(self.dintegral,12,1)
        
        self.tab2.layout.addWidget(self.labeldPO,13,0)        
        self.tab2.layout.addWidget(self.dPO,13,1)
        
        """outputs"""
        self.tab2.layout.addWidget(self.labeldAm,6,2,3,2) 
        self.tab2.layout.addWidget(self.dAm,6,3)
        
        self.tab2.layout.addWidget(self.labeldBm,7,2) 
        self.tab2.layout.addWidget(self.dBm,7,3)
        
        self.tab2.layout.addWidget(self.labeldCm,8,2) 
        self.tab2.layout.addWidget(self.dCm,8,3)
        
        self.tab2.layout.addWidget(self.labeldDm,9,2) 
        self.tab2.layout.addWidget(self.dDm,9,3)
        
        self.tab2.setLayout(self.tab2.layout)
                
        
#        layout = QVBoxLayout() 
                
        self.tab2.layout.addWidget(self.push2)
        
        
        """"""""""""""""""""""""""""""
        """"""""""""""""""""""""""""""
        layout.addWidget(self.tabs)

        self.push1.clicked.connect(self.CtrbObsv)
        self.push2.clicked.connect(self.fullstate)
#                
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Controllability and observablity checker and full state observer designer ")
        
        self.da = None
        
        
      
    def CtrbObsv(self) :
        #try :  
            A = eval(self.ctrbA.text())
            B = eval(self.ctrbB.text())
            C = eval(self.ctrbC.text())
            ct = control.ctrb(A,B)
            ob = control.obsv(A,C)
            rank_con = matrix_rank(ct)
            rank_obs = matrix_rank(ob)
            lenA = len(A[0])
            if(rank_con==len(A[0])):
                self.outputC.setText("This system is Controllable")
            else:
                self.outputC.setText("This system is Not controllable")
                
            if(rank_obs==len(A[0])):
                self.outputO.setText("This system is Observable")
            else:
                self.outputO.setText("This system is Not observable")

    def fullstate(self) :
        #try :  
            F = eval(self.dF.text())
            G = eval(self.dG.text())
            H = eval(self.dH.text())
            J = eval(self.dJ.text())
            os = eval(self.dos.text())
            os = os/100
            ts = eval(self.dts.text())
            integral = eval(self.dintegral.text())
            PO = eval(self.dPO.text())
            
            zeta = -math.log(os)/math.sqrt(math.log(os)**2 + (math.pi**2))
            wn = 4/(zeta*ts)
            #sys_ss = control.matlab.ss(F,G,H,J)
            n,d = scipy.signal.ss2tf(F,G,H,J)
            z = np.roots(n[0])
            p = [z[0], complex(-zeta*wn,(wn*math.sqrt(1-zeta**2))), complex(-zeta*wn,-(wn*math.sqrt(1-zeta**2))), integral]
            #row2 = [ [0,F[0][0],F[0][1],F[0][2]], [0,F[1][0],F[1][1],F[1][2]], [0, F[2][0],F[2][1],F[2][2] ] ]
            A2 = [ [0,-H[0],-H[1],-H[2]],[0,F[0][0],F[0][1],F[0][2]], [0,F[1][0],F[1][1],F[1][2]], [0, F[2][0],F[2][1],F[2][2] ] ]
            B2 = [ [0],[ G[0][0] ], [ G[1][0] ], [ G[2][0] ] ]
            K = control.acker(A2,B2,p)
            KI = K[0,0]
            KO = [K[0,1], K[0,2], K[0,3] ]
            L =  np.transpose(control.acker( np.transpose(F), [ [H[0]], [H[1]], [H[2]] ], PO ) )
            LH = L*H
            X = F-L*H
            
            self.da = "Am =\n"
           
            Am = [ [ 0,-H[0],-H[1],-H[2],0,0,0]  , \
                  [ -G[0][0]*KI,F[0][0],F[0][1],F[0][2],G[0][0]*KO[0],G[0][0]*KO[1],G[0][0]*KO[2]]  , \
                  [ -G[1][0]*KI,F[1][0],F[1][1],F[1][2],G[1][0]*KO[0],G[1][0]*KO[1],G[1][0]*KO[2]]  , \
                  [ -G[2][0]*KI,F[2][0],F[2][1],F[2][2],G[2][0]*KO[0],G[2][0]*KO[1],G[2][0]*KO[2]]  ,  \
                  [ -G[0][0]*KI,LH[0,0],LH[0,1],LH[0,2],X[0,0]-G[0][0]*KO[0],X[0,1]-G[0][0]*KO[1],X[0,2]-G[0][0]*KO[2] ] , \
                  [ -G[1][0]*KI,LH[1,0],LH[1,1],LH[1,2],X[1,0]-G[1][0]*KO[0],X[1,1]-G[1][0]*KO[1],X[1,2]-G[1][0]*KO[2] ] , \
                  [ -G[2][0]*KI,LH[2,0],LH[2,1],LH[2,2],X[2,0]-G[2][0]*KO[0],X[2,1]-G[2][0]*KO[1],X[2,2]-G[2][0]*KO[2] ] , \
                 ]
            
            self.da += str(Am)
            self.da+=" \n\nBm = \n"
            Bm = [[1],[0],[0],[0],[0],[0],[0]]
            self.da+= str(Bm)
            self.da+=" \n\nCm = \n"            
            Cm = [0,H[0],H[1],H[2],0,0,0]
            self.da+= str(Cm)
            self.da+=" \n\nDm = \n"            
            Dm = J
            self.da+= str(Dm)
            
            print(Am)
            
            self.dAm.setText(str(Am))
            self.dBm.setText(str(Bm))
            self.dCm.setText(str(Cm))
            self.dDm.setText(str(Dm))
            

# 
#        
#        
        
    def saveas(self):
        fileName, _ = QFileDialog.getSaveFileName(self)
        if fileName:
             with open(fileName,'w') as sfile:
                 sfile.write(self.da)
   

    def about(self) :
        QMessageBox.about(self, 
            "About the project",
            """<b>Project ME 701, Fall 2017 </b>
               <p>Copyright &copy; 2017, All Rights Reserved.
               <p>Python %s -- Qt %s -- PyQt %s on %s""" %
            (platform.python_version(),
             QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))              
                 

        
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""        



app = QApplication(sys.argv)



form = Form()
form.show()

app.exec_()
