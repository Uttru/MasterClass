import math
def main():
    with open('Shells/prices.dat','r') as file:
        price_dict={}
        for lines in file:
            lines_splitted=lines.strip().split()
            products =lines_splitted[0].replace(':','')
            prices = float(lines_splitted[1])
            price_dict[products]=prices

    with open('Shells/offers.dat','r') as doc:
        offers_dict={}
        for pines in doc:
            pines=pines.strip().split(':')
            offer = tuple(pines[0].strip().split())
            free_product = pines[1].strip()
            offers_dict[offer] = free_product
    print(offers_dict)
            
    with open('Shells/cart.dat','r') as text:
        cart_list= []
        for hines in text:  
            hines = hines.strip()
            cart_list.append(hines)

    cart_counts = {}
    for item in cart_list:
        if item in cart_counts:
            cart_counts[item] += 1
        else:
            cart_counts[item] = 1

    total_price = 0
    # for item, count in cart_counts.items():
    #     if item =='A' and count> 2:
    #         if count % 2 == 0:
    #             bolum =(count/2) -1
    #         else:
    #             bolum =(math.floor(count/2))-1
    #         if bolum >= 1:
    #             cart_counts[item] -= bolum
    # print(cart_counts)
    for item, count in cart_counts.items():
        for offers,frees in offers_dict.items():
            if offers[0] == item and count >= len(offers):
                if count % len(offers) == 0:
                    bolum= (count/len(offers))-1
                else:
                    bolum=(math.floor(count/len(offers)))-1
                if bolum == 0.0:
                    bolum = 1.0
                if bolum >= 0:
                    cart_counts[frees]-= bolum
    print(cart_counts)

    for item, count in cart_counts.items():
        for m,l in price_dict.items():
            if item == m:
                total_price += l * count
    print(f"Final price: {total_price:.2f} EUR")
if __name__ == '__main__':
    main()
  