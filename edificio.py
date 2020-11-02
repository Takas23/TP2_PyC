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


    def establecerOficina(self, numeroPiso, numeroHabitaculo, oficinaAtencion):
        if self.habitaculoLibre(numeroPiso, numeroHabitaculo):
            edificioAux = self.edificio.clone()
            self.edificio.empty()
            edificioAux.invertir()
            pisoActual = 0
            while not edificioAux.isEmpty():
                self.edificio.push(edificioAux.pop())
                if numeroPiso == pisoActual:
                    self.establecerOficinaUltimoPiso(numeroHabitaculo, oficinaAtencion)
                pisoActual += 1


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
            if pisoActual.dequeue().esCritica():
                cant += 1
        return cant

    def cantidadDeOficinasCriticasTotal(self, piso):
        cant = 0
        if piso == 0:
            cant += self.cantidadDeOficinasCriticas(piso)
        else:
            cant = self.cantidadDeOficinasCriticas(piso) + self.cantidadDeOficinasCriticasTotal(piso-1)
        return cant


######################################
    #REVISAR
    def oficinaMenosRecargada(self):
        pisos = self.cantPisos -1
        aux = None
        while pisos != 0:
            aux = self.menorEntre(self.oficinaMenosRecargadaEnPiso(pisos), self.oficinaMenosRecargadaEnPiso(pisos-1))
            pisos -= 1
        return self.menorEntre(aux, self.oficinaMenosRecargadaEnPiso(0))

#######################
# AUXILIAR de oficinaMenosRecargada()
    def oficinaMenosRecargadaEnPiso(self, numeroPiso):
        pisoAux = self.clonPiso(numeroPiso)
        minimo = 999
        oficina = None
        while not pisoAux.isEmpty():
            if pisoAux.top() is not None:
                if pisoAux.top().auxiliosPorTipo()[0] < minimo:
                    minimo = pisoAux.top().auxiliosPorTipo()[0]
                    oficina = pisoAux.dequeue()
            pisoAux.dequeue()
        return oficina

    def menorEntre(self, ofi1, ofi2):
        salida = ofi1
        if ofi1 is None:
            salida = ofi2
        if ofi1 and ofi2:
            if ofi1.auxiliosPorTipo()[0] > ofi2.auxiliosPorTipo()[0]:
                salida = ofi2
        return salida


#######################

# AUXILIAR de oficinaMenosRecargadaEnPiso()
    def pisoVacio(self, nroPiso):
        pisoAux = self.clonPiso(nroPiso)
        oficinas = 0
        while not pisoAux.isEmpty():
            if pisoAux.top() is not None:
                oficinas += 1
                pisoAux.dequeue()
            pisoAux.dequeue()
        return oficinas == 0

    def buscaOficina(self, nroInterno):
        piso = self.cantPisos - 1
        while piso >= 0:
            if self.habitaculoOficinaEn(nroInterno, piso) is None:
                piso -= 1
            else:
                return piso, self.habitaculoOficinaEn(nroInterno, piso)
        raise Exception("Numero de Interno no valido")

# AUXILIAR de busca oficina
# devuelve el nro habitaculo en donde se encuentra la oficina buscada en el piso dado
    def habitaculoOficinaEn(self, nroInterno, piso):
        pisoAux = self.clonPiso(piso)
        habitaculo = 0
        while not pisoAux.isEmpty():
            if pisoAux.top() is None:
                pisoAux.dequeue()
                habitaculo += 1
            else:
                if pisoAux.top().getInterno() != nroInterno:
                    pisoAux.dequeue()
                    habitaculo += 1
                else:
                    return habitaculo

# AUXILIAR
# Retorna la oficina en el (piso, habitaculo)
    def getOficinaEn(self, listPisoHabit):
        piso = listPisoHabit[0]
        habit = listPisoHabit[1]
        pisoAux = self.clonPiso(piso)
        habitAux = 0
        while not pisoAux.isEmpty():
            if habit == habitAux:
                return pisoAux.top()
            pisoAux.dequeue()
            habitAux += 1


# Al recibir una pila la invierto para enviar por orden de llegada ya que ingresan a una cola
    def centralTelefonica(self, pilaDeAuxilios):
        pilaAux = pilaDeAuxilios
        pilaAux.invertir()
        while not pilaAux.isEmpty():
            self.oficinaMenosRecargada().recibirAuxilio(pilaAux.pop())

# ¿recibe oficina o solo numero¡?
# REVISAR
    def moverAuxilio(self, nroPatente, internoOficinaOrigen, internoOficinaDestino):
        ofOrigen = self.getOficinaEn(self.buscaOficina(internoOficinaOrigen))
        ofDestino = self.getOficinaEn(self.buscaOficina(internoOficinaDestino))
        if self.verOficina(internoOficinaOrigen) and self.verOficina(internoOficinaDestino):
            auxilio = ofOrigen.buscarAuxilio(nroPatente)
            ofOrigen.eliminarAuxilio(nroPatente)
            ofDestino.recibirAuxilio(auxilio)
        else:
            raise Exception("interno no valido")



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

    def verOficina(self, nroInterno):
        existe = False
        if self.buscaOficina(nroInterno):
            existe = True
        return existe