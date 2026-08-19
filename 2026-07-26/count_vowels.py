#Count vowels of a string
def count_vowels(s):
    if s == "":
        return 0
    if s[0] in "AEIOUaeiou":
        return 1 + count_vowels(s[1:])
    return count_vowels(s[1:])

print(count_vowels("SERGIO RAMOS"))