def main():

    myHotelsList = []
    myHotelsDict = {}
    roomsUnbooked = {}
    with open("hotels/hotels.txt", "r") as f:
       for i in f:
           myHotelsList.append(i[:-1])

    for i in myHotelsList:
        k = i.split(':')
        myHotelsDict[k[1]] = [k[0],int(k[2]), float(k[3])]
        roomsUnbooked[k[0]] = int(k[2])
  
    myBookingsList = []
    myBookingsDict = {}
    with open("hotels/bookings.txt", "r") as f:
       for i in f:
           myBookingsList.append(i[:-1])

    for i in myBookingsList:
        k = i.split(' ')
        myBookingsDict[k[0]] =[k[1],int(k[2])]

    confirmedBookings = 0
    unconfirmedcount = 0
    unconfirmedBookings = []
    for key, value in myBookingsDict.items():
        for i,j in myHotelsDict.items():
            if i == value[0]:
                if (j[1] - value[1] < 0) == False:
                    j[1] -= value[1]
                    confirmedBookings += 1
                else:
                    unconfirmedcount += 1
                    unconfirmedBookings.append(key)
    print(f'Unconfirmed booking: {','.join(unconfirmedBookings)} ')
    print(f'Confirmed bookings: {confirmedBookings} - Unconfirmed bookings: {unconfirmedcount}',end ='\n\n')
    print('Hotels status:')

    place=[]
    for j in myHotelsDict.values():
        place.append(j[0])

    for item in place:
        for l, h in roomsUnbooked.items():  
            for i, j in myHotelsDict.items():
                if item == j[0] and l == j[0]:  
                    print(3 * ' ',f'{item}: {roomsUnbooked[l]} rooms ({(j[1])} free)')
                    break
    max_free_rooms = -1
    hotel_with_most_free_rooms = []
    for i, j in myHotelsDict.items():
        if j[1] > max_free_rooms:
            max_free_rooms = j[1]
            hotel_with_most_free_rooms = j[0]    
    print('')    
    print(f'The hotel with the most free rooms: {hotel_with_most_free_rooms} ')
if __name__ == '__main__':
    main()
