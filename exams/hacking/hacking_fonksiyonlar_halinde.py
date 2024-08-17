def products_reader(product_filename):
    hackingPro = dict()
    with open(product_filename , 'r') as file:
        for i in file:
            i=i.split()
            hackingPro[i[0]]=i[1]
    return hackingPro
def transactions_reader(transactions_filename):
    hackingTra = dict()
    with open (transactions_filename,'r') as file:
        for i in file:
            i=i.split()
            if i[0] in hackingTra:
                hackingTra[i[0]].append(i[1])
            else:
                hackingTra[i[0]] = [i[1]]
    return hackingTra
def printer(hackingTra,hackingPro):
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
def main():
    product_filename ='hacking/products.txt'
    transactions_filename ='hacking/transactions.txt'
    
    hackingPro =products_reader(product_filename)
    hackingTra =transactions_reader(transactions_filename)
    print('Suspect transactions', end='\n\n')
    printer(hackingTra,hackingPro)
if __name__=='__main__':
    main()