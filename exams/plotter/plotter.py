EMPTY = '.'
COLUMN = 5
RAW = 5

def opener(board):
    with open("plotter/plotter.txt", 'r') as file:
        for plot in file:
            words = plot.split()
            instruction = words[0]
            if instruction == 'P':
                x = int(words[1])
                y = int(words[2])
                board[RAW - 1 - y][x] = '*'
            elif instruction == 'H': 
                x = int(words[1])
                y = int(words[2])
                length = int(words[3])
                for j in range(x, x + length):#sağ doğru gilidiği için xler artacak
                    if j< RAW:
                        board[RAW - 1 - y][j] = '-'# sağ doğru - işareti koyulacak yani rowlar eşit kalıcak(burda y'ler bizim rowlarımız)x ler değişecek çünkü column o
                x = int(words[1])
            elif instruction == 'V':
                x = int(words[1])
                y = int(words[2])
                length = int(words[3])
                for i in range(y, y + length):# yukrı gidiliyor y ler artacak ama y bizim row unutuma
                    if i < COLUMN:
                        if board[RAW - 1 - i][x] != '-':
                            board[RAW - 1 - i][x] = '|'
                        else:
                            board[RAW - 1 - i][x] = '+'
    return board

def print_board(board):
    for i in range(RAW):
        for j in range(COLUMN):
            print(board[i][j], end='')
        print()

def main():
    board = [[EMPTY] * COLUMN for i in range(RAW)]
    for l in range(20):
        for m in range(20):
            print(EMPTY, end='')
        print()
    board = opener(board)
    print_board(board)

if __name__ == '__main__':
    main()