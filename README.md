# 5109
Attempt at decrypting the One-Time-Password known as SCP-5109

http://www.scpwiki.com/scp-5109

7lwords.txt filtered through list_limiter.py, then iterated through by oxford_5109.py  

Frequency analysis:  
k 4 VOWEL?  
a 4  
h 4  
l 5 (xx) CONSONANT?  
b 1  
c 2  
d 1  
e 1  
f 2  
g 1  
i 1  
j 2  
m 2  
n 1  
o 1  
p 1  
q 2 (xx)  
r 1  
s 1  
t 2 (xx) CONSONANT?  
u 1  
v 1  

jkllahm 2! Assumption: Is natural Word?

oxford_output.txt: Candidates for jkllahm, includes matching words from Oxford English Dictionary and as much key as possible

Nolan: Article notes "aberrance", possibly indicating a direct link between the symbol shown and the char/int encoded. Some symbols look similar to upside-down chars/ints, with some elements of the encoded char/int obscured/moved

Solution: oxford_output.txt iteration 1157 combined with the hint of http://www.scpwiki.com/character-development (Iteration 1157 is made redundant by the hint, but still nice to see that it *was* in the candidate list, at least.)
