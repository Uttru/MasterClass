EMPTY = '.'
COLUMN = 5
RAW = 5

def runner(*a):
    if a[4] == 'P':
        a[3][RAW - 1 - a[1]][a[0]] = '*'
    elif a[4] == 'H': 
        for j in range(a[0], a[0] + a[2]):#sağ doğru gilidiği için xler artacak
            if j< RAW:
                a[3][RAW - 1 - a[1]][j] = '-'# sağ doğru - işareti koyulacak yani rowlar eşit kalıcak(burda y'ler bizim rowlarımız)x ler değişecek çünkü column o
    elif a[4] == 'V':
        for i in range(a[1], a[1] + a[2]):# yukrı gidiliyor y ler artacak ama y bizim row unutuma
            if i < COLUMN:
                if a[3][RAW - 1 - i][a[0]] != '-':
                    a[3][RAW - 1 - i][a[0]] = '|'
                else:
                    a[3][RAW - 1 - i][a[0]] = '+'
    # print(a)
    # print(a[0], type(a[0]))



def opener(board):
    with open("plotter/plotter.txt", 'r') as file:
        for plot in file:
            words = plot.split()
            instruction = words[0]
            x = int(words[1])
            y = int(words[2])
            length = int(words[3]) if len(words) == 4 else 0
            runner(x, y, length, board, instruction)

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