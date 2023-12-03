import logging
import sys
import random

from PySide2.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout


class Anuncio(object):
    #clase que representa la pestaña que va ser mostrada
    def __init__(self,slogan,parent=None):
        super(Anuncio, self).__init__(parent)
        
        #Creamos una disposición para que el anuncip pueda ser mostrado
        self.label=QLabel(slogan)
        layout=QVBoxLayout()
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        
        #para evitar que se pueda cerrar desde la ventana abierta
        '''
        def CloseEvent(self,event):
            event.ignore()
        '''
        
class Adware(QApplication):
    
    anuncios = ['KAWASAKI','KAGO','STRIPPER','KRICO']
    def __init__(self, args):
        super(Adware,self).__init__(args)
        
    def crear_ventanas(self,slogan):
        #creamos la ventanas con los slogan
        window = Anuncio(slogan=slogan)
        window.show()
        return window

    def enseniar_anuncios(self):
        anuncios=[]
        for anuncio in anuncios:
            ventana = self.crear_ventanas(anuncio)
            x_cor,y_cord = random.randint(1,800),random.randint(1, 600)
            ventana.move(x_cor,y_cord)
            anuncios.append(ventana)
        return anuncios
    
adware = Adware(sys.argv)
windows= adware.enseniar_anuncios()
        
