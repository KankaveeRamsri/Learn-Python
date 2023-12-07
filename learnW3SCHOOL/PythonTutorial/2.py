def get_valid_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Error! Value must be greater than 0.")
        except ValueError:
            print("Error! Please enter a valid integer.")

def get_average_speed(speeds):
    if speeds:
        return sum(speeds) / float(len(speeds))
    else:
        return 0

def main():
    car_quantity = get_valid_positive_integer_input("Enter the quantity of cars : ")
    car_speeds = []

    for i in range(1, car_quantity + 1):
        car_speed = get_valid_positive_integer_input("Enter car speed #{} (km/hr) : ".format(i))
        car_speeds.append(car_speed)

    average_speed = get_average_speed(car_speeds)
    print("Average car speed for the day is {:.2f} km/hr".format(average_speed))

if __name__ == "__main__":
    main()
