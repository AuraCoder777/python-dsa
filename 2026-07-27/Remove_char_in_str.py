def remove_char(s, char):
    if s == "":
        return ""

    if s[0].lower() == char:
        return remove_char(s[1:], char)

    return s[0] + remove_char(s[1:], char)


s = "car"
char = "a"

print(remove_char(s, char))