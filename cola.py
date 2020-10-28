from pila import *


# orientacion: S <-- <-- E
class Queue:
    def __init__(self):
        self.cola = []

    def __repr__(self):
        return str(self.cola)

    def empty(self):
        self.cola.clear()

    def size(self):
        return len(self.cola)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, element):
        self.cola.append(element)

    def dequeue(self):
        dato = None
        if not self.isEmpty():
            dato = self.cola.pop(0)
        return dato

    def top(self):
        dato = None
        if not self.isEmpty():
            dato = self.cola[0]
        return dato

    def clone(self):
        colaNew = Queue()
        for element in self.cola:
            colaNew.enqueue(element)
        return colaNew

    def invertir(self):
        pilaAux = Stack()
        while not self.isEmpty():
            pilaAux.push(self.dequeue())
        while not pilaAux.isEmpty():
            self.enqueue(pilaAux.pop())

# devuelve la posicion/indice del elemento
    def posicion(self, elemento):
        posicion = 0
        colaAux = self.clone()
        while posicion < self.size() and self.top() != elemento:
            colaAux.dequeue()
            posicion += 1
        if self.top() == elemento:
            return posicion
        else:
            raise Exception("Elemento no valido")

    def eliminar(self, posicion):
        colaAux = self.clone()
        self.empty()
        pos = 0
        while not colaAux.isEmpty():
            if pos == posicion:
                colaAux.dequeue()
            self.enqueue(colaAux.dequeue())
            pos += 1