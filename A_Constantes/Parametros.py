SUB_EXPERIMENTOS = 4

# ==================================================
# ------------- TOPOLOGIAS -------------------------
# ==================================================

ALGORITMO_TOPOLOGIA = {
    "DES": [64, 128, 256, 384, 512],
    "AES": [128, 256, 384, 512],
    "SEM": [64, 128, 256, 384, 512],
    "ALE": [64, 128, 256, 384, 512]
}

TOPOLOGIAS = [
        {"nome": "S1", "tamanhos":[128, 256, 384, 512], "camadas": [2], "fator": [4]}, 

        {"nome": "D1", "tamanhos":[128, 256, 384, 512], "camadas": [10], "fator": [1]},
        {"nome": "D2", "tamanhos":[128, 256, 384, 512], "camadas": [12], "fator": [1]},
        {"nome": "D3", "tamanhos":[128, 256, 384, 512], "camadas": [14], "fator": [1]},

        {"nome": "MB", "tamanhos":[256, 384, 512], "camadas": [2, 3, 4], "fator": [[1, 2], [1, 2, 3], [1, 2, 3, 4]]},
    ]

NOME_CAMADAS = ["{indice}{letra}-{neuronios}", "Saida_{neuronios}"]

BLOCOS = [
        {"qtde": 1, "tam": 128, "estrutura": "A"   },
        {"qtde": 2, "tam": 256, "estrutura": "AB"  },
        {"qtde": 3, "tam": 384, "estrutura": "ABC" },
        {"qtde": 4, "tam": 512, "estrutura": "ABCD"}
    ]

# ==================================================
# ------------ EXPERIMENTOS ------------------------
# ==================================================
HIPER_PARAMETROS = {
    "estado"      : ["N", "E", "F"],
    "nome_exp"    : ["EXP_{blocos}_{modo}_{tipo_exp}_{base}{chave}_{topologia}_{indice}"],
    "modos"       : ["ECB", "CBC", "CFB", "OFB", "CTR"],
    "tipo_exp"    : ["MC"],
    "chaves"      : ["A", "B", "C"],
    
    "funcoes"     : ["S70", "S80"],
    "pesos"       : ["ZEROS", "VS-TN-FO-0.01"],
    
    "epocas"      : ["E-100"],
    "batch"       : ["B-32"],
    "otimizador"  : ["SGD-T-0.1-0.25"],
    "perda"       : ["mse"]
}

# ==================================================
# -------------- EXECUÇÕES -------------------------
# ==================================================
QUANT_PALAVRAS = 10
# AMBIENTE_EXEC = {
#     "tr":     "Treinamento", 
#     "val":    "Validacao",
#     "tr-val": "Treinamento e Validacao"
# }

AMBIENTE_EXEC = [
    {
        "sigla": "tr",
        "nome":  "Treinamento",
        "cor":   ["blue"],
        "label": ["Treinamento"],
        "sinal": ["."]
    },

    {
        "sigla": "val",
        "nome":  "Validação",
        "cor":   ["red"],
        "label": ['Validação'],
        "sinal": ["x"]
    },

    {
        "sigla": "tr-val",
        "nome":  "Treinamento e Validação",
        "cor":   ["blue", "red"],
        "label": ["Treinamento","Validação"],
        "sinal": [".", "x"]
    }
]

#NOME_SUBEXPERIMENTO = "EXP_{blocos}_{modo}_{tipo_exp}_{base}{chave}_{topologia}_{indice}_[V{subexp}]"
NOME_EXPERIMENTO    = "EXP_{computador}_{topologia}_{indice}" 
NOME_SUBEXPERIMENTO = "EXP_{computador}_{topologia}_{indice}_[V{subexp}]"
#EXP_COMP5_D1_1_[V1]

SUB_PASTAS_EXECUCOES = {
    "pe-{ind}":      "{topologia}/{exp}/{variacao}/Pos-Execucao",
    "pe_met-{ind}":  "{topologia}/{exp}/{variacao}/Pos-Execucao/{metricas}", 
    
    "te-{ind}":      "{topologia}/{exp}/{variacao}/Testes",
    "te_100-{ind}":  "{topologia}/{exp}/{variacao}/Testes/100 Palavras",
    "te_10":         "{topologia}/{exp}/{variacao}/Testes/10 Palavras", 
    "te_10-{ind}":   "{topologia}/{exp}/{variacao}/Testes/10 Palavras/Palavra {indice}", 
    "te_neur-{ind}": "{topologia}/{exp}/{variacao}/Testes/Neuronios",

    "top":           "{topologia}/{exp}/{variacao}/Topologia",
    "top_exp-{ind}": "{topologia}/{exp}/{variacao}/Topologia/Experimento",
    "top_mod":       "{topologia}/{exp}/{variacao}/Topologia/Modelo"
}

