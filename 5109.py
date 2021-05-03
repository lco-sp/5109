#latin and alphanumerical, 41 syms, name der img file greek für "Nachahmung"?


# jkllahm wiederholt sich 2 mal

# k vmtl vokal
# l und t konsonanten

#k 4 VOKAL
#a 4
#h 4
#l 5 (xx) KONSONANT
#b 1
#c 2
#d 1
#e 1
#f 2
#g 1
#i 1
#j 2
#m 2
#n 1
#o 1
#p 1
#q 2 (xx)
#r 1
#s 1
#t 2 (xx) KONSONANT
#u 1
#v 1

#JKLLAHM 2


#mimisi.png

#ABCDEFGHIJKLLAHMFNKOPCQQRSKTTAULHVJKLLAHM


import string

enc_str = "ABCDEFGHIJKLLAHMFNKOPCQQRSKTTAULHVJKLLAHM"

alphabet_list = list(string.ascii_lowercase + string.digits)

enc_alph_list = list("ABCDEFGHIJKLMNOPQRSTUV")

enc_str_list=[]
enc_str_list[:0]=enc_str

dec_map = [alphabet_list][enc_alph_list] #map one value from alpahbet_list to enc_alph_list
#doesnt work like that, how to create clean mapping?

dec_map = [len(alphabet_list)] #ref to enc_alph_list? permutate() needs logic to make sure no perms are ignored or duplicated

def output_decrypt(dec_str_list, attempt_no){
        print("Attempt: " + attempt_no + ": " + dec_str_list + "\n")
        }

def permutate(dec_map, iteration){
        for i in #idk do
            #do recursive logic
        dec_str_list = decrypt(dec_map, enc_str_list)
        output_print(dec_str_list, iteration)
        iteration = iteration + 1
        }

def decrypt(dec_map, enc_str_list){
        return dec_str_list
        }

def main(){
        permutate(dec_map, 1)
        }
