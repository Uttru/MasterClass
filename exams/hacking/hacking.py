#iki tane ayrı dict açılacak
#keyler eşit ise birden fazla veya farklı value değerleri olanlar print edilecek
def main():
    hackingPro = dict()
    with open('products.txt' , 'r') as file:
        for i in file:
            i=i.split()
            hackingPro[i[0]]=i[1]
    
    hackingTra = dict()
    with open ('transactions.txt','r') as file:
        for i in file:
            i=i.split()
            if i[0] in hackingTra:
                hackingTra[i[0]].append(i[1])
            else:
                hackingTra[i[0]] = [i[1]]
    print('Suspect transactions', end='\n\n')
    for i,j in hackingPro.items():
        kall = list()
        kall.append(j)
        for z,k in hackingTra.items():
            if z == i and k != j:
                kall.append(k)
        if len(kall[1]) >=2:
            print(f'Product code: {i}')
            print(f'Official seller: {j}')
            print(f'Sellers list: {kall[1]}', end="\n\n")
        elif kall[0] not in kall[1]:
            print(f'Product code: {i}')
            print(f'Official seller: {j}')
            print(f'Sellers list: {kall[1]}')
if __name__=='__main__':
    main()