import random
class Meca(object):

    n = None

    def atributo(n):
        n = ["pedra", "papel", "tesoura"]
        random.shuffle(n)
        return n