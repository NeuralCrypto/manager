TAM_BASE_PREFIX      = {"A": 2**16, "B":2**17,  "C": 2**18, "D": 2**19}
TAM_CHAVE_PREFIX_AES = {"A": 128,   "B": 192,   "C": 256}
TAM_CHAVE_PREFIX_DES = {"A": 64}

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