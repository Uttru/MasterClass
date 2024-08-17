def req(x):
    if x == 0:
        return 1
    else:
        print(x)
        req(x-1)
    


req(10)