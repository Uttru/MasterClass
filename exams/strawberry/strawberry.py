# N yan yana ayni uzunlukta olan kelimeleri bir setin icine koyup en sonda bastiriyor.

def main():
    previous_words = []
    N=int(input('number :'))

    with open('strawberry/strawberry-short.txt', 'r') as file:
        all = ""
        for line in file:
            line = line.strip().replace('...', '').replace(',', '')
            if not line:
                continue
            all+=' '+line
        all = all.split()
        
            # for i in range(len(line)-2):
            #     if len(line[i])==len(line[i+1])==len(line[i+2]):
            #         print(f'({line[i].upper()},{line[i+1].upper()},{line[i+2].upper()})')
           
            # if len(previous_words) >= 2 and len(line) >= 1:
            #     if len(previous_words[-2]) == len(previous_words[-1]) == len(line[0]):
            #         print(f'({previous_words[-2].upper()},{previous_words[-1].upper()},{line[0].upper()})')

            # if len(previous_words) >= 1 and len(line) >= 2:
            #     if len(previous_words[-1]) == len(line[0]) == len(line[1]):
            #         print(f'({previous_words[-1].upper()},{line[0].upper()},{line[1].upper()})')
            # previous_words = line
        p =0
        for i in range(1, len(all)):
            a = []
            j = 0
            a.append(all[p])
            while len(all[i+j]) == len(all[p]):
                a.append(all[i+j])
                j+=1
                if (j >= N-1):
                    print(tuple(a))
                    break
            p +=1
                    
        # print(all)


if __name__ == '__main__':
    main()
