from A_Constantes.Pastas        import *
from A_Constantes.Computadores  import COMPUTADORES
from A_Constantes.Algoritmos    import *

class Pastas:

    def __init__(self):
        pass

    def gerar(self):

        for l in LARGURA_ANALISE:
            for a in ALGORITMOS:                
                for c in COMPUTADORES: 

                    if c["modos"][a["sigla"]]:
                        # Pasta Base - Conjuntos 
                        endereco = None
                        for modo in c["modos"][a["sigla"]]:
                            endereco = PASTA_CONJ_MODO.format(
                                largura=l["nome"],
                                algoritmo=a["sigla"],
                                computador=c["nome"],
                                modo=modo
                            )
                            os.makedirs(endereco)
                        
                        # Pasta Base - Dados
                        endereco = None
                        for modo in c["modos"][a["sigla"]]:
                            for base in c["bases"]:
                                for chave in ALGO_CHAVE_PREFIX[a["sigla"]]:
                                    endereco = PASTA_BASE_CHAVE.format(
                                        largura=l["nome"],
                                        algoritmo=a["sigla"],
                                        computador=c["nome"],
                                        modo=modo, 
                                        base=base, 
                                        chave=chave
                                    )
                                    os.makedirs(endereco)

                        # Pasta Codigo
                        endereco = None
                        endereco = PASTA_CODIGO.format(
                                        largura=l["nome"],
                                        algoritmo=a["sigla"],
                                        computador=c["nome"]
                                    )
                        os.makedirs(endereco)

                        # Pasta Resultados
                        endereco = None
                        endereco = PASTA_RESULTADOS.format(
                                        largura=l["nome"],
                                        algoritmo=a["sigla"],
                                        computador=c["nome"]
                                    )
                        os.makedirs(endereco)

                        # Pasta Experimentos
                        endereco = None
                        endereco = PASTA_EXP_CSV.format(
                                        largura=l["nome"],
                                        algoritmo=a["sigla"],
                                        computador=c["nome"]
                                    )
                        os.makedirs(endereco)

                        endereco = None
                        endereco = PASTA_EXP_JSON.format(
                                        largura=l["nome"],
                                        algoritmo=a["sigla"],
                                        computador=c["nome"]
                                    )
                        os.makedirs(endereco)
                    else:
                        continue