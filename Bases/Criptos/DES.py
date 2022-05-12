from Crypto.Cipher import DES

class DES:

    TAM_BLOCO = 64
    TAM_CHAVE = 56
    
    MODOS = {
        "ECB": DES.MODE_ECB,
        "CBC": DES.MODE_CBC,
        "CFB": DES.MODE_OFB,
        "OFB": DES.MODE_CFB,
        "CTR": DES.MODE_CTR
    }

    def __init__(self):
        pass

    def encriptar(self):
        pass
    