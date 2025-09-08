from collections import Counter

sentence=input("Enter the sentence=")
words=sentence.split()

word_cnt=Counter(words)

print("Frequency of word:",dict(word_cnt))