# listeyi okut ve kart sırasını içeri al

# kırmızı en büyük green yellow
# büyük küçüğü yer
# kırmızı 5 yeşil 3 yellow 1
# yerdeki kartlar puana eklenir
import sys
path = 'deck.txt'

def show_score(a, b):
    print(f"Player 1's score: {a}")
    print(f"Player 2's score: {b}\n")


def main():
    mydict = {"Red":5, "Green":3, "Yellow":1}
    p1s = 0
    p2s = 0
    hand = 1
    middle = 0
    result = "italianoo"
    with open(path,'r') as file:
        show_score(p1s, p2s)
        while (True):
            first = file.readline()[:-1]
            last = file.readline()[:-1]
            if not last:
                break
            print(f"Hand {hand}")
            print(f"Player 1's card: {first} ")
            print(f"Player 2's card: {last} ")
            p1h = mydict[first]
            p2h = mydict[last]
            if p1h == p2h:
                result = "draw"
                middle += (p1h + p2h)
            elif p1h > p2h:
                result = "Player 1 wins the hand"
                p1s += (p1h + middle + p2h)
                middle = 0
            elif p2h > p1h:
                result = "Player 2 wins the hand"
                p2s += (p1h + middle + p2h)
                middle = 0
            print(f'Result: {result}')
            show_score(p1s, p2s)
            hand += 1
    if p1s > p2s:             
        print(f'Player 1 wins with {p1s} points')
    else:
        print(f'Player 2 wins with {p2s} points')


    
    
    
    



if __name__ == '__main__' :
    if len(sys.argv) == 1:
        main()
    elif sys.argv[1] == "-h":
        print("usage:python dinosaur.py <file_name>")
    else:
        path = sys.argv[1]
        main()
 