from edificio import *


pila1 = Stack()
pila2 = Stack()
cola1 = Queue()
cola2 = Queue()

cola1.enqueue(1); cola1.enqueue(2)
cola2.enqueue(3); cola2.enqueue(4), cola2.enqueue(5)
pila1.push(cola1); pila1.push(cola2)
pila2.push(1); pila2.push(3)

auxilio1 = Auxilio("AAA111", "Sur", "Norte", "Remolque", "Aprobado")
auxilio2 = Auxilio("BBB111", "Norte", "Norte", "Reparacion", "Aprobado")
auxilio3 = Auxilio("AAA222", "Oeste", "Oeste", "Remolque", "Espera")
auxilio4 = Auxilio("BBB222", "Este", "CABA", "Reparacion", "Espera")

oficina1 = OficinaAtencion(50)

edificio1 = EdificioEmpresa(3, 4)

# pila ok
#print(pila2)
#print(pila2.posicion(3))
#print(pila2.clone())
#pila1.invertir()
#print(pila1)

# cola ok
#print(cola2)
#print(cola2.posicion(3))
#cola2.eliminar(0)
#print(cola2.index(5))
#print(cola2.clone())
#cola2.invertir()
#print(cola2)

# auxilio ok

# print(auxilio1)
# print(auxilio1.getPartida())
# print(auxilio1.getTipo())
#auxilio1.cambiaTipo()
#print(auxilio1.getTipo())

# oficina OK

# Remolques <[1, 3]<
# Reparacion <[2, 4]<
oficina1.recibirAuxilio(auxilio1); oficina1.recibirAuxilio(auxilio2)
oficina1.recibirAuxilio(auxilio3); oficina1.recibirAuxilio(auxilio4)
#print(oficina1.primerAuxilioAEnviar())
#oficina1.enviarAuxilio("Sur")
#print(oficina1.auxiliosPorTipo())
#print(oficina1.primerAuxilioAEnviar())
#print(oficina1.cantidadTotalAuxilios())
#print(oficina1.auxiliosEnEspera())
#print(oficina1.buscarAuxilio("BBB222"))
#print(oficina1.verAuxilio("BBB111"))
#oficina1.eliminarAuxilio("BBB111")
#print(oficina1.cantidadTotalAuxilios())
#print(oficina1.auxiliosPorTipo())
#print(oficina1.verAuxilioEn(oficina1.colaRemolque, "AAA111"))
#print(oficina1.verAuxilio("ANA111"))
#print(oficina1.verAuxilio("BBB111"))
#print(auxilio3.getTipo())
#print(oficina1.colaRemolque)
#oficina1.cambiaDeTipo("AAA222")
#print(auxilio3.getTipo())
#print(oficina1.auxiliosPorTipo())
#print(oficina1.colaRemolque)

# Edificio

print(edificio1)
#edificio1.establecerOficina(0, 2, oficina1)
#print(edificio1)

print(edificio1.habitaculoLibre(0,2))