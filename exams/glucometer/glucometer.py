
def value_length(item):
    return len(item[1])

def main():
    with open('glucometer/glucometer.txt','r') as file :
        glucometerDict={}
        for lines in file:
            elements = lines.strip().split()
            if int(elements[2]) >= 200:
                if elements[0] not in glucometerDict:
                    glucometerDict[elements[0]] =[[elements[1], int(elements[2])]]
                else:
                    glucometerDict[elements[0]].append([elements[1], int(elements[2])])
        items = glucometerDict.items()
        sorted_items = sorted(items, key=value_length, reverse=1)
        sorted_dict = dict(sorted_items)
        for i,j in sorted_dict.items():
            for k in sorted_dict[i]:
                print(f'{i} {k[0]} {k[1]}')

if __name__ == "__main__":
    main()