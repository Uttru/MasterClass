def main():

    myHotelsList = []
    myHotelsDict = {}
    with open("hotels.txt", "r") as f:
       for i in f:
           myHotelsList.append(i[:-1])

    for i in myHotelsList:
        k = i.split(':')
        myHotelsDict[k[1]] = [k[0],int(k[2]), float(k[3])]
    print(myHotelsDict)

    myBookingsList = []
    myBookingsDict = {}
    with open("bookings.txt", "r") as f:
       for i in f:
           myBookingsList.append(i[:-1])

    for i in myBookingsList:
        k = i.split(' ')
        myBookingsDict[k[0]] =[k[1],int(k[2])]
   

    confirmedBookings = 0
    unconfirmedBookings = []
    print(myHotelsDict)
    print("a"*15)
    print(myBookingsDict)
    print("a"*15)
    for key, value in myBookingsDict.items():
        for i,j in myHotelsDict.items():
            if i == value[0]:
                j[1] -= value[1]
    print(myHotelsDict)

if __name__ == '__main__':
    main()
