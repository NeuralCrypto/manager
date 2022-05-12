from Crypto.Cipher import AES

class AES:

    TAM_BLOCO   = 128
    TAM_CHAVE   = [128, 192, 256]
    TAM_ROUND   = [10, 12, 14]
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
    
    def gerar_chave(self):
        chave = 0
        return chave
