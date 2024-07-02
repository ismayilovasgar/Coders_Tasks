import random
import math


def random_list():
    # asan_Yol
    return [
        int(math.pow(i, 2)) for i in random.sample([*range(21, 50)], 5) if i % 2 == 0
    ]

    # diger_Yol
    # my_list = [i for i in random.sample([*range(21, 50)], 5)]

    # def double_even(num):
    #     return int(math.pow(num, 2)) if num % 2 == 0 else num

    # return [*map(double_even, my_list)]


print(random_list())
