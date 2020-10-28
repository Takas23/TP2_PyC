from enum import Enum


class ZonaAuxilio(int,Enum):
  Sur = 0
  Norte = 1
  Este = 2
  Oeste = 3
  CABA = 4


class TipoAuxilio(int,Enum):
  Remolque = 0
  Reparacion = 1


class EstadoAuxilio(int,Enum):
  Espera = 0
  Aprobado = 1



