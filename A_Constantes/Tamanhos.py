TAM_BASE_PREFIX      = {"A": 2**16, "B":2**17,  "C": 2**18, "D": 2**19}
TAM_CHAVE_PREFIX_AES = {"A": 128,   "B": 192,   "C": 256}
TAM_CHAVE_PREFIX_DES = {"A": 64}

TAM_BLOCOS = {
    "DES": 64,
    "AES": 128,
    "SEM": 64,
    "ALE": 64
}

ALGO_CHAVE_PREFIX = {
    "DES": {"A": 64},
    "AES": {"A": 128,   "B": 192,   "C": 256},
    "SEM": {"Z": 0},
    "ALE": {"Z": 0}
}

LARGURA_ANALISE = {
    "nome": "1-bit",    "tamanho": 1,
    "nome": "8-bit",    "tamanho": 8,
    "nome": "32-bit",   "tamanho": 32,
    "nome": "64-bit",   "tamanho": 64,
    "nome": "128-bit",  "tamanho": 128
}

SUB_EXPERIMENTOS = 4

TAMANHO_ARQUIVO  = 2**23
TAM_MAX_BLOCO    = 512
TAM_MAX_BASE     = 2**19
TAM_MAX_IV       = 128

MAX_ARQUIVOS_MSG = int((TAM_MAX_BASE * TAM_MAX_BLOCO) / TAMANHO_ARQUIVO)
MAX_ARQUIVOS_IV  = int((TAM_MAX_BASE * TAM_MAX_IV) / TAMANHO_ARQUIVO)
