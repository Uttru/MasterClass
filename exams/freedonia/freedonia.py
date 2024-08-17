def rules_reader():
    rules = []
    with open('freedonia/rules-example1.dat', 'r') as file:
        for line in file:
            lines_splitted = line.strip().split()
            if lines_splitted[0].endswith(':'):
                lines_splitted[0] = lines_splitted[0][:-1]
            rules.append(lines_splitted)
    return rules
        
def dates_reader():
    with open('freedonia/dates-example1.dat', 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def process(rules, dates):
    date_items = {}
    for date in dates:
        date_items[date] = []
    
    for rule in rules:
        rule_date = rule[0]
        rule_items = rule[1:]
        rule_date_parts = []
        for part in rule_date.split('-'):  
            int_part = int(part)  
            rule_date_parts.append(int_part)  
        for date in dates:
            date_parts=[]
            for part in date.split('-'):
                int_date =int(part)
                date_parts.append(int_date)
            print(date_parts)
            if date_parts[2] >= rule_date_parts[2] :  
                for item in rule_items:
                    if item.startswith('+'):
                        item_name = item[1:]
                        date_items[date].append(item_name)
                    elif item.startswith('-'):
                        item_name = item[1:]
                        date_items[date].remove(item_name)
    return date_items

def printer(date_items):
    for keys,it in date_items.items():
        print(f'{keys}:')
        items = sorted(it)
        if items:
            for item in items:
                print(item)
        else:
            print()  

def main():

    rules = rules_reader()
    dates = dates_reader()
    date_items =process(rules, dates)
    printer(date_items)

if __name__ == '__main__':
    main()
