import json
import os
import shutil
from A_Constantes.Algoritmos    import ALGORITMOS_IV
from A_Constantes.Arquivos      import ARQ_CONJ, ARQ_CONJUNTOS, ARQ_NOME_DATA
from A_Constantes.Computadores  import COMPUTADORES

from A_Constantes.Pastas    import LARGURA_ANALISE, PASTA_BASE_CONJ, PASTA_BASE_MES, PASTA_CONJUNTO, ALGORITMOS, PASTA_DATA_MES
from A_Constantes.Tamanhos  import MAX_ARQUIVOS_IV, MAX_ARQUIVOS_MSG, SUB_EXPERIMENTOS, TAM_BASE_PREFIX, TAMANHO_ARQUIVO

import random

class Conjunto:

    def __init__(self):
        pass

    def __ler_arquivos(self):
        endereco = os.path.join(".", "A_Constantes", "Datasets.json")
        with open(endereco, "r") as arquivo:
            dados = json.load(arquivo)
        return dados

    def gerar(self):
        
        dados = {}
        datasets = self.__ler_arquivos()

        conta = 0
        
        for i in range(1, (SUB_EXPERIMENTOS+1)):
            dados[i]  = {}
            dados[i]["Tr"] = {}
            dados[i]["Te"] = {}
            dados[i]["Tr_IV"] = {}
            dados[i]["Te_IV"] = {}


            for j in range(0, (MAX_ARQUIVOS_MSG+1)):
                dados[i]["Tr"][j] = random.choice(datasets)
                dados[i]["Te"][j] = random.choice(datasets)
                conta = conta + 1

            for j in range(0, (MAX_ARQUIVOS_IV+1)):
                dados[i]["Tr_IV"][j] = random.choice(datasets)
                dados[i]["Te_IV"][j] = random.choice(datasets)
                conta = conta + 1
        
        end_totais = os.path.join(PASTA_CONJUNTO, ARQ_CONJUNTOS)
        arq_totais = open(end_totais, "w")
        json.dump(dados, arq_totais)
        arq_totais.close()

    def distribuir(self):

        self.gerar()

        end_totais = os.path.join(PASTA_CONJUNTO, ARQ_CONJUNTOS)
        with open(end_totais, "r") as arquivo:
            datasets_totais = json.load(arquivo)

        for l in LARGURA_ANALISE:
            for a in ALGORITMOS:                
                for c in COMPUTADORES:
                    if c["modos"][a["sigla"]]:
                        for b in c["bases"]:

                            dados = {}

                            qtde_arquivos_msg = int((TAM_BASE_PREFIX[b] * c["blocos"]) / TAMANHO_ARQUIVO)
                            qtde_arquivos_iv  = int((TAM_BASE_PREFIX[b] * ALGORITMOS_IV[a["sigla"]]) / TAMANHO_ARQUIVO)

                            for i_int in range(1, (SUB_EXPERIMENTOS+1)):
                                i = str(i_int)
                                dados[i]  = {}
                                dados[i]["Tr"] = {}
                                dados[i]["Te"] = {}
                                dados[i]["Tr_IV"] = {}
                                dados[i]["Te_IV"] = {}

                                for j_int in range(0, (qtde_arquivos_msg+1)):
                                    j = str(j_int)
                                    dados[i]["Tr"][j] = datasets_totais[i]["Tr"][j]
                                    dados[i]["Te"][j] = datasets_totais[i]["Te"][j]
                                    

                                for j_int in range(0, (qtde_arquivos_iv+1)):
                                    j = str(j_int)
                                    dados[i]["Tr_IV"][j] = datasets_totais[i]["Tr_IV"][j]
                                    dados[i]["Te_IV"][j] = datasets_totais[i]["Te_IV"][j]
                            
                            endereco = os.path.join(PASTA_BASE_CONJ, ARQ_CONJ)
                            endereco = endereco.format(
                                largura=l["nome"],
                                algoritmo=a["sigla"],
                                computador=c["nome"],
                                tamanho=c["blocos"],
                                base=b
                            )
                            arquivo = open(endereco, "w")
                            json.dump(dados, arquivo)
                            arquivo.close()

    def copiar(self):
        """
        Copia os arquivos .bin (datasets) para os computadores.
        """
        for l in LARGURA_ANALISE:
            for a in ALGORITMOS:                
                for c in COMPUTADORES:
                    for b in c["bases"]:
                        if c["modos"][a["sigla"]]:
                            
                            # Abrir os arquivos de datasets
                            endereco = os.path.join(PASTA_BASE_CONJ, ARQ_CONJ)
                            endereco = endereco.format(
                                largura=l["nome"],
                                algoritmo=a["sigla"],
                                computador=c["nome"],
                                tamanho=c["blocos"],
                                base=b
                            )
                            with open(endereco, "r") as arquivo:
                                dados = json.load(arquivo)
                            
                            for sub_exp in dados:
                                for ambiente in dados[sub_exp]:
                                    for id in dados[sub_exp][ambiente]:
                                        nome_arq = dados[sub_exp][ambiente][id]
                                        ano = nome_arq["ano"]
                                        mes = nome_arq["mes"]
                                        dia = nome_arq["dia"]

                                        end_pasta = PASTA_BASE_MES.format(
                                            largura=l["nome"],
                                            algoritmo=a["sigla"],
                                            computador=c["nome"],
                                            ano=ano,
                                            mes=mes
                                        )

                                        try:
                                            os.makedirs(end_pasta)
                                        except:
                                            continue
                                        
                                        end_origem = os.path.join(PASTA_DATA_MES, ARQ_NOME_DATA)
                                        end_origem = end_origem.format(
                                            largura=l["nome"],
                                            algoritmo=a["sigla"],
                                            computador=c["nome"],
                                            ano=ano,
                                            mes=mes,
                                            dia=dia
                                        )

                                        end_destino = os.path.join(PASTA_BASE_MES, ARQ_NOME_DATA)
                                        end_destino = end_destino.format(
                                            largura=l["nome"],
                                            algoritmo=a["sigla"],
                                            computador=c["nome"],
                                            ano=ano,
                                            mes=mes,
                                            dia=dia
                                        )

                                        shutil.copyfile(end_origem, end_destino)