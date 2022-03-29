import random


def rand_arr(minn, maxx):
    res = [el for el in range(minn, maxx)]
    random.shuffle(res)

    return res
