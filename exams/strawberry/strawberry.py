def main():
    previous_words = []

    with open('strawberry/strawberry-short.txt', 'r') as file:
        for line in file:
            line = line.strip().replace('...', '').replace(',', '').split()
            if not line:
                continue
            
            for i in range(len(line)-2):
                if len(line[i])==len(line[i+1])==len(line[i+2]):
                    print(f'({line[i].upper()},{line[i+1].upper()},{line[i+2].upper()})')
           
            if len(previous_words) >= 2 and len(line) >= 1:
                if len(previous_words[-2]) == len(previous_words[-1]) == len(line[0]):
                    print(f'({previous_words[-2].upper()},{previous_words[-1].upper()},{line[0].upper()})')

            if len(previous_words) >= 1 and len(line) >= 2:
                if len(previous_words[-1]) == len(line[0]) == len(line[1]):
                    print(f'({previous_words[-1].upper()},{line[0].upper()},{line[1].upper()})')
            previous_words = line
if __name__ == '__main__':
    main()
