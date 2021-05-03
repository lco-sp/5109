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

## recursive:

#  for c in enc_alph_list
#    recursive(c):
#    for d in alph_list
#      c = d
#      if c != is_last_element
#        recursive(c+1)
#      else:
#        print_decode(decode())


import string

enc_str = "ABCDEFGHIJKLLAHMFNKOPCQQRSKTTAULHVJKLLAHM"

alphabet_list = list(string.ascii_lowercase + string.digits)

enc_str_list=[]
enc_str_list[:0]=enc_str

dec_map = [36][22] #map one value from alpahbet_list to enc_str_list


