#
# jaccard.py
# Jaccard shingling algorithm project
#
# Copyright (c) 2012, Gokul Das
#

def bigram_shingler(str):
    """Extract a set of 2 character n-grams (character bigrams) from string"""
    big_set = {str[x:x+2] for x in range(0, len(str) -1) if len(str) > 1}
    return big_set

def jacc_ind(bigrams1, bigrams2):
    """Calculate Jaccard index for 2 bigrams"""
    unin = bigrams1 | bigrams2
    intn = bigrams1 & bigrams2
    if len(unin) == 0: return 0.0
    else: return len(intn) / len(unin)

from corpus import text
words = text.split()
corpus = {i : bigram_shingler(i) for i in words}

str = input("Enter a word. ").strip()
in_big = bigram_shingler(str)
index_list = [(i, jacc_ind(in_big, corpus[i])) for i in corpus]
sorted_list = sorted(index_list, key = lambda x : x[1], reverse = True)
print("\nThe 3 best matches are:")
for i in range(3): print(sorted_list[i][0])
