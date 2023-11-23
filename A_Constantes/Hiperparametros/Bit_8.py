TAMANHO_LARGURA = 8

CHAVES_DES = ["A"]
CHAVES_AES = ["A", "B", "C"]
CHAVES_SEM = ["Z"]
CHAVES_ALE = ["Z"]

ALGORITMO_CHAVES = {
    "DES":CHAVES_DES,
    "AES":CHAVES_AES,
    "SEM":CHAVES_SEM,
    "ALE":CHAVES_ALE
}

#Quantidade de neurônios de entrada: [64, 128, 256, 384, 512]
MIN_BLOCO_DES = int(64/TAMANHO_LARGURA)
MIN_BLOCO_AES = int(128/TAMANHO_LARGURA)

TAMANHOS_NEUR_DES = [int(64*1/TAMANHO_LARGURA), int(64*2/TAMANHO_LARGURA), int(64*4/TAMANHO_LARGURA), int(64*6/TAMANHO_LARGURA), int(64*8/TAMANHO_LARGURA)]
TAMANHOS_NEUR_AES = [int(128*i/TAMANHO_LARGURA) for i in range(1, 5)]

TAMANHOS_NEUR_DES_MB = [int(64*2/TAMANHO_LARGURA), int(64*4/TAMANHO_LARGURA), int(64*6/TAMANHO_LARGURA), int(64*8/TAMANHO_LARGURA)]
TAMANHOS_NEUR_AES_MB = [int(128*i/TAMANHO_LARGURA) for i in range(2, 5)]

CAMADAS_MB_DES    = [i for i in range(2, 9, 2)]
CAMADAS_MB_AES    = [2, 3, 4]

FUNCOES           = ["Q1.0", "A1.0"]


TOPO_DES = {
    "S1": {"tamanhos":TAMANHOS_NEUR_DES, "camadas": [2],  "fator": [1], "funcoes": FUNCOES},

    "D1": {"tamanhos":TAMANHOS_NEUR_DES, "camadas": [10], "fator": [1], "funcoes": ["Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "A1.0"]},
    "D2": {"tamanhos":TAMANHOS_NEUR_DES, "camadas": [12], "fator": [1], "funcoes": ["Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "A1.0"]},
    "D3": {"tamanhos":TAMANHOS_NEUR_DES, "camadas": [14], "fator": [1], "funcoes": ["Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "A1.0"]},

    "MB": {
        "tamanhos": TAMANHOS_NEUR_DES_MB, 
        "camadas":  CAMADAS_MB_DES, 
        "fator":    [[j*MIN_BLOCO_DES for j in range(1, i+1)] for i in CAMADAS_MB_DES], 
        "funcoes":  [[FUNCOES[0] if j != i else FUNCOES[1] for j in range(1, i+1)] for i in CAMADAS_MB_DES]
    }
}

TOPO_AES = {
    "S1": {"tamanhos":TAMANHOS_NEUR_AES, "camadas": [2],  "fator": [1], "funcoes": ["Q1.0", "A1.0"]},

    "D1": {"tamanhos":TAMANHOS_NEUR_AES, "camadas": [10], "fator": [1], "funcoes": ["Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "A1.0"]},
    "D2": {"tamanhos":TAMANHOS_NEUR_AES, "camadas": [12], "fator": [1], "funcoes": ["Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "A1.0"]},
    "D3": {"tamanhos":TAMANHOS_NEUR_AES, "camadas": [14], "fator": [1], "funcoes": ["Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "Q1.0", "A1.0"]},

    "MB":{
        "tamanhos": TAMANHOS_NEUR_AES_MB, 
        "camadas":  CAMADAS_MB_AES, 
        "fator":    [[j*MIN_BLOCO_AES for j in range(1, i+1)] for i in CAMADAS_MB_AES], 
        "funcoes":  [[FUNCOES[0] if j != i else FUNCOES[1] for j in range(1, i+1)] for i in CAMADAS_MB_AES]
    }
}

TOPO_SEM = TOPO_DES
TOPO_ALE = TOPO_DES

ALGORITMO_TOPOLOGIA = {
    "DES": TOPO_DES,
    "AES": TOPO_AES,
    "SEM": TOPO_SEM,
    "ALE": TOPO_ALE
}

NOME_CAMADAS = ["{indice}{letra}-{neuronios}", "Saida_{neuronios}"]

BLOCOS_AES = [
    {"qtde": 1, "tam": TAMANHOS_NEUR_AES[0], "estrutura": "A"   },
    {"qtde": 2, "tam": TAMANHOS_NEUR_AES[1], "estrutura": "AB"  },
    {"qtde": 3, "tam": TAMANHOS_NEUR_AES[2], "estrutura": "ABC" },
    {"qtde": 4, "tam": TAMANHOS_NEUR_AES[3], "estrutura": "ABCD"}
]

BLOCOS_DES = [
    {"qtde": 1, "tam": MIN_BLOCO_DES*1, "estrutura": "A"        },
    {"qtde": 2, "tam": MIN_BLOCO_DES*2, "estrutura": "AB"       },
    {"qtde": 3, "tam": MIN_BLOCO_DES*3, "estrutura": "ABC"      },
    {"qtde": 4, "tam": MIN_BLOCO_DES*4, "estrutura": "ABCD"     },
    {"qtde": 5, "tam": MIN_BLOCO_DES*5, "estrutura": "ABCDE"    },
    {"qtde": 6, "tam": MIN_BLOCO_DES*6, "estrutura": "ABCDEF"   },
    {"qtde": 7, "tam": MIN_BLOCO_DES*7, "estrutura": "ABCDEFG"  },
    {"qtde": 8, "tam": MIN_BLOCO_DES*8, "estrutura": "ABCDEFGH" }
]

BLOCOS_SEM = BLOCOS_DES
BLOCOS_ALE = BLOCOS_DES

ALGORITMO_BLOCOS = {
    "DES": BLOCOS_DES,
    "AES": BLOCOS_AES,
    "SEM": BLOCOS_SEM,
    "ALE": BLOCOS_ALE
}

HIPER_PARAMETROS = {
    "estado"      : ["N", "E", "F"],
    "nome_exp"    : ["EXP_{blocos}_{modo}_{tipo_exp}_{base}{chave}_{topologia}_{indice}"],
    "modos"       : ["ECB", "CBC", "CFB", "OFB", "CTR"],
    "tipo_exp"    : ["MC"],
    "chaves"      : ALGORITMO_CHAVES,

    "topologia"   : ALGORITMO_TOPOLOGIA,
    
    "pesos"       : ["ZEROS", "VS-TN-FO-0.01"],
    
    "epocas"      : ["E-100"],
    "batch"       : ["B-32"],
    "otimizador"  : ["SGD-T-0.1-0.25"],
    "perda"       : ["mse"]
}