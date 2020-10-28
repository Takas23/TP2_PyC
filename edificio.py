from oficina import *
#from pila import Stack


# pisos y habitaculos desde el 0
class EdificioEmpresa:
    def __init__(self, cantPisos, cantHabitaculos):
        self.edificio = Stack()
        self.cantPisos = cantPisos
        self.cantHabitaculos = cantHabitaculos
        nPisos = cantPisos
        while nPisos != 0:
            self.edificio.push(self.creaPiso(cantHabitaculos))
            nPisos -= 1

    def __repr__(self):
        return str(self.edificio)

# AUXILIAR del __init__
    def creaPiso(self, habitaculos):
        piso = Queue()
        self.addHabitaculos(piso, habitaculos)
        return piso

# AUXILIAR de creaPiso()
    def addHabitaculos(self, piso, habitaculos):
        if habitaculos > 0:
            piso.enqueue(None)
            self.addHabitaculos(piso, habitaculos-1)

# REVISAR
    def establecerOficina(self, numeroPiso, numeroHabitaculo, oficinaAtencion):
        if self.habitaculoLibre(numeroPiso, numeroHabitaculo):
            edificioAux = self.edificio.clone().invertir()
            pisoActual = 0
            habitaculoActual = 0
            self.edificio.empty()
            while not edificioAux.isEmpty():
                if pisoActual == numeroPiso:
                    pisoAux = edificioAux.top().clone()
                    edificioAux.top().empty()
                    while not pisoAux.isEmpty():
                        if habitaculoActual == numeroHabitaculo:
                            pisoAux.dequeue()
                            edificioAux.top().enqueue(oficinaAtencion)
                        edificioAux.top().enqueue(pisoAux.dequeue())
                        habitaculoActual += 1
                self.edificio.push(edificioAux.pop())
                pisoActual += 1

# HACER RECURSIVA!
# retorna cuantas oficinas criticas hay en el piso. (iter)
    def cantidadDeOficinasCriticas(self, piso):
        cant = 0
        pisoActual = self.clonPiso(piso)
        while pisoActual.size() < 0:
            if self.clonPiso(piso).dequeue().esCritica():
                cant += 1
        return cant

    def oficinaMenosRecargada(self):
        edificioAux = self.edificio.clone()
        remolques = edificioAux.top().top().colaRemolque.size()
        oficina = edificioAux.top().top()
        while edificioAux.size() > 0:
            while self.edificio.top().size > 0:
                if remolques > edificioAux.top().top().colaRemolque.size():
                    remolques = edificioAux.top().top().colaRemolque.size()
                    oficina = edificioAux.top().top()
            self.edificio.pop()
        return self.buscaOficina(oficina)

    def buscaOficina(self, nroInterno):
        return self.habitaculoOficinaEn(nroInterno, self.cantPisos)

# AUXILIAR
    def habitaculoOficinaEn(self, nroInterno, piso):
        pisoAux = self.clonPiso(piso)
        salida = None
        while piso >= 0:
            while not pisoAux.isEmpty() and pisoAux.top() != nroInterno:
                pisoAux.dequeue()
            if pisoAux.top() == nroInterno:
                salida = piso, pisoAux.index(nroInterno)
            else:
                self.habitaculoOficinaEn(nroInterno, piso-1)
        return salida

# Al recibir una pila la invierto para enviar por orden de llegada ya que ingresan a una cola
    def centralTelefonica(self, pilaDeAuxilios):
        pilaAux = pilaDeAuxilios.invertir()
        while not pilaAux.isEmpty():
            self.internoEn(self.oficinaMenosRecargada()[0], self.oficinaMenosRecargada()[1]).recibirAuxilio(pilaAux.pop())

# Completar
    def moverAuxilio(self, nroPatente, internoOficinaOrigen, internoOficinaDestino):
        if internoOficinaOrigen.verAuxilio(nroPatente):
            internoOficinaDestino.recibirAuxilio(internoOficinaOrigen.buscarAuxilio(nroPatente))
            internoOficinaOrigen.eliminarAuxilio(nroPatente)
        else:
            raise Exception("Auxilio no valido")

# AUXILIAR
# Busca el nro de interno en determinado piso y habitaculo
    def internoEn(self, nroPiso, nroHabitaculo):
        piso = self.clonPiso(nroPiso)
        while not piso.isEmpty() and nroHabitaculo != piso.size()-1:
            piso.dequeue()
        return piso.top()

# AUXILIAR
# retorna un clon del piso sin modificar el edificio
    def clonPiso(self, numeroPiso):
        edificioAux = self.edificio.clone()
        while numeroPiso != edificioAux.size():
            edificioAux.pop()
        return edificioAux.top()

# VERIFICADORES
    def verPiso(self, numeroPiso):
        return numeroPiso < self.edificio.size()

    def verHabitaculo(self, numeroHabitaculo):
        return numeroHabitaculo < self.cantHabitaculos

    def habitaculoLibre(self, numeroPiso, numeroHabitaculo):
        if self.verPiso(numeroPiso) and self.verHabitaculo(numeroHabitaculo):
            edificioAux = self.edificio.clone()
            while numeroPiso != edificioAux.size():
                edificioAux.pop()
            habitaculoActual = 0
            while habitaculoActual != numeroHabitaculo:
                edificioAux.pop()
                habitaculoActual += 1
            return edificioAux.top().top() is None
        else:
            raise Exception("Piso y/o Habitaculo no valido")


