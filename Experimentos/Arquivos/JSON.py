import os
import json

from A_Constantes.Arquivos import ARQ_EXP_JSON
from A_Constantes.Pastas import PASTA_EXP_JSON

class JSON:
    
    def __init__(self):
        pass

    def nomear(self, largura, algoritmo, computador, topologia):
        """
        Nomeia-se o arquivo de experimentos a ser criado.
        Parâmetros:
        * topologia:  É a topologia da rede neural em questão;
        * computador: É o nome do computador onde executará os experimentos.
        """
        endereco = os.path.join(PASTA_EXP_JSON, ARQ_EXP_JSON)
        arquivo  = endereco.format(
            estado      = "N",
            largura     = largura,
            algoritmo   = algoritmo,
            topologia   = topologia,
            computador  = computador
        )
        return arquivo

    def criar(self, nome):
        """
        Verifica-se se o arquivo existe. Caso não exista, deve-se criar.
        """
        self.arquivo = None
        #if not os.path.exists(nome):
        #    arquivo = open(nome, "a")
        self.arquivo = open(nome, "w")
        
        return self.arquivo
    
    def adicionar(self, indice="", estado="", computador="", nome_exp="", tam_blocos="", modo="", tipo_exp="", tam_base="", tam_chave="", topologia="", camadas="", epocas="", batch="", otimizador="", perda=""):
        
        argumentos = locals()
        del argumentos['self']
        experimento = {}
        for k, v in argumentos.items():
            experimento[k.upper()] = argumentos[k]
        return experimento
        
    def escrever(self, experimento):
        json.dump(experimento, self.arquivo)