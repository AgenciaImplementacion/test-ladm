from .resources import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class testLADM:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):



        # Check if the menu exists and get it
        self.menu = self.iface.mainWindow().findChild( QMenu, '&Test LADM' )

        # If the menu does not exist, create it!
        if not self.menu:
            self.menu = QMenu( '&Test LADM', self.iface.mainWindow().menuBar() )
            self.menu.setObjectName( '&Test LADM' )
            actions = self.iface.mainWindow().menuBar().actions()
            lastAction = actions[-1]
            self.iface.mainWindow().menuBar().insertMenu( lastAction, self.menu )

        # Finally, add your action to the menu

        self.action = QAction(QIcon(":/testLADM/resources/Z_Happy1.png"),"Gestion Interesado", self.iface.mainWindow())
        self.action.triggered.connect(self.gestionInteresado)
        #self.iface.addPluginToMenu("Test LADM", self.action)
        self.menu.addAction( self.action )

        self.action = QAction(QIcon(":/testLADM/resources/icon14.png"),"Gestionar Fuentes", self.iface.mainWindow())
        self.action.triggered.connect(self.gestionFuentes)
        #QObject.connect(self.action, SIGNAL("triggered()"),self.gestionFuentes)
        #self.iface.addPluginToMenu("Test LADM", self.action)
        self.menu.addAction( self.action )

        self.action = QAction(QIcon(":/testLADM/resources/icon14.png"),"Gestionar RRR", self.iface.mainWindow())
        self.action.triggered.connect(self.gestionRrr)
        #QObject.connect(self.action, SIGNAL("triggered()"),self.gestionRrr)
        #self.iface.addPluginToMenu("Test LADM", self.action)
        self.menu.addAction( self.action )

        self.action = QAction(QIcon(":/testLADM/resources/Z_Happy1.png"),"Gestionar BA_Unit", self.iface.mainWindow())
        self.action.triggered.connect(self.gestionBa_unit)
        #QObject.connect(self.action, SIGNAL("triggered()"),self.gestionBa_unit)
        #self.iface.addPluginToMenu("Test LADM", self.action)
        self.menu.addAction( self.action )

        self.action = QAction(QIcon(":/testLADM/resources/icon14.png"),"Gestión Geometría", self.iface.mainWindow())
        self.action.triggered.connect(self.gestionGeometria)
        #QObject.connect(self.action, SIGNAL("triggered()"),self.gestionGeometria)
        #self.iface.addPluginToMenu("Test LADM", self.action)
        self.menu.addAction( self.action )

        self.action = QAction(QIcon(":/testLADM/resources/Z_Happy1.png"),"Gestión Calidad", self.iface.mainWindow())
        self.action.triggered.connect(self.gestionCalidad)
        #QObject.connect(self.action, SIGNAL("triggered()"),self.gestionCalidad)
        #self.iface.addPluginToMenu("Test LADM", self.action)
        self.menu.addAction( self.action )

    def unload(self):
        self.iface.removePluginMenu("Test LADM", self.action)

    def gestionInteresado(self):
        QMessageBox.information(self.iface.mainWindow(), "Gestion Interesado", "Gestion Interesado")

    def gestionFuentes(self):
        QMessageBox.information(self.iface.mainWindow(), "Gestionar Fuentes", "Gestionar Fuentes")

    def gestionRrr(self):
        QMessageBox.information(self.iface.mainWindow(), "Gestionar RRR", "Gestionar RRR")

    def gestionBa_unit (self):
        QMessageBox.information(self.iface.mainWindow(), "Gestionar BA_Unit", "Gestionar BA_Unit")

    def gestionGeometria (self):
        QMessageBox.information(self.iface.mainWindow(), "Gestionar Geometría", "Gestionar Geometría")

    def gestionCalidad (self):
        QMessageBox.information(self.iface.mainWindow(), "Gestionar Calidad", "Gestionar Calidad")
