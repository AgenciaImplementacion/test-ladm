
def name():
    return "PruebasLADM"

def description():
    return "Pruebas LADM"

def version():
    return "Version 0.1"



def qgisMinimumVersion():
    return "2.0"

def author():
    return "Sergio Ramírez"

def email():
    return "sergio.ramirez@incige.com"


def classFactory(iface):
    from .pluginLADM import testLADM
    return testLADM(iface)
