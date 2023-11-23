from Bases.Criptos.AES import AES
from Bases.Criptos.DES import DES
from Bases.Criptos.ALE import ALE
from Bases.Criptos.SEM import SEM

class Base:
    def __init__(self):
        pass

    def escolher(self, tam):
        if   tam == 1:
            pass

        elif tam == 8:
            pass

        elif tam == 32:
            pass

        elif tam == 64:
            pass

        elif tam == 128:
            pass
    
    def ambientar(self, tipo):
        if tipo == "Conjunto":
            pass

        if tipo == "Base":
            pass
    
    def selecionar(self, opcao):
        
        algoritmo = None
        if opcao == "AES":
            algoritmo = AES()
        elif opcao == "DES":
            algoritmo = DES()
        elif opcao == "ALE":
            algoritmo = ALE()
        elif opcao == "SEM":
            algoritmo = SEM()
        return algoritmo
        
    def gerar():
        algoritmo().encriptar(simples, chave, modo_op, iv, nonce)
