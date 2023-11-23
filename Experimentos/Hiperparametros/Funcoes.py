import keras
import re
import tensorflow as tf

class Funcoes:

    def __init__(self):
        self.A_SIGMOID = 1
        self.A_TANH    = 1
        self.B_SIGMOID = 0
        self.B_TANH    = 0
        pass

    def definir(self, nome, largura=None):
        funcoes = []
        for funcao in nome:
            if nome[funcao]["CA_FUNCOES"][0] == "S":
                self.A_SIGMOID = float(re.findall('[\d+\.\d*]+', nome[funcao]["CA_FUNCOES"])[0])
                valor = lambda x: keras.activations.sigmoid(self.A_SIGMOID * x + self.B_SIGMOID)
                funcoes.append(valor)

            elif nome[funcao]["CA_FUNCOES"][0] == "T":
                self.A_TANH    = float(re.findall('[\d+\.\d*]+', nome[funcao]["CA_FUNCOES"])[0])
                valor = lambda x: keras.activations.tanh(self.A_TANH * x + self.B_TANH)
                funcoes.append(valor)
            
            elif nome[funcao]["CA_FUNCOES"][0] == "R":
                valor = lambda x: keras.activations.relu(x)
                funcoes.append(valor)
            
            elif nome[funcao]["CA_FUNCOES"][0] == "P":
                valor = None
                valor = lambda x: self.funcao_passo(x, largura)
                funcoes.append(valor)
            
            elif nome[funcao]["CA_FUNCOES"][0] == "Q":
                valor = None
                valor = lambda x: x**2
                funcoes.append(valor)

        return funcoes

    def funcao_passo(self, x, largura):
        valor = tf.constant([0.0])
        for i in range(0, 2**largura):
            novo = lambda x : keras.activations.sigmoid(-100*i + 100*x)
            valor = valor + novo(x)
        return valor
    
    def funcao_quadratica(self, x):
        valor = x**2
        return 