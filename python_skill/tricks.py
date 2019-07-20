from itertools import zip_longest


def n_grams(lst, n):
    return zip(*([iter(lst)] * n))


def n_grams_with_padding(lst, n, fillvalue=None):
    return zip_longest(*([iter(lst)] * n), fillvalue=fillvalue)
