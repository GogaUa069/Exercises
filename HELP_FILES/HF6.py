from math import prod
from time import time

data_list = [-10, -10, 3, 1, 2]


def get_max_mul():
    data_list.sort()

    min_mul = prod(data_list[:2]) * data_list[-1]
    max_mul = prod(data_list[-3:-2]) * data_list[-1]

    prod_res = min_mul if min_mul > max_mul else max_mul

    return prod_res


start = time()
res = get_max_mul()
end = time()

res_time = end - start

print(f"The biggest multiplication: {res}")
print(f"Time: {round(res_time, 5)} s")
