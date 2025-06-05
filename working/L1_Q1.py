eps = 1
for i in range(55):
    eps_new = eps + 1
    print(eps_new)
    if eps_new == 1:
        print("Equal now")
        print(i)
    eps = eps/2

       