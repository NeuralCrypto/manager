from A_Constantes.Hiperparametros.Bit_8 import *
from Experimentos.Arquivos.Arquivos     import Arquivos
from Experimentos.Camadas               import Camadas

class Bit_8:
    
    def __init__(self) -> None:
        self.largura      = 8
        self.nome_largura = "8-bit"

    def experimentar(self, algoritmo, computador):

        blocos      = int(computador["blocos"]/TAMANHO_LARGURA)                          # Tamanho do bloco
        estado      = HIPER_PARAMETROS["estado"     ][0]                                 # Estado de execução
        tipo_exp    = HIPER_PARAMETROS["tipo_exp"   ][0]                                 # Tipo de experimento (MC)
        epocas      = HIPER_PARAMETROS["epocas"     ][0]                                 # Quantidade de épocas
        batch       = HIPER_PARAMETROS["batch"      ][0]                                 # Quantidade de Batch
        otimizador  = HIPER_PARAMETROS["otimizador" ][0]                                 # Otimizador
        perda       = HIPER_PARAMETROS["perda"      ][0]                                 # Perda

        for topologia in HIPER_PARAMETROS["topologia"][algoritmo]:                       # Topologias
            
            if (topologia == "MB" and (blocos == MIN_BLOCO_AES and computador["nome"] in ["COMP0", "COMP1"] and algoritmo == "AES") or (blocos == MIN_BLOCO_DES  and computador["nome"] in ["COMP8", "COMP9"])):
                continue
            else:
                indice = 1
                arquivo = Arquivos(self.nome_largura, algoritmo, computador["nome"], topologia)

                for modo in computador["modos"][algoritmo]:                                  # Modos de operação
                    for base in computador["bases"]:                                         # Tamanho das bases
                        for peso in HIPER_PARAMETROS["pesos"]:                               # Pesos
                            for chave in HIPER_PARAMETROS["chaves"][algoritmo]:              # Tamanho das chaves

                                nome_exp      = HIPER_PARAMETROS["nome_exp"][0].format(         # Nome do experimento
                                    blocos    = blocos,
                                    modo      = modo,
                                    tipo_exp  = tipo_exp,
                                    base      = base,
                                    chave     = chave,
                                    topologia = topologia,
                                    indice    = indice
                                )

                                camadas   = Camadas(NOME_CAMADAS, HIPER_PARAMETROS["topologia"][algoritmo], ALGORITMO_BLOCOS[algoritmo])
                                cam_dados = camadas.escolher(topologia, blocos, peso)

                                arquivo.adicionar(
                                    indice      = indice,
                                    estado      = estado, 
                                    computador  = computador["nome"],
                                    nome_exp    = nome_exp,
                                    tam_blocos  = blocos,
                                    modo        = modo,
                                    tipo_exp    = tipo_exp,
                                    tam_base    = base,
                                    tam_chave   = chave,
                                    topologia   = topologia,
                                    camadas     = cam_dados, 
                                    epocas      = epocas, 
                                    batch       = batch, 
                                    otimizador  = otimizador, 
                                    perda       = perda
                                )

                                indice += 1
                arquivo.fechar()


