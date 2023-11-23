from A_Constantes.Pastas        import LARGURA_ANALISE
from A_Constantes.Algoritmos    import TIPOS_ALGORITMOS
from A_Constantes.Computadores  import COMPUTADORES

from Experimentos.Largura.Largura import Largura

class Experimentos:

    def __init__(self):
        pass

    def escolher(self):
        
        for l in LARGURA_ANALISE:                       # Largura de Bits
            
            if l["tamanho"] == 128:
                continue
            else:
                largura = Largura().escolher(l["tamanho"])
            
            for a in TIPOS_ALGORITMOS:                  # Algoritmos criptográficos
                for c in COMPUTADORES:                  # Computadores
                    
                    if c["modos"][a]:
                        largura.experimentar(a, c)
