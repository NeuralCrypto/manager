import os
ALGORITMOS = [
    {"sigla": "AES", "nome": "AES"},
    {"sigla": "DES", "nome": "DES"},
    {"sigla": "SEM", "nome": "Original"},
    {"sigla": "ALE", "nome": "Aleatoria"}
]

LARGURA_ANALISE = [
    {"nome": "1-bit",    "tamanho": 1},
    {"nome": "8-bit",    "tamanho": 8},
    {"nome": "32-bit",   "tamanho": 32},
    {"nome": "64-bit",   "tamanho": 64},
    {"nome": "128-bit",  "tamanho": 128}
]

PASTA_INICIAL    = os.path.join(os.path.expanduser("~"), "Mestrado", "NC")

# PASTAS PARA LARGURA DE BITS, CRIPTOGRAFIA, E COMPUTADORES -----
PASTA_LARGURA    = os.path.join(PASTA_INICIAL, "{largura}")
PASTA_ALGORITMO  = os.path.join(PASTA_LARGURA, "{algoritmo}")
PASTA_COMPUTADOR = os.path.join(PASTA_ALGORITMO, "{computador}")
PASTA_PRINCIPAL  = PASTA_COMPUTADOR

# SUB_PASTAS DENTRO DE CADA COMPUTADOR --------------------------
PASTA_BASE          = os.path.join(PASTA_PRINCIPAL, "Base")
PASTA_BASE_CONJ     = os.path.join(PASTA_BASE, "Conjuntos")
PASTA_CONJ_MODO     = os.path.join(PASTA_BASE_CONJ, "{modo}")
PASTA_BASE_TIPO     = os.path.join(PASTA_BASE, "MC")
PASTA_BASE_MODO     = os.path.join(PASTA_BASE_TIPO, "{modo}")
PASTA_BASE_TAM      = os.path.join(PASTA_BASE_MODO, "{base}")
PASTA_BASE_CHAVE    = os.path.join(PASTA_BASE_TAM, "{chave}")

PASTA_CODIGO        = os.path.join(PASTA_PRINCIPAL, "Codigo")

PASTA_RESULTADOS    = os.path.join(PASTA_PRINCIPAL, "Resultados")
PASTA_RESULT_TOPO   = os.path.join(PASTA_RESULTADOS, "{topologia}")
PASTA_RESULT_EXP    = os.path.join(PASTA_RESULT_TOPO, "{experimento}")
PASTA_RESULT_SUB    = os.path.join(PASTA_RESULT_EXP, "{sub}")

PASTA_EXPERIMENTOS  = os.path.join(PASTA_PRINCIPAL, "Experimentos")
PASTA_EXP_CSV       = os.path.join(PASTA_EXPERIMENTOS, "CSV")
PASTA_EXP_JSON      = os.path.join(PASTA_EXPERIMENTOS, "JSON")

# PASTA ORIGINAL DE DATASETS ------------------------------------
PASTA_DATASETS = os.path.join(PASTA_INICIAL, "Datasets")
PASTA_DATA_ANO = os.path.join(PASTA_DATASETS, "{ano}")
PASTA_DATA_MES = os.path.join(PASTA_DATA_ANO, "{mes}")
PASTA_DATA_DIA = os.path.join(PASTA_DATA_MES, "{dia}")

PASTAS_JSON = {
    "{largura}": {
        "{algoritmo}": {
            "{computador}": {
                "Base":{
                    "Conjuntos":{
                        "{modo}":[]
                    },
                    "MC":{
                        "{modo}":{
                            "{base}":{
                                "{chave}":[]
                            }
                        }
                    }
                },
                "Codigo":[],
                "Resultados":[],
                "Experimentos":{
                    "CSV": [],
                    "JSON": []
                }
            }
        }
    }
}

