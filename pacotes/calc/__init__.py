#  Pacote de FACHADA (facade) : apenas chama os pacotes e funções

from pacote1.modulo1 import soma
from pacote2.modulo1 import subtracao

__all__=['soma','subtracao']