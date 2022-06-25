import os

from A_Constantes.Arquivos  import ARQ_EXP_CSV
from A_Constantes.Pastas    import PASTA_EXP_CSV

class CSV:

    CABECALHO   = "INDICE,ESTADO,COMPUTADOR,NOME_EXP,TAM_BLOCOS,MODO,TIPO_EXP,TAM_BASE,TAM_CHAVE,TOPOLOGIA,CA_NOME,CA_FUNCOES,CA_BIAS,CA_KERNEL,EPOCAS,BATCH,OTIMIZADOR,PERDA\n"
    LINHA       = "{indice},{estado},{computador},{nome_exp},{tam_blocos},{modo},{tipo_exp},{tam_base},{tam_chave},{topologia},{ca_nome},{ca_funcoes},{ca_bias},{ca_kernel},{epocas},{batch},{otimizador},{perda}\n"

    def __init__(self):
        self.arquivo = None
        pass

    def nomear(self, largura, algoritmo, computador, topologia):
        """
        Nomeia-se o arquivo de experimentos a ser criado.
        Parâmetros:
        * topologia:  É a topologia da rede neural em questão;
        * computador: É o nome do computador onde executará os experimentos.
        """
        endereco = os.path.join(PASTA_EXP_CSV, ARQ_EXP_CSV)
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

    def __corpo(self, indice="", estado="", computador="", nome_exp="", tam_blocos="", modo="", tipo_exp="", tam_base="", tam_chave="", topologia="", ca_nome="", ca_funcoes="", ca_bias="", ca_kernel="", epocas="", batch="", otimizador="", perda=""):
        row = self.LINHA.format(
            indice      = indice,
            estado      = estado, 
            computador  = computador,
            nome_exp    = nome_exp,
            tam_blocos  = tam_blocos,
            modo        = modo,
            tipo_exp    = tipo_exp,
            tam_base    = tam_base,
            tam_chave   = tam_chave,
            topologia   = topologia,
            ca_nome     = ca_nome, 
            ca_funcoes  = ca_funcoes, 
            ca_bias     = ca_bias, 
            ca_kernel   = ca_kernel, 
            epocas      = epocas, 
            batch       = batch, 
            otimizador  = otimizador, 
            perda       = perda
        )
        return row
    
    def adicionar(self, dados):
        
        experimento = {}
        linha       = []
        for indice in dados:
            if indice == "CAMADAS":
                for ind in dados[indice][1]:
                    experimento[ind.lower()] = dados[indice][1][ind]
            else:
               experimento[indice.lower()] = dados[indice]
        
        linha.append(self.__corpo(**experimento))

        for indice in experimento:
            experimento[indice] = ""
        
        for i in dados["CAMADAS"]:
            if i == 1:
                continue
            else:
                experimento["ca_nome"]      = dados["CAMADAS"][i]["CA_NOME"]
                experimento["ca_funcoes"]   = dados["CAMADAS"][i]["CA_FUNCOES"]
                experimento["ca_bias"]      = dados["CAMADAS"][i]["CA_BIAS"]
                experimento["ca_kernel"]    = dados["CAMADAS"][i]["CA_KERNEL"]
                linha.append(self.__corpo(**experimento))
                
        return linha
    
    def escrever(self, dados):

        self.arquivo.write(self.CABECALHO)
        for dado in dados:
            self.arquivo.write(dado)
