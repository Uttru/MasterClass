#eğer x ve y diğer bir line daki x ve y 'Ye eşit ise 

def main():
    with open('sensors/sensors.txt','r') as file:
        addict = {}
        max_sensor = float('-inf')  
        max_time = 0
        for line in file:
            line = line.strip().split()
            time = line[0]
            x = line[1]
            y = line[2]
            sensor = float(line[3])
            x_y= x +','+ y
            addict[line[0]]= x_y,sensor
            if sensor > max_sensor:
                max_sensor = sensor
                max_time = time
                max_key= x_y
    flag = 0
    final_dict = {}
    for key, value in addict.items():
        coordinates = value[0]
        sensor_value = value[1]
        if coordinates not in final_dict:
            final_dict[coordinates] = (key, sensor_value)
        else:
            flag = 1
            if flag == 1:
                existing_key, existing_value = final_dict[coordinates]
                new_value = (sensor_value + existing_value) / 2
                final_dict[coordinates] = (key, new_value)
                flag = 0

    for key, value in final_dict.items():
        print(f"({key}): {value[1]}")

    print(f"Maximum sensor value: ({max_key}) at {max_time}")

if __name__ == '__main__':
    main()
    

