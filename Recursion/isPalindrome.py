def isPalindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return isPalindrome(s[1:-1])

s = input("Enter string")
print(isPalindrome(s))