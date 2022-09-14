def max_prod_pair(num_arr):
    a = max(num_arr)
    num_arr.remove(a)
    b = max(num_arr)
    return a*b
