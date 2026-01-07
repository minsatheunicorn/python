def match_words(words):
    c=0
    l=[]
    for word in words:
        if len(word)>1 and word [0]==word[-1]:
            c+=1
            l.append(word)
    print("list of the words with first and last characters same",l)
    return c 
count=match_words(["abc","cfc","aba","1221","xyz"])
print("number of words are the same",count)