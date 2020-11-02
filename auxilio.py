from tipos import TipoAuxilio, EstadoAuxilio, ZonaAuxilio


class Auxilio:
    def __init__(self, patente, zonaPartida, zonaDestino, tipo, estado):
        self.patente = patente
        self.zonaPartida = verZona(zonaPartida)
        self.zonaDestino = verZona(zonaDestino)
        self.tipo = verTipo(tipo)
        self.estado = verEstado(estado)

    def __repr__(self):
        return str(self.patente)

    def getTipo(self):
        return self.tipo

    def getEstado(self):
        return self.estado

    def getPartida(self):
        return self.zonaPartida

    def getPatente(self):
        return self.patente

    def cambiaTipo(self):
        if self.getTipo() == TipoAuxilio(0).name:
            self.tipo = TipoAuxilio(1).name
        else:
            self.tipo = TipoAuxilio(0).name

# VERIFICACIONES
def verTipo(tipo):
    if tipo in TipoAuxilio._member_names_:
        return tipo
    else:
        raise Exception("Tipo no valido")

#def verTipo(tipo):
#    if tipo == 0 or 1:
#        return TipoAuxilio(tipo).name

def verEstado(estado):
    if estado in EstadoAuxilio._member_names_:
        return estado
    else:
        raise Exception("Estado no valido")

#def verEstado(estado):
#    if estado == 0 or 1:
#        return EstadoAuxilio(estado).name

def verZona(zona):
    if zona in ZonaAuxilio._member_names_:
        return zona
    else:
        raise Exception("Zona no valida")

#def verZona(zona):
#    if 0 <= zona <= 4:
#        return ZonaAuxilio(zona).name



