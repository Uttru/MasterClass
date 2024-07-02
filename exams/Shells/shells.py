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
    
    total_price = 0
    free_items = []

    for offer, free in pines_dict.items():
        min_offer_count = float('inf')  
        for product in offer:
            product_count_in_cart = cart_counts.get(product, 0)
            offer_count = offer.count(product)
            
            if offer_count > 0:
                offer_times = product_count_in_cart // offer_count
                if offer_times < min_offer_count:
                    min_offer_count = offer_times
        
        if min_offer_count > 0:
            free_items.extend([free] * min_offer_count)
            for product in offer:
                cart_counts[product] -= offer.count(product) * min_offer_count
            
            print(f"As you buy {' '.join(offer)}; you got {free} for free")

    for item, count in cart_counts.items():
        total_price += dict_dict[item] * count

    print(f"Final price: {total_price:.2f} EUR")


if __name__ == '__main__':
    main()