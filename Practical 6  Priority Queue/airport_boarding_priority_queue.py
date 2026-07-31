from colorama import init, Fore
import time

# Initialize Colorama
init(autoreset=True)


class PriorityQueue:
    def __init__(self, max_capacity):
        self.queue = []
        self.max_capacity = max_capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.max_capacity

    def enqueue(self, passenger, priority):
        if self.is_full():
            print(Fore.RED + "Boarding Queue is full. Cannot add passenger.")
            return

        self.queue.append((passenger, priority))
        self.queue.sort(key=lambda x: x[1])

        print(Fore.GREEN + f"Passenger '{passenger}' added successfully with Priority {priority}.")
        self.loading_animation()

    def dequeue(self):
        if self.is_empty():
            print(Fore.RED + "Boarding Queue is empty. No passenger to board.")
            return None

        passenger = self.queue.pop(0)[0]

        print(Fore.GREEN + f"Passenger '{passenger}' has boarded the flight.")
        self.loading_animation()
        return passenger

    def traverse(self):
        if self.is_empty():
            print(Fore.YELLOW + "Boarding Queue is empty.")
        else:
            print(Fore.CYAN + "\nCurrent Boarding Queue")
            print("-" * 40)
            for passenger, priority in self.queue:
                print(Fore.CYAN + f"Passenger : {passenger} | Priority : {priority}")

    def show_ascending(self):
        if self.is_empty():
            print(Fore.YELLOW + "Boarding Queue is empty.")
        else:
            print(Fore.CYAN + "\nPassengers (Highest Priority First)")
            print("-" * 40)
            for passenger, priority in sorted(self.queue, key=lambda x: x[1]):
                print(Fore.CYAN + f"Passenger : {passenger} | Priority : {priority}")

    def show_descending(self):
        if self.is_empty():
            print(Fore.YELLOW + "Boarding Queue is empty.")
        else:
            print(Fore.CYAN + "\nPassengers (Lowest Priority First)")
            print("-" * 40)
            for passenger, priority in sorted(self.queue, key=lambda x: x[1], reverse=True):
                print(Fore.CYAN + f"Passenger : {passenger} | Priority : {priority}")

    def loading_animation(self):
        for _ in range(2):
            for ch in ["-", "\\", "|", "/"]:
                print(Fore.BLUE + f"\rProcessing {ch}", end="", flush=True)
                time.sleep(0.15)

        print("\r" + " " * 30 + "\r", end="", flush=True)


def Main():

    while True:
        try:
            max_capacity = int(input("Enter Maximum Boarding Queue Capacity: "))
            break
        except ValueError:
            print(Fore.RED + "Please enter a valid integer.")

    pq = PriorityQueue(max_capacity)

    while True:

        print(Fore.YELLOW + "\n========== AIRPORT BOARDING PRIORITY QUEUE ==========")
        print("1. Add Passenger")
        print("2. Board Passenger")
        print("3. Display Boarding Queue")
        print("4. Check if Queue is Empty")
        print("5. Check if Queue is Full")
        print("6. Show Boarding Order (Ascending)")
        print("7. Show Boarding Order (Descending)")
        print("8. Exit")

        try:
            choice = int(input(Fore.BLUE + "\nEnter your choice: "))
        except ValueError:
            print(Fore.RED + "Invalid input! Enter a number between 1 and 8.")
            continue

        if choice == 1:
            passenger = input("Enter Passenger Name: ")

            try:
                priority = int(input("Enter Boarding Priority (1 = Highest): "))
                pq.enqueue(passenger, priority)
            except ValueError:
                print(Fore.RED + "Priority must be an integer.")

        elif choice == 2:
            pq.dequeue()

        elif choice == 3:
            pq.traverse()

        elif choice == 4:
            if pq.is_empty():
                print(Fore.CYAN + "Boarding Queue is Empty.")
            else:
                print(Fore.CYAN + "Boarding Queue is Not Empty.")

        elif choice == 5:
            if pq.is_full():
                print(Fore.CYAN + "Boarding Queue is Full.")
            else:
                print(Fore.CYAN + "Boarding Queue is Not Full.")

        elif choice == 6:
            pq.show_ascending()

        elif choice == 7:
            pq.show_descending()

        elif choice == 8:
            print(Fore.RED + "Thank You! Have a Safe Flight.")
            break

        else:
            print(Fore.RED + "Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    Main()
