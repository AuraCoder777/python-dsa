#Sum of numbers in a list
def sum_list(l):
    if l==[]:
        return 0
    return l[0] + sum_list(l[1:])

l=[1,2,3,4,5]
print(sum_list(l))
    