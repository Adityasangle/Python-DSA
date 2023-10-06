#Apple question
def reverse_str(s):
    if s == "":
        return ""
    else:
        return reverse_str(s[1:]) + s[0]
    

print(reverse_str("hello"))