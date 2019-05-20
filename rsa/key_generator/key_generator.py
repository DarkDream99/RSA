class KeyGenerator(object):

    def __init__(self):
        p = 999979
        q = 999983
        n = p * q

        euler_func = (p - 1) * (q - 1)
        e = 65537  # Ferma numbers
        


