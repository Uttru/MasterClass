def main():
    non_empty_lines=[]
    with open('quotes/quotes.txt','r') as file:
        for line in file:
            a=line.strip().split('\n')
            if a != ['']:  
                non_empty_lines.append(a[0])
    print(non_empty_lines)
    topics=[]
    with open('quotes/topics.txt','r') as file:
        for line in file:
            a=line.strip()
            topics.append(a)
    Name = [non_empty_lines[0],non_empty_lines[7],non_empty_lines[11],non_empty_lines[2]]
    aDict = {
        Name[0]: [non_empty_lines[1],  non_empty_lines[5] + non_empty_lines[6],  non_empty_lines[12]],
        Name[3]: [non_empty_lines[3]],
        Name[1]: [non_empty_lines[8] +" "+ non_empty_lines[9]+" " + non_empty_lines[10]],
        Name[2]: [non_empty_lines[11]]  
    }
    for author, quotes in aDict.items():
        for quote in quotes:
            for topic in topics:
                if f' {topic} ' in f' {quote} ':
                    a = quote
                    if len(quote) > 50:
                        a = quote[:50]+ "..." 
                    print(f"{author} - {a}")
                    



if __name__ == '__main__':
    main()