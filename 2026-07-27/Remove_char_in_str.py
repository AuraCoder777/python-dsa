#Remove a character from a string
def remove_char(s, char):
    if s == "":
        return ""

    if s[0].lower()== char.lower():
        return remove_char(s[1:], char)

    return s[0] + remove_char(s[1:], char)


s = "Car"
char = "C"

print(remove_char(s, char))