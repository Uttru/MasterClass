def main():
    kenar = input('lutfen kenar karakterinizi secin: ')
    kose = input('lutfen kose karakterinizi secin: ')
    sol_kosegen=input('lutfen sol kosegen karakterini secin: ')
    sag_kosegen=input('lutfen sag kosegen karakterini secin: ')
    return kenar, kose, sag_kosegen, sol_kosegen

def p(kenar,kose,sag_kosegen, sol_kosegen):
    si = 10
    for i in range(si):
        for j in range(si):
            if i==0 and j==0 or i== 0 and j==si-1 or i== si-1 and j==0 or j== si-1 and i== si-1:
                print(kose,end='')
            elif i==0 or j==0 or i== si-1 or j == si-1:
                print(kenar,end='')
            elif i == j :
                print(sol_kosegen,end='')
            elif j == si-1-i:
                print(sag_kosegen,end='')
            else:
                print(' ',end='')
            
        print()

if __name__ == '__main__' :
    kenar,kose,sag_kosegen,sol_kosegen = main()
    p(kenar, kose,sag_kosegen,sol_kosegen)

    