def binary(n,current=""):
    if len(current)==n:
        print(current)
        return
    binary(n,current+"0")
    binary(n,current+"1")

binary(3)
