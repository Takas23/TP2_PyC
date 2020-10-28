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
# REVISAR
def verTipo(tipo):
    if tipo == TipoAuxilio(0).name or TipoAuxilio(1).name:
        return tipo
    else:
        raise Exception("Tipo no valido")


def verEstado(estado):
    if estado == EstadoAuxilio(0).name or EstadoAuxilio(1).name:
        return estado
    else:
        raise Exception("Estado no valido")


def verZona(zona):
    for z in ZonaAuxilio:
        if zona == z.name:
            return zona
#        else:
#            raise Exception("Zona no valida")


