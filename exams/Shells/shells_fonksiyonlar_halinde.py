import math
def prices_reader():
    with open('Shells/prices.dat','r') as file:
        price_dict={}
        for lines in file:
            lines_splitted=lines.strip().split()
            products =lines_splitted[0].replace(':','')
            prices = float(lines_splitted[1])
            price_dict[products]=prices
    return price_dict

def offers_reader():
    with open('Shells/offers.dat','r') as doc:
        offers_dict={}
        for pines in doc:
            pines=pines.strip().split(':')
            offer = tuple(pines[0].strip().split())
            free_product = pines[1].strip()
            offers_dict[offer] = free_product
    return offers_dict

def cart_reader():       
    with open('Shells/cart.dat','r') as text:
        cart_list= []
        for hines in text:  
            hines = hines.strip()
            cart_list.append(hines)
    return cart_list

def cart_count(offers_dict,cart_list):
    cart_counts = {}
    for item in cart_list:
        if item in cart_counts:
            cart_counts[item] += 1
        else:
            cart_counts[item] = 1

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
    return cart_counts

def printer(cart_counts,price_dict):
    total_price = 0
    for item, count in cart_counts.items():
        for m,l in price_dict.items():
            if item == m:
                total_price += l * count
    print(f"Final price: {total_price:.2f} EUR")

def main():
    price_dict = prices_reader()
    offers_dict =offers_reader()
    cart_list=cart_reader()
    cart_counts=cart_count(offers_dict,cart_list)
    printer(cart_counts,price_dict)

if __name__ == '__main__':
    main()
  