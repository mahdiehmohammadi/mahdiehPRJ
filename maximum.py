lst = [1, 100, 7, 34534534, 34, 1000, 324]

mx = lst[0]
for n in lst:
    if n > mx:
        mx = n

print(mx)
