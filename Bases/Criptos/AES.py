import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from A_Constantes.Arquivos import ARQ_CHAVE
from A_Constantes.Tamanhos import SUB_EXPERIMENTOS

class AES:

    TAM_BLOCO   = 128
    TAM_CHAVE   = [128, 192, 256]
    TAM_ROUND   = [10, 12, 14]
    PREFIXO     = {"A": 128,   "B": 192,   "C": 256}
    CHAVE_ROUND = {
        "128": 10,
        "192": 12,
        "256": 14
    }

    MODOS = {
        "ECB": AES.MODE_ECB,
        "CBC": AES.MODE_CBC,
        "CFB": AES.MODE_OFB,
        "OFB": AES.MODE_CFB,
        "CTR": AES.MODE_CTR
    }

    def __init__(self):
        pass
    
    def encriptar(self, simples, chave, modo_op, iv=None, nonce=None):

        cifra = AES.new(chave, self.MODOS[modo_op], iv=iv, nonce=nonce)
        cifrado = cifra.encrypt(simples)
        return cifrado
    
    def gerar_chave(self, endereco):
        """
        Gera os arquivos de chaves do AES para 128, 192 e 256 bits.
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

