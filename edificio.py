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
        if numeroPiso == self.cantPisos - 1:
            self.establecerOficinaUltimoPiso(numeroHabitaculo, oficinaAtencion)
        else:
            edificioAux = self.edificio.clone().invertir()
            self.edificio.empty()
            pisoActual = 0
            while not edificioAux.isEmpty():
                if numeroPiso == pisoActual:
                    self.establecerOficinaUltimoPiso(numeroHabitaculo, oficinaAtencion)
            self.edificio.push(edificioAux.pop())


# AUXILIAR de establecerOficina()
# coloca la oficina en el piso superior
    def establecerOficinaUltimoPiso(self, nroHabitaculo, oficinaAtencion):
        piso = self.edificio.top().clone()
        self.edificio.top().empty()
        habitActual = 0
        while not piso.isEmpty():
            if nroHabitaculo == habitActual:
                self.edificio.top().enqueue(oficinaAtencion)
                piso.dequeue()
            self.edificio.top().enqueue(piso.dequeue())
            habitActual += 1

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
        pisoAux = None
        if self.verPiso(numeroPiso):
            edificioAux = self.edificio.clone()
            while numeroPiso != edificioAux.size()-1:
                edificioAux.pop()
            pisoAux = edificioAux.top().clone()
        return pisoAux

# VERIFICADORES
    def verPiso(self, numeroPiso):
        if numeroPiso < self.edificio.size():
            return True
        else:
            raise Exception("Piso no valido")

    def verHabitaculo(self,numeroPiso, numeroHabitaculo):
        if numeroHabitaculo < self.cantHabitaculos and self.verPiso(numeroPiso):
            return True
        else:
            raise Exception("Habitaculo y/o Piso no valido")

    def habitaculoLibre(self, numeroPiso, numeroHabitaculo):
        if self.verHabitaculo(numeroPiso, numeroHabitaculo):
            pisoAux = self.clonPiso(numeroPiso)
            habitActual = 0
            while habitActual != numeroHabitaculo:
                pisoAux.dequeue()
                habitActual += 1
            return pisoAux.top() == None
        else:
            raise Exception("Habitaculo ocupado")


