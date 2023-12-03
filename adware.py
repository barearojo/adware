import logging
import sys
import random

from PySide2.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout


class Anuncio(object):
    #clase que representa la pestaña que va ser mostrada
    def __init__(self,slogan,parent=None):
        super(Anuncio, self).__init__(parent)
        
        #Creamos una disposición para que el anuncip pueda ser mostrado
        

        