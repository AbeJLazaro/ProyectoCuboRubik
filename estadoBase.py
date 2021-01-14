from abc import abstractmethod,ABC

class EstadoProblema:
  '''
  Esta clase es abstracta
  Tendrá métodos que adelante sobre escribiremos
  para cada uno de los problemas que nosotros
  necesitemos, ya sea ajedrez, puzzle 15, etc
  '''

  @abstractmethod
  def expandir():
    '''
    return: conjunto de estados sucesores
    '''
    pass

  @abstractmethod
  def obtenerProfundidad():
    '''
    return: la profundidad del nodo-estado
    '''
    pass

  @abstractmethod
  def obtenerPadre():
    '''
    return: Padre del estado
    '''
    pass
