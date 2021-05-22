from itertools import chain,repeat,count,islice
from collections import Counter
import string

enc_str = "ABCDEFGHIJKLLAHMFNKOPCQQRSKTTAULHVJKLLAHM"

alphabet_list = list(string.ascii_lowercase + string.digits)

turing_list = list['j', 'k', 'l', 'a', 'h', 'm']

enc_alph_list = list("ABCDEFGHIJKLMNOPQRSTUV")

#src: https://stackoverflow.com/questions/36429507/python-combinations-without-repetitions

def combinations_without_repetition(r, iterable=None, values=None, counts=None):
    if iterable:
        values, counts = zip(*Counter(iterable).items())

    f = lambda i,c: chain.from_iterable(map(repeat, i, c))
    n = len(counts)
    indices = list(islice(f(count(),counts), r))
    if len(indices) < r:
        return
    while True:
        yield tuple(values[i] for i in indices)
        for i,j in zip(reversed(range(r)), f(reversed(range(n)), reversed(counts))):
            if indices[i] != j:
                break
        else:
            return
        j = indices[i]+1
        for i,j in zip(range(i,r), f(count(j), counts[j:])):
            indices[i] = j


def main():
    i = 0
    for perm in combinations_without_repetition(6, alphabet_list):
        print(i)
        i = i+1

main()

