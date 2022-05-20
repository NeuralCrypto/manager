from Bases.Chave        import Chave
from Bases.Conjunto     import Conjunto
from Estrutura.Pastas   import Pastas
#from Bases.Base         import Base


class Main:

    def __init__(self) -> None:
        pass

    def inicio(self):
        print("Gerenciamento de bases e experimentos")
        print("1. Geração de pastas de computadores, de bases e experimentos")
        print("2. Coleta e organização dos resultados")
        
        print("PASTAS: Estruturação")
        #Pastas().gerar()
        
        print("BASE: Geração")
        print("1.. Iniciando geração de chaves aleatórias")
        #Chave().gerar()
        print("2.. Iniciando geração de conjuntos de mensagens simples...")
        #Conjunto().distribuir()
        print("3.. Distribuição dos arquivos nos computadores respectivos")
        #Conjunto().copiar()
        
        print("EXPERIMENTOS: Geração")

if __name__ == "__main__":
    Main().inicio()