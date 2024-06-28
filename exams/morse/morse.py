
def encode(path:str, mydict):
   with open(path ,'r') as file:
       for i in file :
           for a in i.upper():
               if a in mydict:
                   print(mydict[a],end=" ")

def decode(path:str,addict):
    with open(path,'r') as file :
        for i in file:
            for k in i.split():
                if k in addict:
                     print(addict[k],end="")
def main():
    morse_dict = {}
    decodeDict = {}
    with open ('morse.txt','r') as file :
        for i in file:
            a = i.split()
            morse_dict[a[0]]=a[1]
            decodeDict[a[1]]= a[0]
    with open ('commands.txt', 'r') as file:
        for i in file:
            b= i.split()
            if b[0] == 'e':
                print(f'\nEncoding file {b[1]} :')
                encode(b[1], morse_dict)
    
            else:
                print(f'\nDecoding file {b[1]} :')
                decode(b[1],decodeDict)
if __name__ == '__main__':
    main()