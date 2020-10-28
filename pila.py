# orientacion: [ <--> E/S
class Stack:
    def __init__(self):
        self.pila = []

    def __repr__(self):
        return str(self.pila)

    def empty(self):
        self.pila.clear()

    def size(self):
        return len(self.pila)

    def isEmpty(self):
        return self.size() == 0

    def push(self, elemento):
        self.pila.append(elemento)

    def pop(self):
        dato = None
        if not self.isEmpty():
            dato = self.pila.pop()
        return dato

    def top(self):
        dato = None
        if not self.isEmpty():
            dato = self.pila[(len(self.pila)-1)]
        return dato

    def clone(self):
        pilaNueva = Stack()
        for elemento in self.pila:
            pilaNueva.pila.append(elemento)
        return pilaNueva

    def invertir(self):
        pilaAux = self.clone()
        self.empty()
        while not pilaAux.isEmpty():
            self.push(pilaAux.pop())


    def posicion(self, elemento):
        posicion = self.size() - 1
        pilaAux = self.clone()
        while posicion > 0 and self.top() != elemento:
            pilaAux.pop()
            posicion -= 1
        if self.top() == elemento:
            return posicion
        else:
            raise Exception("Elemento no valido")


