
class ParkingLot:

    def __init__(self, capacity):
        self.capacity = capacity
        self.parking_spots = [None] * capacity

    def display_parking_lot(self):
        print("\nParking Lot Status :")

        for index, spot in enumerate(self.parking_spots):
            if spot is None:
                print(f"Spot {index + 1}: [Empty]")

            else:
                print(f"Spot {index + 1}: [Occupied by car {spot}]")

    def park_car(self, car_number):

        for index in range(self.capacity):

            if self.parking_spots[index] is None:
                self.parking_spots[index] = car_number
                print(f"\nCar {car_number} parked in spot {index + 1}")
                return
            
        print("\nSorry, the parking lot is full.")

    def retrive_car(self, car_number):

        for index in range(self.capacity):

            if self.parking_spots[index] == car_number:
                self.parking_spots[index] = None
                print(f"\nCar {car_number} retrived from spot {index + 1}")
                return
            
        print(f"\nCar {car_number} is not in the parking lot.")

def parking_menu():
    print("\nPARKING LOT MANAGEMENT")
    print("1. Display Parking lot Status")
    print("2. Park a Car")
    print("3. Retrive a Car")
    print("4. Exit")

def main():
    parking_lot = ParkingLot(7)

    while True:
        parking_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            parking_lot.display_parking_lot()

        elif choice == "2":
            car_number = input("Enter car number to park: ")
            parking_lot.park_car(car_number)

        elif choice == "3":
            car_number = input("Enter car number to retrive: ")
            parking_lot.retrive_car(car_number)

        elif choice == "4":
            print("Exiting the app.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()