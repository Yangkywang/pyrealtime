import numpy as np


def gen_dummy_data(counter):
    data = np.random.randint(100, size=(1,))
    return ','.join([str(x) for x in data.tolist()])

def gen_randn_data(counter):
    return np.random.randn(1)
