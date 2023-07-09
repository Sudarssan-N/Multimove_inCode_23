import fastapi

bus_time = car_time = bike_time = metro_time =0

def find_optimal_time():
    if bus_time == car_time:
        return car_time 
    elif car_time >= bike_time:
        return bike_time
    elif car_time==bike_time==bus_time:
        return bike_time()
    else:
        return  bus_time