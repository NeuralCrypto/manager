import os
from A_Constantes.Arquivos import ARQ_EXP_COMUM
from Experimentos.Arquivos.CSV  import CSV
from Experimentos.Arquivos.JSON import JSON

class Arquivos:

    def __init__(self, largura, algoritmo, computador, topologia):
        self.csv    = CSV()
        self.json   = JSON()

        self.arq_csv  = None
        self.arq_json = None
        
        self.dados_csv  = []
        self.dados_json = []

        self.arq_csv, self.arq_json = self.criar(largura, algoritmo, computador, topologia)

    def __nomear(self, largura, algoritmo, computador, topologia):
        """
        Nomeia-se o arquivo de experimentos a ser criado.
        Parâmetros:
        * topologia:  É a topologia da rede neural em questão;
        * computador: É o nome do computador onde executará os experimentos.
        """

        end_csv  = self.csv.nomear(largura, algoritmo, computador, topologia)
        end_json = self.json.nomear(largura, algoritmo, computador, topologia)
        return end_csv, end_json


    def criar(self, largura, algoritmo, computador, topologia):
        """
        Verifica-se se o arquivo existe. Caso não exista, deve-se criar.
        """
        end_csv, end_json = self.__nomear(largura, algoritmo, computador, topologia)

        arq_csv  = self.csv.criar(end_csv)
        arq_json = self.json.criar(end_json)
        
        return arq_csv, arq_json

    def adicionar(self, indice="", estado="", computador="", nome_exp="", tam_blocos="", modo="", tipo_exp="", tam_base="", tam_chave="", topologia="", camadas="", epocas="", batch="", otimizador="", perda=""):
        dados_json = self.json.adicionar(indice, estado, computador, nome_exp, tam_blocos, modo, tipo_exp, tam_base, tam_chave, topologia, camadas, epocas, batch, otimizador, perda)
        self.dados_json.append(dados_json)
        dados_csv = self.csv.adicionar(dados_json)
        self.dados_csv = self.dados_csv + dados_csv

    def __escrever(self):
        self.json.escrever(self.dados_json)
        self.csv.escrever(self.dados_csv)
        #self.csv.escrever(indice, estado, computador, nome_exp, tam_blocos, modo, tipo_exp, tam_base, tam_chave, topologia, camadas, epocas, batch, otimizador, perda)

    def __limpar(self):
        self.dados_csv  = None
        self.dados_json = None
    
    def fechar(self):
        self.__escrever()
        self.__limpar()
        pass