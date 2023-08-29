# for Var in range(0,11):
#     print (Var*" *")
# for Var in range(11,0,-1):
#     print (Var*" *")
h=10
for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))