class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    # Push Operation
    def push(self, item):
        if len(self.stack) == self.size:
            print("Stack Overflow!")
        else:
            self.stack.append(item)
            print(f"{item} inserted into stack.")

    # Pop Operation
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow!")
        else:
            print(f"{self.stack.pop()} removed from stack.")

    # Peek Operation
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty!")
        else:
            print("Top Element:", self.stack[-1])

    # Traversal (Display)
    def display(self):
        if len(self.stack) == 0:
            print("Stack is Empty!")
        else:
            print("Stack Elements (Top to Bottom):")
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i])

# Main Program
size = int(input("Enter Stack Size: "))
s = Stack(size)

while True:
    print("\n===== STACK MENU =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")