#prices text açılacak saatler key ve value atanacak dictin içine
#users text açılacak idler key valuelar diğer liste
#for kodunda key
def main():
    time
    pricesDict={}
    with open('skipass/prices.txt', 'r') as file:
        for line in file:
            lineSplitted = line.split()
            DayTime = lineSplitted[0]
            start_time, end_time = lineSplitted[1].split('-')
            price = int(lineSplitted[2])
            pricesDict[DayTime] = {
                'start': int(start_time.replace(':', '')),
                'end': int(end_time.replace(':', '')),
                'price': price
            }
      
    with open('skipass/users.txt','r') as file:
        usersDict={}
        for line in file:
            lineSplitted= line.split()
            StartCloackToInteger=int(lineSplitted[2].replace(':',''))
            FinishCloackToInteger=int(lineSplitted[3].replace(':',''))
            usersDict[lineSplitted[0]]=[lineSplitted[1],StartCloackToInteger,FinishCloackToInteger]
        print(usersDict)
        TargetDate =input('please enter target date: ')
        TotalIncome= 0
        Morning =0
        Afternoon =0
        Full=0
        total=0
        for id, time in usersDict.items():
            if TargetDate == time[0]:
                start = time[1]/100
                end = time[2]/100
                if start >= pricesDict['Morning']['start'] and end <= pricesDict['Morning']['end']:
                    TotalIncome += pricesDict['Morning']['price']
                    Morning += 1
                    total += 1
                    print(f'Skipass {id}: Morning {pricesDict["Morning"]["price"]}.00 EURO')
                elif start >= pricesDict['Afternoon']['start'] and end <= pricesDict['Afternoon']['end']:
                    TotalIncome += pricesDict['Afternoon']['price']
                    Afternoon += 1
                    total += 1
                    print(f'Skipass {id}: Afternoon {pricesDict["Afternoon"]["price"]}.00 EURO')
                elif start >= pricesDict['Full']['start'] and end <= pricesDict['Full']['end']:
                    TotalIncome += pricesDict['Full']['price']
                    Full += 1
                    total += 1
                    print(f'Skipass {id}: FULL {pricesDict["Full"]["price"]}.00 EURO')

        print(f'Total income : {TotalIncome}', end="\n\n")
        print('User Status:')
        print(f'Morning {(Morning*100)/total}%')
        print(f'Morning {(Afternoon*100)/total}%')
        print(f'Morning {(Full*100)/total}%')

if __name__ == '__main__':
    main()