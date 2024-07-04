def main():
    N=int(input('N: '))
    with open('word/a.txt', 'r') as file:
        for line in file:
            words = line.strip().replace(',', '').replace(';', '').split()
            if N == 2:
                for i in range(len(words) - 1):
                    if len(words[i]) == len(words[i + 1]):
                        print(f' ({words[i].upper()}, {words[i + 1].upper()})')
if __name__ == "__main__":
    main()

           

          

