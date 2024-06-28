# import sympy

# x, y = sympy.symbols("x y")
# formula = (x -2*y) ** 3
# print(str(formula.expand()).replace("**", "^"))
def faq(n):
    ret = 1
    for i in range(1,n+1):
        ret *= i
    return ret

def pascalTriangle(n):
    for i in range(n+1):
        for j in range(i+1):
            print(faq(i)//(faq(j)*faq(i-j)),end=' ')
        print(end="\n")
    print()

def C(n, r):
    return faq(n)/(faq(n-r)*(faq(r)))

def binomi(n, x, y):
    for r in range(n+1):
        a = C(n,r)*x**(n-r)*y**r
        print(f'{a}', end=" ")
        if n-r != 0:
            print(f'x^{n-r}',end=" ")
        if r != 0:
            print(f'y^{r}',end=" ")
    print()

def main():
    a=0
    with open('binomial/powers.txt','r') as file:
        x,y = 0,0
        for i in file:
            if a == 0:
                a += 1
                l = i.split()
                x = float(l[0])
                y = float(l[1])
            else:
                n=int(i[:-1])
                binomi(n,x,y)
if __name__ == '__main__':
    main()
   