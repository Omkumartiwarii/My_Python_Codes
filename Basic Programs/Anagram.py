def anagram_check(s1,s2):
    count = 0
    if(sorted(s1.lower()) == sorted(s2.lower())):
        count +=1
    
    return count

word1 = input("Enter 1st word : ")
word2 = input("Enter 2nd word : ")

Anagram = anagram_check(word1,word2)

if Anagram == 0:
    print(f"\"{word1}\" and \"{word2}\" is not Anagram")
else:
    print(f"\"{word1}\" and \"{word2}\" is Anagram")