lst = [1,2,3,4,5,6,7,8,12,23,1,23,12,4,35,45,6,3]


lst2 = [v**2 if v % 2 == 0 else v**3 for v in lst]
print(lst2)