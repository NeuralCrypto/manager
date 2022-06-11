from Experimentos.Arquivos.CSV  import CSV
from Experimentos.Arquivos.JSON import JSON

class Camadas:
    
    def __init__(self, nomes_modelo, topologias, blocos):
        self.nomes_modelo = nomes_modelo
        self.topologias   = topologias
        self.blocos       = blocos

    def escolher(self, topologia, tam_bloco, peso):
        
        if topologia == "S1":
            rede = self.S1
        
        elif topologia == "D1":
            rede = self.D1
        
        elif topologia == "D2":
            rede = self.D2
        
        elif topologia == "D3":
            rede = self.D3
        
        elif topologia == "MB":
            rede = self.MB
        
        dados = rede(tam_bloco, peso)
        return dados

    def S1(self, tam_bloco, peso):
        
        camadas = {}
        topologia = self.topologias["S1"]

        for c in range(1, topologia["camadas"][0]):
            
            nome_camada = self.nomes_modelo[0].format(
                indice      = c,
                letra       = next(item for item in self.blocos if item["tam"] == tam_bloco)["estrutura"],
                neuronios   = tam_bloco * topologia["fator"][0]
            )

            funcao = topologia["funcoes"][c-1]

            camadas[c] = {}
            camadas[c]['CA_NOME']    = nome_camada
            camadas[c]["CA_FUNCOES"] = funcao
            camadas[c]["CA_BIAS"]    = peso
            camadas[c]["CA_KERNEL"]  = peso
        
        c = topologia["camadas"][0]-1
        
        nome_camada = self.nomes_modelo[1].format(
            indice      = c,
            neuronios   = tam_bloco
        )

        funcao = topologia["funcoes"][c]

        camadas[c+1] = {}
        camadas[c+1]['CA_NOME']    = nome_camada
        camadas[c+1]["CA_FUNCOES"] = funcao
        camadas[c+1]["CA_BIAS"]    = peso
        camadas[c+1]["CA_KERNEL"]  = peso

        return camadas
    
    def D1(self, tam_bloco, peso):
        
        camadas = {}
        topologia = self.topologias["D1"]
        
        for c in range(1, topologia["camadas"][0]):
            
            nome_camada = self.nomes_modelo[0].format(
                indice      = c,
                letra       = next(item for item in self.blocos if item["tam"] == tam_bloco)["estrutura"],
                neuronios   = tam_bloco * topologia["fator"][0]
            )

            funcao = topologia["funcoes"][c-1]

            camadas[c] = {}
            camadas[c]['CA_NOME']    = nome_camada
            camadas[c]["CA_FUNCOES"] = funcao
            camadas[c]["CA_BIAS"]    = peso
            camadas[c]["CA_KERNEL"]  = peso
        
        c = topologia["camadas"][0]-1

        nome_camada = self.nomes_modelo[1].format(
            indice      = c,
            neuronios   = tam_bloco
        )

        funcao = topologia["funcoes"][c]

        camadas[c+1] = {}
        camadas[c+1]['CA_NOME']    = nome_camada
        camadas[c+1]["CA_FUNCOES"] = funcao
        camadas[c+1]["CA_BIAS"]    = peso
        camadas[c+1]["CA_KERNEL"]  = peso

        return camadas

    def D2(self, tam_bloco, peso):
        
        camadas = {}
        topologia = self.topologias["D2"]
        
        for c in range(1, topologia["camadas"][0]):
            
            nome_camada = self.nomes_modelo[0].format(
                indice      = c,
                letra       = next(item for item in self.blocos if item["tam"] == tam_bloco)["estrutura"],
                neuronios   = tam_bloco * topologia["fator"][0]
            )

            funcao = topologia["funcoes"][c-1]

            camadas[c] = {}
            camadas[c]['CA_NOME']    = nome_camada
            camadas[c]["CA_FUNCOES"] = funcao
            camadas[c]["CA_BIAS"]    = peso
            camadas[c]["CA_KERNEL"]  = peso
        
        c = topologia["camadas"][0]-1

        nome_camada = self.nomes_modelo[1].format(
            indice      = c,
            neuronios   = tam_bloco
        )

        funcao = topologia["funcoes"][c]

        camadas[c+1] = {}
        camadas[c+1]['CA_NOME']    = nome_camada
        camadas[c+1]["CA_FUNCOES"] = funcao
        camadas[c+1]["CA_BIAS"]    = peso
        camadas[c+1]["CA_KERNEL"]  = peso

        return camadas

    def D3(self, tam_bloco, peso):
        
        camadas = {}
        topologia = self.topologias["D3"]
        
        for c in range(1, topologia["camadas"][0]):
            
            nome_camada = self.nomes_modelo[0].format(
                indice      = c,
                letra       = next(item for item in self.blocos if item["tam"] == tam_bloco)["estrutura"],
                neuronios   = tam_bloco * topologia["fator"][0]
            )

            funcao = topologia["funcoes"][c-1]

            camadas[c] = {}
            camadas[c]['CA_NOME']    = nome_camada
            camadas[c]["CA_FUNCOES"] = funcao
            camadas[c]["CA_BIAS"]    = peso
            camadas[c]["CA_KERNEL"]  = peso
        
        c = topologia["camadas"][0]-1
        
        nome_camada = self.nomes_modelo[1].format(
            indice      = c,
            neuronios   = tam_bloco
        )

        funcao = topologia["funcoes"][c]

        camadas[c+1] = {}
        camadas[c+1]['CA_NOME']    = nome_camada
        camadas[c+1]["CA_FUNCOES"] = funcao
        camadas[c+1]["CA_BIAS"]    = peso
        camadas[c+1]["CA_KERNEL"]  = peso

        return camadas

    def MB(self, tam_bloco, peso):
        
        camadas     = {}
        topologia   = self.topologias["MB"]
        indice      = topologia["tamanhos"].index(tam_bloco)
        
        for c in range(1, topologia["camadas"][indice]):

            fator  = topologia["fator"][indice][c-1]
            letras = next(item for item in self.blocos if item["tam"] == fator)["estrutura"]
            nome_camada = self.nomes_modelo[0].format(
                indice      = c,
                letra       = letras,
                neuronios   = fator
            )
            funcao = topologia["funcoes"][indice][c-1]

            camadas[c] = {}
            camadas[c]['CA_NOME']    = nome_camada
            camadas[c]["CA_FUNCOES"] = funcao
            camadas[c]["CA_BIAS"]    = peso
            camadas[c]["CA_KERNEL"]  = peso
        
        c = topologia["camadas"][indice]

        nome_camada = self.nomes_modelo[1].format(
            indice      = c,
            neuronios   = tam_bloco
        )
        funcao = topologia["funcoes"][indice][c-1]

        camadas[c] = {}
        camadas[c]['CA_NOME']    = nome_camada
        camadas[c]["CA_FUNCOES"] = funcao
        camadas[c]["CA_BIAS"]    = peso
        camadas[c]["CA_KERNEL"]  = peso

        return camadas