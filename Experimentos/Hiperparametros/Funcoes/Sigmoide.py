import keras
import tensorflow as tf

class Sigmoide:

    def __init__(self, x, A_SIGMOID=None, B_SIGMOID=None):
        if A_SIGMOID == None:
            A_SIGMOID = 1
        if B_SIGMOID == None:
            B_SIGMOID = 0
        valor = lambda x: keras.activations.sigmoid(A_SIGMOID * x + B_SIGMOID)
        return valor