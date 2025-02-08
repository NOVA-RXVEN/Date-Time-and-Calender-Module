def hotel_cost(nights):
    return 170 * nights

def plane_ride_cost(city):
    
    if city == "Abu Dhabi":
        return 850
    elif city == "Canada":
        return 1250
    elif city == "France":
        return 1630
    elif city == "Dhaka":
        return 250
    
def rental_car_cost(days):
    if days >= 7:
        return (50*days) - 20
    elif days>=3:
        return(50*days) - 10
    else:
        return (50*days)
    
def trip_cost(city, days):
    h_c= hotel_cost(days)
    r_c= rental_car_cost(days)
    p_c= plane_ride_cost(city)
    
    sum = h_c + r_c + p_c
    return sum

d = int(input("Enter the Amount of Days you wish to Stay (in digit): "))
c = input("Enter the City where you want to visit\n1.Dhaka\n2.Canada\n3.Abu Dhabi\n4.France\nEnter Your Choice: ")

print()
print(f"Hotel Cost: ${hotel_cost(d)}")
print(f"Car Cost: ${rental_car_cost(d)}")
print(f"Plane Cost: ${plane_ride_cost(c)}")
print(f"Total Cost: ${trip_cost(c,d)}")