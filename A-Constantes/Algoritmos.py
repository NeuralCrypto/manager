TIPOS_ALGORITMOS = ["AES", "DES", "SEM", "INV"]

TIPO_AES = {
    "tam_bloco": [128],
    "tam_chave": [128, 192, 256],
    "tam_round": [10, 12, 14],
    "chave_round": {
        "128": 10,
        "192": 12,
        "256": 14
    }
}

TIPO_DES = {
    "tam_bloco": [64],
    "tam_chave": [56],
    "tam_round": [16]
}

TIPO_SEM_1 = {
    "tam_bloco_DES": [64,  128, 192, 256],
    "tam_bloco_AES": [128, 256, 384, 512]
}

TIPO_SEM_8 = {
    "tam_bloco_DES": [8,  16, 24, 32],
    "tam_bloco_AES": [16, 32, 48, 64]
}