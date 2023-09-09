def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    letters = [0]*26
    for letter in s1:
        letters[ord(letter)-97]+=1
    for letter in s2:
        letters[ord(letter)-97]-=1
    for letter in letters:
        if letter!=0:
            return False
    return True


s1 = input("Enter string s1: ")
s2 = input("Enter string s2: ")
print(is_anagram(s1,s2))