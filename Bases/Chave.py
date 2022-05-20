from Crypto.Random import get_random_bytes

from Bases.Criptos.AES import *
from Bases.Criptos.DES import *
from Bases.Criptos.ALE import *
from Bases.Criptos.SEM import *

from A_Constantes.Pastas        import *
from A_Constantes.Computadores  import COMPUTADORES
from A_Constantes.Algoritmos    import *
from A_Constantes.Arquivos      import ARQ_CHAVE


class Chave:

    def __init__(self):
        pass

    def gerar(self):
        
        for l in LARGURA_ANALISE:
            for a in ALGORITMOS:                
                for c in COMPUTADORES:
                    
                    if c["modos"][a["sigla"]]:
                        if a["sigla"] == "AES":
                            algoritmo = AES()
                        elif a["sigla"] == "DES":
                            algoritmo = DES()
                        elif a["sigla"] == "ALE":
                            algoritmo = ALE()
                        elif a["sigla"] == "SEM":
                            algoritmo = SEM()
                        
                        endereco = os.path.join(PASTA_BASE_CHAVES, ARQ_CHAVE)
                        endereco = endereco.format(
                            largura=l["nome"],
                            algoritmo=a["sigla"],
                            computador=c["nome"],
                            chave="{chave}",
                            numero="{numero}"
                        )

                        algoritmo.gerar_chave(endereco)
                    
                    else:
                        continue