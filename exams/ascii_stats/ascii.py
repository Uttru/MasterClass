def reader(filename):
    with open (filename,'r') as file:
        lines = file.readlines()
    return lines

def input_taker():
    x_cordinate = int(input('please enter the x cordinate: '))
    y_cordinate = int(input('please enter the y cordinate: '))
    square_size = int(input('please enter the square size: '))
    return x_cordinate, y_cordinate, square_size

def process(x_cordinate, y_cordinate, square_size,lines):
    for j in range(y_cordinate,y_cordinate + square_size):
        for i in range(x_cordinate,x_cordinate + square_size):
            print(lines[j][i], end="")
        print()

def check_true(x_cordinate, y_cordinate, square_size,lines):
    lines_length = len(lines[0])
    lines_clength = len(lines)
    if x_cordinate > lines_length:
        print('x cordinate out of index')
        exit(1)
    if y_cordinate > lines_clength:
        print('y cordinate out of index')
        exit(1)
    if square_size > lines_length - x_cordinate or square_size > lines_clength - y_cordinate:
        print('square size out of index')
        exit(1)
    if x_cordinate < 0 or y_cordinate < 0:
        print('you can not give negative value to cordinates')
        exit(1)

def main():
    filename = 'ascii_stats/ascii_short.txt'

    lines =reader(filename)
    x_cordinate, y_cordinate, square_size = input_taker()

    check_true(x_cordinate, y_cordinate, square_size,lines)
    process(x_cordinate, y_cordinate, square_size,lines)






















if __name__=='__main__':
    main()