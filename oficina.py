from cola import *
from auxilio import *


class OficinaAtencion:
    def __init__(self, nroInterno, cantCritica=50):
        if 0 < nroInterno <= 999:
            self.nroInterno = nroInterno
        else:
            raise Exception("Numero de Interno no valido")
        self.cantCritica = cantCritica
        self.colaRemolque = Queue()
        self.colaReparacion = Queue()

    def __repr__(self):
        return str(self.nroInterno)

    def recibirAuxilio(self, auxilio):
        if auxilio.getTipo() == TipoAuxilio(0).name:
            self.colaRemolque.enqueue(auxilio)
        else:
            self.colaReparacion.enqueue(auxilio)
#        if self.esCritica():
#            raise Exception("Oficina en situacion critica")

    def primerAuxilioAEnviar(self):
        salida = None
        if self.colaNoVacia(self.colaRemolque):
            salida = self.colaRemolque.top()
        elif self.colaNoVacia(self.colaReparacion):
            salida = self.colaReparacion.top()
        return salida

    def enviarAuxilio(self, zonaDeGrua):
        salida = self.buscaZona(self.colaRemolque, zonaDeGrua)
        if salida is None:
            salida = self.buscaZona(self.colaReparacion, zonaDeGrua)
        return salida

# AUXILIAR de enviarAuxilio()
# busca por zona y desencola el primero encontrado
    def buscaZona(self, cola, zonaDeGrua):
        colaAux = cola.clone()
        cola.empty()
        auxilio = None
        while self.colaNoVacia(colaAux):
            if colaAux.top().getPartida() == zonaDeGrua:
                auxilio = colaAux.dequeue()
            cola.enqueue(colaAux.dequeue())
        return auxilio

    def auxiliosPorTipo(self):
        return self.colaRemolque.size(), self.colaReparacion.size()

    def cantidadTotalAuxilios(self):
        return sum(self.auxiliosPorTipo())

# devuelve si hay algun valor mayor a la cantidad critica entre los valores de cada cola
    def esCritica(self):
        return any(i >= self.cantCritica for i in self.auxiliosPorTipo())

    def auxiliosEnEspera(self):
        enEspera = 0
        clon = self.colaRemolque.clone()
        while not clon.isEmpty():
            if clon.dequeue().getEstado() == EstadoAuxilio(0).name:
                enEspera += 1
        clon = self.colaReparacion.clone()
        while not clon.isEmpty():
            if clon.dequeue().getEstado() == EstadoAuxilio(0).name:
                enEspera += 1
        return enEspera

    def buscarAuxilio(self, nroPatente):
        if self.verAuxilio(nroPatente):
            auxilio = self.buscarPatente(self.colaRemolque, nroPatente)
            if auxilio is None:
                auxilio = self.buscarPatente(self.colaReparacion, nroPatente)
            return auxilio

# AUXILIAR de buscarAuxilio()
# Busca por patente en la cola enviada por parametro y devuelve sin desencolar
    def buscarPatente(self, cola, nroPatente):
        auxilio = None
        colaAux = cola.clone()
        cola.empty()
        while self.colaNoVacia(colaAux):
            if colaAux.top().getPatente() == nroPatente:
                auxilio = colaAux.top()
            cola.enqueue(colaAux.dequeue())
        return auxilio

    def eliminarAuxilio(self, nroPatente):
        aux = self.buscarAuxilio(nroPatente)
        if self.verAuxilioEn(self.colaRemolque, nroPatente):
            pos = self.colaRemolque.posicion(aux)
            self.eliminarEn(self.colaRemolque, pos)
        elif self.verAuxilioEn(self.colaReparacion, nroPatente):
            pos = self.colaReparacion.posicion(aux)
            self.eliminarEn(self.colaReparacion, pos)
        else:
            raise Exception("Numero de patente no valido")

    def eliminarEn(self, cola, posicion):
            cola.eliminar(posicion)

# REVISAR
    def cambiaDeTipo(self, nroPatente):
        if self.verAuxilio(nroPatente):
            aux = self.buscarAuxilio(nroPatente)
            self.eliminarAuxilio(nroPatente)
            aux.cambiaTipo()
            self.recibirAuxilio(aux)

        else:
            raise Exception("Auxilio no valido")

# VERIFICADORES
    def verAuxilioEn(self, cola, nroPatente):
        return self.buscarPatente(cola, nroPatente) is not None

    def verAuxilio(self, nroPatente):
        return self.verAuxilioEn(self.colaRemolque, nroPatente) or self.verAuxilioEn(self.colaReparacion, nroPatente)

    def colaNoVacia(self, cola):
        return not cola.isEmpty()


