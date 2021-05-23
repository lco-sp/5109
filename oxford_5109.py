from itertools import chain,repeat,count,islice
from collections import Counter
import string

enc_str = "ABCDEFGHIJKLLAHMFNKOPCQQRSKTTAULHVJKLLAHM"

alphabet_list = list(string.ascii_lowercase + string.digits)

alphabet_list_letter_only = list(string.ascii_lowercase)

turing_list = list['j', 'k', 'l', 'a', 'h', 'm']

enc_alph_list = list("ABCDEFGHIJKLMNOPQRSTUV")

def main():
    i = 0
    inp = open('match_words.txt', 'r')
    outp = open('oxford_output.txt', 'w')
    while True:
        line = inp.readline()
        if not line:
            break
        perm = list(line.strip().lower())
        
        #map the 6 unique syms from jkllahm onto the full encrypted string
        #j=0, k=1, l=2, a=4, h=5, m=6 (no 3, because l is present twice)
        #unknowns replaced with asterisks
        #hook is full jkllahm sequence
        
        hook = str(perm[0]) + str(perm[1]) + str(perm[2]) + str(perm[2]) + str(perm[4]) + str(perm[5]) + str(perm[6])
        turing_key = str(perm[4]) + "******" + str(perm[5]) + "*" + hook + "**" + str(perm[1]) + "**********" + str(perm[4]) + "*" + str(perm[2]) + "**" + hook

        #verbose version
        turing_key_verbose = str(perm[4]) + "BCDEFG" + str(perm[5]) + "I" + hook + "FN" + str(perm[1]) + "OPCQQRSKTT" + str(perm[4]) + "U" + str(perm[2]) + "HV" + hook

        #out = str(i) + ": " + hook + " :: " + turing_key
        out = turing_key + " :: Verbose: " + turing_key_verbose + " :: Key: " + hook + " :: Iteration: " + str(i)
        print(out)
        outp.write(out)
        outp.write("\n")
        i = i+1
    inp.close()
    outp.close()

main()

