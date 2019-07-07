
def fact(n):
    if type(n) != int:
         raise Exception("line 1 ")
    elif n < 0 :
        raise Exception("line 2")
    else:
        out = 1
        while n > 0:
            out *= n
        n -= 1
    return out


print(fact(-1))