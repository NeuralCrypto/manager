import os
ALGORITMOS = {
    "sigla": "AES", "nome": "AES",
    "sigla": "DES", "nome": "DES",
    "sigla": "SEM", "nome": "Original",
    "sigla": "ALE", "nome": "Aleatoria"
}

LARGURA_ANALISE = {
    "nome": "1-bit",    "tamanho": 1,
    "nome": "8-bit",    "tamanho": 8,
    "nome": "64-bit",   "tamanho": 64,
    "nome": "128-bit",  "tamanho": 128
}

PASTA_INICIAL    = os.path.join(os.path.expanduser("~"), "Mestrado", "NC")
PASTA_LARGURA    = os.path.join(PASTA_INICIAL, "{largura}")
PASTA_ALGORITMO  = os.path.join(PASTA_LARGURA, "{algoritmo}")
PASTA_COMPUTADOR = os.path.join(PASTA_ALGORITMO, "{computador}")
PASTA_PRINCIPAL  = PASTA_COMPUTADOR