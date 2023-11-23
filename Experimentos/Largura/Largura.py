
from Experimentos.Largura.Bit_1      import Bit_1
from Experimentos.Largura.Bit_8      import Bit_8
from Experimentos.Largura.Bit_16     import Bit_16
from Experimentos.Largura.Bit_32     import Bit_32
from Experimentos.Largura.Bit_64     import Bit_64
from Experimentos.Largura.Bit_128    import Bit_128

class Largura:

    def __init__(self):
        pass

    def escolher(self, tamanho):

        largura = None

        if tamanho == 1:
            print("Gerando experimentos para 1-bit")
            largura = Bit_1()
        
        elif tamanho == 8:
            print("Gerando experimentos para 8-bit")
            largura = Bit_8()
            
        elif tamanho == 16:
            print("Gerando experimentos para 16-bit")
            largura = Bit_16()
        
        elif tamanho == 32:
            print("Gerando experimentos para 32-bit")
            largura = Bit_32()
        
        elif tamanho == 64:
            print("Gerando experimentos para 64-bit")
            largura = Bit_64()
        
        elif tamanho == 128:
            print("Gerando experimentos para 128-bit")
            largura = Bit_128()
        
        else:
            print("Erro: Largura errada")
            exit
        
        return largura
