def main():
    with open('Shells/prices.dat','r') as file:
        dict_dict={}
        for lines in file:
            lines_splitted=lines.strip().split()
            products =lines_splitted[0].replace(':','')
            prices = float(lines_splitted[1])
            dict_dict[products]=prices

    with open('Shells/offers.dat','r') as doc:
        pines_dict={}
        for pines in doc:
            pines=pines.strip().split(':')
            offer = tuple(pines[0].strip().split())
            free_product = pines[1].strip()
            pines_dict[offer] = free_product
    with open('Shells/cart.dat','r') as text:
        hines_list= []
        for hines in text:  
            hines = hines.strip()
            hines_list.append(hines)
    
    cart_counts = {}
    for item in hines_list:
        if item in cart_counts:
            cart_counts[item] += 1
        else:
            cart_counts[item] = 1
    print(cart_counts)
    
    total_price = 0

    for item, count in cart_counts.items():
        for m,l in dict_dict.items():
            total_price += l * count
    

    print(f"Final price: {total_price:.2f} EUR")


if __name__ == '__main__':
    main()