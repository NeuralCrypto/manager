TIPOS_ALGORITMOS = ["AES", "DES", "SEM", "INV"]

TIPO_AES = {
    "tam_bloco": [128],
    "tam_chave": [128, 192, 256],
    "tam_round": [10, 12, 14],
    "chave_round": {
        "128": 10,
        "192": 12,
        "256": 14
    },
    "tam_IV": [128],
    "tam_nonce":[64],
    "prefixo": {"A": 128,   "B": 192,   "C": 256}
}

TIPO_DES = {
    "tam_bloco": [64],
    "tam_chave": [64],
    "tam_round": [16],
    "tam_IV":    [64],
    "tam_nonce": [64],
    "prefixo": {"A": 64}
}

ALGO_CHAVE_PREFIX = {
    "DES": {"A": 64},
    "AES": {"A": 128,   "B": 192,   "C": 256},
    "SEM": {"Z": 0},
    "ALE": {"Z": 0}
}

TAM_MSGS_B = {
    "64":  int(64/8),
    "128": int(128/8),
    "192": int(192/8),
    "256": int(192/8),
    "384": int(192/8),
    "512": int(192/8)
}

# TIPO_SEM_1 = {
#     "tam_bloco_DES": [64,  128, 192, 256],
#     "tam_bloco_AES": [128, 256, 384, 512]
# }

# TIPO_SEM_8 = {
#     "tam_bloco_DES": [int(64/8),  int(128/8), int(192/8), int(256/8)],
#     "tam_bloco_AES": [int(128/8), int(256/8), int(384/8), int(512/8)]
# }

# TIPO_SEM_8 = {
#     "tam_bloco_DES": [8,  16, 24, 32],
#     "tam_bloco_AES": [16, 32, 48, 64]
# }

# TIPO_SEM_32 = {
#     "tam_bloco_DES": [2,  16, 24, 32],
#     "tam_bloco_AES": [16, 32, 48, 64]
# }

# TIPO_SEM_64 = {
#     "tam_bloco_DES": [1,  16, 24, 32],
#     "tam_bloco_AES": [16, 32, 48, 64]
# }

# TIPO_SEM_128 = {
#     "tam_bloco_DES": [0,  16, 24, 32],
#     "tam_bloco_AES": [16, 32, 48, 64]
# }

MODOS_OPERACAO = ["ECB", "CBC", "CFB", "OFB", "CTR"]
MODOS_IV = {
    "ECB": "N", 
    "CBC": "S", 
    "OFB": "S", 
    "CFB": "S", 
    "CTR": "S"
}

ALGORITMOS_MODOS = {
    "AES": ["ECB", "CBC", "CFB", "OFB", "CTR"],
    "DES": ["ECB", "CBC", "CFB", "OFB", "CTR"],
    "SEM": [],
    "INV": []
}