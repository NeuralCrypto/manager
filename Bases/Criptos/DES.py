import os

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from A_Constantes.Tamanhos import SUB_EXPERIMENTOS


class DES:

    TAM_BLOCO = [64]
    TAM_CHAVE = [56]
    PREFIXO     = {"A": 64}
    
    MODOS = {
        "ECB": DES.MODE_ECB,
        "CBC": DES.MODE_CBC,
        "CFB": DES.MODE_OFB,
        "OFB": DES.MODE_CFB,
        "CTR": DES.MODE_CTR
    }

    def __init__(self):
        pass

    def encriptar(self, simples, chave, modo_op, iv=None, nonce=None):
        
        cifra = DES.new(chave, self.MODOS[modo_op], iv=iv, nonce=nonce)
        cifrado = cifra.encrypt(simples)
        return cifrado
    
    def gerar_chave(self, endereco):
        """
        Gera os arquivos de chaves do DES para 64 bits.
        """

        for letra in self.PREFIXO:

            # Abrir arquivo de chaves
            end_chave = endereco.format(chave=letra, numero=self.PREFIXO[letra])
            arq_chave = open(end_chave, "wb")

            chave = None

            tamanho = self.PREFIXO[letra]

            for sub in range(0, SUB_EXPERIMENTOS):
                chave = get_random_bytes(int(tamanho/8))
                arq_chave.write(chave)
            arq_chave.close()