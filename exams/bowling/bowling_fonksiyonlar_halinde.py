def reader(filename):
    with open(filename,'r') as file:
        bowlingDict= {}
        for lines in file:
            lines = lines.strip().split(';')
            surname = lines[0]
            name = lines[1]
            points= lines[2:]
            for i in range(len(points)):
                points[i]=int(points[i])
            bowlingDict [name + ' '+surname]= points
    return bowlingDict

def calculate_sum(bowlingDict):
    most_0_dict= {}
    most_10_dict={}
    sum_dict={}
    for i,j in bowlingDict.items():
        summed=sum(j)
        sum_dict[i]=summed
        most_10=0
        most_0=0
        for details in j:
            if details == 0:
                most_0 += 1
            if details == 10:
                most_10 += 1
        most_0_dict[i] = most_0
        most_10_dict[i] = most_10
    return most_0_dict, most_10_dict, sum_dict

def print_sum(sum_dict):
    sorted_sum_dict=dict(sorted(sum_dict.items(),key=lambda x: x[1],reverse=True))
    for i,j in sorted_sum_dict.items():
        print(f'{i}  {j}')
        
def print_most(most_0_dict, most_10_dict):
    max_10_count = max(most_10_dict.values())
    for names,most10 in most_10_dict.items():
        if most10== max_10_count:
            print(f'Most 10:{names} ({max_10_count} times)')

    max_0_count = max(most_0_dict.values())
    for names,most0 in most_0_dict.items():
        if most0== max_0_count:
            print(f'Most 0:{names} ({max_0_count} times)')
def main():
    filename = 'bowling/bowling.txt'

    bowlingDict=reader(filename)
    most_0_dict, most_10_dict, sum_dict=calculate_sum(bowlingDict)

    print_sum(sum_dict)
    print_most(most_0_dict, most_10_dict)


if __name__ == '__main__':
    main()