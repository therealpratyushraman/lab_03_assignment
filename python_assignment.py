class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_flight_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None

    def search_by_source(self, source):
        found_flights = []
        for flight in self.flights:
            if flight.source == source:
                found_flights.append(flight)
        return found_flights

    def search_by_destination(self, destination):
        found_flights = []
        for flight in self.flights:
            if flight.destination == destination:
                found_flights.append(flight)
        return found_flights

def main():
    flight_table = FlightTable()

    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    while True:
        print("1. Search by Flight ID")
        print("2. Search by Source")
        print("3. Search by Destination")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            flight_id = input("Enter Flight ID: ")
            flight = flight_table.search_by_flight_id(flight_id)
            if flight:
                print("Flight ID:", flight.flight_id)
                print("Source:", flight.source)
                print("Destination:", flight.destination)
                print("Price:", flight.price)
            else:
                print("Flight not found.")
        elif choice == 2:
            source = input("Enter Source: ")
            found_flights = flight_table.search_by_source(source)
            if found_flights:
                for flight in found_flights:
                    print("Flight ID:", flight.flight_id)
                    print("Source:", flight.source)
                    print("Destination:", flight.destination)
                    print("Price:", flight.price)
            else:
                print("No flights found for the given source.")
        elif choice == 3:
            destination = input("Enter Destination: ")
            found_flights = flight_table.search_by_destination(destination)
            if found_flights:
                for flight in found_flights:
                    print("Flight ID:", flight.flight_id)
                    print("Source:", flight.source)
                    print("Destination:", flight.destination)
                    print("Price:", flight.price)
            else:
                print("No flights found for the given destination.")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
