from itertools import chain,repeat,count,islice
from collections import Counter
import string

enc_str = "ABCDEFGHIJKLLAHMFNKOPCQQRSKTTAULHVJKLLAHM"

alphabet_list = list(string.ascii_lowercase + string.digits)

alphabet_list_letter_only = list(string.ascii_lowercase)

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
        #out = str(i) + ": " + str(perm[2]) + str(perm[0])
        #print(out)
        
        #map the 6 unique syms from jkllahm onto the full encrypted string
        #j=0, k=1, l=2, a=3, h=4, m=5
        #unknowns replaced with asterisks
        #hook is full jkllahm sequence
        
        hook = str(perm[0]) + str(perm[1]) + str(perm[2]) + str(perm[2]) + str(perm[3]) + str(perm[4]) + str(perm[5])
        turing_key = str(perm[3]) + "******" + str(perm[4]) + "*" + hook + "**" + str(perm[1]) + "**********" + str(perm[3]) + "*" + str(perm[2]) + "**" + hook

        #verbose version
        turing_key_verbose = str(perm[3]) + "BCDEFG" + str(perm[4]) + "I" + hook + "FN" + str(perm[1]) + "OPCQQRSKTT" + str(perm[3]) + "U" + str(perm[2]) + "HV" + hook

        #out = str(i) + ": " + hook + " :: " + turing_key
        out = turing_key + " :: Verbose: " + turing_key_verbose + " :: Key: " + hook + " :: Iteration: " + str(i)
        print(out)
        i = i+1

    i = 0

    print("--------------------------------------------------------------------------------------------------------")
    print("-------------------------------NO-NUMBERS-SECTION-BEGINS------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------")

    #same, but no numbers (in case jkllahm does not include any number)
    for perm in combinations_without_repetition(6, alphabet_list_letter_only):
        hook = str(perm[0]) + str(perm[1]) + str(perm[2]) + str(perm[2]) + str(perm[3]) + str(perm[4]) + str(perm[5])
        turing_key = str(perm[3]) + "******" + str(perm[4]) + "*" + hook + "**" + str(perm[1]) + "**********" + str(perm[3]) + "*" + str(perm[2]) + "**" + hook

        #verbose version
        turing_key_verbose = str(perm[3]) + "BCDEFG" + str(perm[4]) + "I" + hook + "FN" + str(perm[1]) + "OPCQQRSKTT" + str(perm[3]) + "U" + str(perm[2]) + "HV" + hook

        #out = str(i) + ": " + hook + " :: " + turing_key
        out = turing_key + " :: Verbose: " + turing_key_verbose + " :: Key: " + hook + " :: Iteration: " + str(i)
        print(out)
        i = i+1

main()

