def main():
    while True:
        N=int(input('N: '))
        if N == 2 or N ==3 :
            break
        else:
            print('N should be 2 or 3 please try again')
    
    with open('word/a.txt', 'r') as file:
        for line in file:
            words = line.strip().replace(',', '').replace(';', '').split()
            print(words)
            if N == 2:
                for i in range(len(words) - 1):
                    if len(words[i]) == len(words[i + 1]):
                        print(f' ({words[i].upper()}, {words[i + 1].upper()})')
            elif N == 3:
                for i in range(len(words) - 1):
                    if len(words[i]) == len(words[i + 1]) == len(words[i + 2]):
                        print(f' ({words[i].upper()}, {words[i + 1].upper()}, {words[i + 2].upper()})')

if __name__ == "__main__":
    main()

           

          

