import tensorflow as tf
import keras

class Staircase:

    def __init__(self, x, largura):
        valor = tf.constant([0.0])
        for i in range(0, 2**largura):
            novo = lambda x : keras.activations.sigmoid(-100*i + 100*x)
            valor = valor + novo(x)
        return valor