INDICE_METRICAS = "pe_[{met}]_{amb}"
INDICE_PALAVRAS = "te_10_{palavra}-{i}"

ARQUIVOS_EXECUCOES = {
    "top_exp-1":    "{nomeexp} - Mapa Topologico.jpg",

    "pe-1":         "{nomeexp} - Resultados (Metricas e Perdas).json",
    "pe-2":         "{nomeexp} - Resultados (Pesos).json",
    "pe_met-1":     "{nomeexp} - {metricas} - ({ambiente}).png",

    "te-1":         "{nomeexp} - Testes (Distribuicao Normal - Bins).csv",
    "te-2":         "{nomeexp} - Testes (Distribuicao Normal - Counts).csv",
    "te-3":         "{nomeexp} - Testes (Distribuicao Normal - Funcao).csv",
    "te-4":         "{nomeexp} - Testes (Distribuicao Normal).png",
    "te-5":         "{nomeexp} - Testes (Metricas).json",

    "te_100-1":     "{nomeexp} - Testes (100 palavras - Acerto e Erro).png",
    "te_100-2":     "{nomeexp} - Testes (100 palavras - Estatisticas).txt",
    "te_100-3":     "{nomeexp} - Testes (100 palavras - Metricas).csv",
    "te_100-4":     "{nomeexp} - Testes (100 palavras - Metricas).json",
    "te_100-5":     "{nomeexp} - Testes (100 palavras - Predito).csv",
    "te_100-6":     "{nomeexp} - Testes (100 palavras - Verdade).csv",

    "te_10-1":      "{nomeexp} - Testes (Palavra {indice} - Comparacao).csv",
    "te_10-2":      "{nomeexp} - Testes (Palavra {indice} - Confusao).csv",
    "te_10-3":      "{nomeexp} - Testes (Palavra {indice} - Confusao [Porcentagem]).csv",
    "te_10-4":      "{nomeexp} - Testes (Palavra {indice}).txt",
    "te_10-5":      "{nomeexp} - Testes (Palavra {indice} - Valores de saida).png",

    "te_neur-1":    "{nomeexp} - Testes (Neuronios - Correlacao).csv",
    "te_neur-2":    "{nomeexp} - Testes (Neuronios - Correlacao entre neuronios).png",
    "te_neur-3":    "{nomeexp} - Testes (Neuronios - Correlacao os 31 primeiros neuronios).png",
    "te_neur-4":    "{nomeexp} - Testes (Neuronios - Minimo e Maximo).txt",
    "te_neur-5":    "{nomeexp} - Testes (Neuronios - Palavras Acertadas).png",
    "te_neur-6":    "{nomeexp} - Testes (Neuronios - Palavras Acertadas).csv"
}

TITULO_METRICA = "{met} - ({ambiente})"

METRICAS = [
    ["Loss",                            "loss",                           "Perdas (%)",         "",                      {}],
    ["Binary Accuracy",                 "binary_accuracy",                "Acertos (%)",        "BinaryAccuracy",        {"threshold": 0.499999999}],
    ["Binary Cross Entropy",            "binary_crossentropy",            "Perdas (%)" ,        "BinaryCrossentropy",    {"label_smoothing": 0.499999999}],
    ["Precision",                       "precision",                      "Acertos (%)",        "Precision",             {}],
    ["Recall",                          "recall",                         "Acertos (%)",        "Recall",                {}],
    ["True Positives",                  "true_positive",                  "Quantidade de bits", "TruePositives",         {"thresholds": 0.499999999}],
    ["True Negatives",                  "true_negative",                  "Quantidade de bits", "TrueNegatives",         {"thresholds": 0.499999999}],
    ["False Positives",                 "false_positive",                 "Quantidade de bits", "FalsePositives",        {"thresholds": 0.499999999}],
    ["False Negatives",                 "false_negative",                 "Quantidade de bits", "FalseNegatives",        {"thresholds": 0.499999999}],
    ["Precision At Recall",             "precision_at_recall",            "Quantidade de bits", "PrecisionAtRecall",     {"recall": 0.499999999}],
    ["Recall At Precision",             "recall_at_precision",            "Quantidade de bits", "RecallAtPrecision",     {"precision": 0.499999999}],
    ["Sensitivity At Specificity",      "sensitivity_at_specificity",     "Quantidade de bits", "SensitivityAtSpecificity", {"specificity": 0.499999999}],
    ["Specificity At Sensitivity",      "specificity_at_sensitivity",     "Quantidade de bits", "SpecificityAtSensitivity", {"sensitivity": 0.499999999}],
    ["Cosine Similarity",               "cosine_similarity",              "Valores",            "CosineSimilarity",      {}],
    ["Poisson",                         "poisson",                        "Erros (%)",          "Poisson",               {}]
]

LIMIAR      = 0.49999999
LIMIAR_BCE  = 0.49999999
VALIDATION  = 0.25