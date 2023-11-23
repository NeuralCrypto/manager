import keras
import tensorflow as tf

class Tangente_hiperb:

    def __init__(self):
        valor = lambda x: keras.activations.tanh(self.A_TANH * x + self.B_TANH)
        return valor