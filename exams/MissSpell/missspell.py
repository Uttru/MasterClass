
# kutay mutay
def check1off(name, linees):
    name = name.lower()
    linees = linees.lower()
    if len(name) != len(linees):
        return False
    flag = 0
    for i in range(len(name)):
        if name[i] == linees[i]:
            flag += 1 
    if flag == len(name) - 1:
        return True
    else:
        return False

def main():
    with open('MissSpell/names.txt','r') as file:
        for lines in file:
            name = lines[:-1]
            with open('MissSpell/parole_italiane (1).txt','r') as filee:
                print('\nName: '+name)
                flag = 0
                for linees in filee:
                    linees = linees[:-1]
                    if check1off(name, linees):
                        flag +=1
                        print(linees)
                if flag == 0:
                    print('WARNING: No similar words were found!!!')























if __name__ == '__main__':
    main()