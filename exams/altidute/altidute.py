def Control(alist,x,y):
    max_row = len(alist) -1
    max_col = len(alist[0]) -1
    if x < max_row:
        if alist[x][y] <= alist[x+1][y]: #sag
            return False
        
    if x < max_row and y > 0:
        if alist[x][y] <= alist[x+1][y-1]: #sag up
            return False
        
    if x < max_row and y < max_col:
        if alist[x][y] <= alist[x+1][y+1]: # sag down
            return False
        
    if x > 0 and y < max_col :    
        if alist[x][y] <= alist[x-1][y+1]:# sol down
            return False
        
    if x > 0 and y > 0:
        if alist[x][y] <= alist[x-1][y-1]:# sol up
            return False
        
    if x > 0 :
        if alist[x][y] <= alist[x-1][y]:# sol
            return False
        
    if y > 0:
        if alist[x][y] <= alist[x][y-1]: #ust
            return False
        
    if y < max_col:
        if alist[x][y] <= alist[x][y+1]:#alt
            return False

    return True

def main():
    alist=[]
    with open('altidute/map.txt','r') as file:
        for lines in file:
            lines= lines.strip().split()
            alist.append(lines)
    for x in range(len(alist)):
        for y in range(len(alist[x])):
           if Control(alist,x,y):
               print(alist[x][y],x,y)
           
if __name__ == '__main__':
    main()