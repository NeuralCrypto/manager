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
# PASTA BASE DE DADOS____________________________________________
PASTA_BASE          = os.path.join(PASTA_PRINCIPAL, "Base")

PASTA_BASE_DADOS    = os.path.join(PASTA_BASE, "A-Dados")
PASTA_DADOS_TIPO    = os.path.join(PASTA_BASE_DADOS, "MC")
PASTA_DADOS_MODO    = os.path.join(PASTA_DADOS_TIPO, "{modo}")
PASTA_DADOS_TAM     = os.path.join(PASTA_DADOS_MODO, "{base}")
PASTA_DADOS_CHAVE   = os.path.join(PASTA_DADOS_TAM, "{chave}")

PASTA_BASE_DATASETS = os.path.join(PASTA_BASE, "B-Datasets")
PASTA_BASE_ANO      = os.path.join(PASTA_BASE_DATASETS, "{ano}")
PASTA_BASE_MES      = os.path.join(PASTA_BASE_ANO, "{mes}")

PASTA_BASE_CONJ     = os.path.join(PASTA_BASE, "C-Conjuntos")
#PASTA_CONJ_MODO    = os.path.join(PASTA_BASE_CONJ, "{modo}")

PASTA_BASE_CHAVES   = os.path.join(PASTA_BASE, "D-Chaves")

# PASTA CODIGO___________________________________________________
PASTA_CODIGO        = os.path.join(PASTA_PRINCIPAL, "Codigo")

# PASTA RESULTADOS_______________________________________________
PASTA_RESULTADOS    = os.path.join(PASTA_PRINCIPAL, "Resultados")
PASTA_RESULT_TOPO   = os.path.join(PASTA_RESULTADOS, "{topologia}")
PASTA_RESULT_EXP    = os.path.join(PASTA_RESULT_TOPO, "{experimento}")
PASTA_RESULT_SUB    = os.path.join(PASTA_RESULT_EXP, "{sub}")

# PASTA EXPERIMENTOS______________________________________________
PASTA_EXPERIMENTOS  = os.path.join(PASTA_PRINCIPAL, "Experimentos")
PASTA_EXP_CSV       = os.path.join(PASTA_EXPERIMENTOS, "CSV")
PASTA_EXP_JSON      = os.path.join(PASTA_EXPERIMENTOS, "JSON")

# PASTA ORIGINAL DE DATASETS ------------------------------------
PASTA_DATASETS = os.path.join(PASTA_INICIAL, "A-Utils/Datasets")
PASTA_DATA_ANO = os.path.join(PASTA_DATASETS, "{ano}")
PASTA_DATA_MES = os.path.join(PASTA_DATA_ANO, "{mes}")
#PASTA_DATA_DIA = os.path.join(PASTA_DATA_MES, "{dia}")

# PASTA CONJUNTOS DE ARQUIVOS DE MENSAGENS ----------------------
PASTA_CONJUNTO = os.path.join(PASTA_INICIAL, "A-Utils/Conjuntos")

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

