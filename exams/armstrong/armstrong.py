def main():
    with open('armstrong/numbers.txt', 'r') as file:
        for line in file:    
            numberS = line.strip()
            sum_of_powers = sum([int(digit)**len(numberS) for digit in numberS])
            
            if sum_of_powers == int(numberS):
                print(f'{int(numberS)}', end='\n')
if __name__ == '__main__':
    main()