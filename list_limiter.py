inp = open('7lwords.txt', 'r')
outp = open('match_words.txt', 'w')

while True:
    line = inp.readline()
    if not line:
        break
    ll=list(line.strip())
    if patternfinder(ll):
        outp.write(line)
        outp.wirte("\n")
inp.close()
outp.close()

def patternfinder(word)
    #returns true only of word matches jkllahm char distribution
    i = 0
    for c in word:
        if not switcher(i, word):
            return False
        else
            i = i+1
    if i = 7:
        return True


def switcher(iteration, word):
    if iteration is 2:
        if word[iteration] is word[3]:
            return True 
    elif iteration is 3:
        if word[iteration] is word[2]:
                return True
    elif word.count(word[iteration]) is 1:
        return True
    else:
        return False
