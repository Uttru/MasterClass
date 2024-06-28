def main():
    actionsDict={}
    magic_boxes = 2
    with open('magic boxes/actions.txt','r') as file:
        for i in file:
            line_stripped=i.strip().split()
            name = line_stripped[0]
            item = line_stripped[3]
            if name == 'Bob':
                if len(actionsDict) >= magic_boxes and item not in actionsDict:
                    break
                if item not in actionsDict:
                    actionsDict[item] = 1
                else :
                    actionsDict[item] += 1
            if name == 'Carl':
                if item not in actionsDict:
                    print('can not take out {item}')  
                elif item in actionsDict and actionsDict[item] >= 1:
                    actionsDict[item] -= 1
                    if actionsDict[item] == 0 :
                        actionsDict.pop(item)
        
        print(actionsDict)
if __name__== '__main__':
    main()


        