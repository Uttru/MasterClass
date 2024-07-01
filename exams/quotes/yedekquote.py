# topic leri al
# flag koy ve ilk (quotelari alirken) olan yazar gerisi quote taki '/n' a kadar.
#
def main():
    topicL = []
    with open('quotes/topics.txt','r') as file:
        for line in file:
            topicL.append(line[:-1])
    print(topicL)
    flag = 1
    with open('quotes/quotes.txt','r') as file:
        name = ""
        quote = ""
        for line in file:
            if line[0] == '\n':
                flag = 1
                a = quote.split()
                for i in topicL:
                    if i in a:
                        k= quote[:50]+'...' if len(quote)> 50 else quote
                        print(k)
                        break
                name = ""
                quote = ""
            elif flag:
                name = line[:-1]
                flag = 0
            else:
                quote+= " " + line[:-1]
        if name:
            for i in topicL:
                if i in a:
                    k= quote[:50]+'...' if len(quote)> 50 else quote
                    print(k)
                    name =''
                    break
if __name__ == '__main__':
    main()