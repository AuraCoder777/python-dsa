#Palindrome of a string
def rev_str(s):
    if s=="":
        return ""
    return rev_str(s[1:]) + s[0]
def is_palindrome(s):
    if rev_str(s) ==  s:
        print("True")
    else:
        print("False")
    
is_palindrome("LOL")
        