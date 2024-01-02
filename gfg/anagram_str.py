def check_anagram(s1,s2):
    chars = [0]*26
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        chars[ord(s1[i])-97]+=1
        chars[ord(s2[i])-97]-=1

    for i in range(26):
        if chars[i]!=0:
            return False
        
    return True

print(check_anagram("silent","llsent"))
