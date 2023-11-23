from A_Constantes.Pastas        import *
from A_Constantes.Computadores  import COMPUTADORES
from A_Constantes.Algoritmos    import *
from shutil import copytree, ignore_patterns

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
                        endereco = PASTA_BASE_CONJ.format(
                            largura=l["nome"],
                            algoritmo=a["sigla"],
                            computador=c["nome"]
                        )
                        try:
                            os.makedirs(endereco)
                        except:
                            continue

                        # Pasta Base - Chaves
                        if a["sigla"] == "AES" or a["sigla"] == "DES": 
                            endereco = None
                            endereco = PASTA_BASE_CHAVES.format(
                                largura=l["nome"],
                                algoritmo=a["sigla"],
                                computador=c["nome"]
                            )
                            try:
                                os.makedirs(endereco)
                            except:
                                continue
                        
                        # Pasta Base - Datasets 
                        endereco = None
                        endereco = PASTA_BASE_DATASETS.format(
                            largura=l["nome"],
                            algoritmo=a["sigla"],
                            computador=c["nome"]
                        )
                        try:
                            os.makedirs(endereco)
                        except:
                            continue
                        
                        # Pasta Base - Dados
                        endereco = None
                        for modo in c["modos"][a["sigla"]]:
                            for base in c["bases"]:
                                for chave in ALGO_CHAVE_PREFIX[a["sigla"]]:
                                    endereco = PASTA_DADOS_CHAVE.format(
                                        largura=l["nome"],
                                        algoritmo=a["sigla"],
                                        computador=c["nome"],
                                        modo=modo, 
                                        base=base, 
                                        chave=chave
                                    )
                                    try:
                                        os.makedirs(endereco)
                                    except:
                                        continue

                        # Pasta Codigo
                        endereco = None
                        endereco = PASTA_CODIGO.format(
                                        largura=l["nome"],
                                        algoritmo=a["sigla"],
                                        computador=c["nome"]
                                    )
                        try:
                            os.makedirs(endereco)
                            end_cliente = os.path.join(PASTA_INICIAL, "Cliente")
                            copytree(end_cliente, endereco, ignore=ignore_patterns(".git", ".vscode"))
                        except:
                            continue


                        # Pasta Resultados
                        endereco = None
                        endereco = PASTA_RESULTADOS.format(
                                        largura=l["nome"],
                                        algoritmo=a["sigla"],
                                        computador=c["nome"]
                                    )
                        try:
                            os.makedirs(endereco)
                        except:
                            continue


                        # Pasta Experimentos
                        endereco = None
                        endereco = PASTA_EXP_CSV.format(
                                        largura=l["nome"],
                                        algoritmo=a["sigla"],
                                        computador=c["nome"]
                                    )
                        try:
                            os.makedirs(endereco)
                        except:
                            continue


                        endereco = None
                        endereco = PASTA_EXP_JSON.format(
                                        largura=l["nome"],
                                        algoritmo=a["sigla"],
                                        computador=c["nome"]
                                    )
                        try:
                            os.makedirs(endereco)
                        except:
                            continue

                    else:
                        continue