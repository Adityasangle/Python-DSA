def reverse_words(str):
    words = str.split()[::-1]
    return " ".join(words)

s1 = input("Enter string s1: ")
print(reverse_words(s1))