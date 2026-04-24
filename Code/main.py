import grilles 
import interface
import sys 
import numpy as np


app = interface.QtWidgets.QApplication(sys.argv) 
Dialog = interface.QtWidgets.QDialog()
ui = interface.Ui_Dialog()
ui.setupUi(Dialog,10) 
Dialog.show() 

g = grilles.GrilleJeu()
g[0,0].changeEtat('Rocher')
g[5,5].changeEtat('Rocher')
g[2,0].changeEtat('Poisson')
g[3,0].changeEtat('Poisson')
g.afficher(ui)
"""
print(ui.grid)
p = grilles.Polyomino(np.array([[0,1,0],[1,1,1]]),'r')
p.afficher(ui)
"""

sys.exit(app.exec())
