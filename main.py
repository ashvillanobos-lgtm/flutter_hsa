from array_structures import ArrayStack, ArrayQueue
from linked_structures import LinkedStack, LinkedQueue

def is_balanced(expression):
    """6a: Use a stack to check whether a string of parentheses is balanced."""
    stack = LinkedStack()
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for symbol in expression:
        if symbol in "([{":
            stack.push(symbol)
        elif symbol in ")]}":
            if stack.is_empty():
                return False
            if stack.pop() != bracket_map[symbol]:
                return False
    return stack.is_empty()


def simulate_print_queue():
    """6b: Simulate a print queue."""
    printer_queue = LinkedQueue()
    print("\n--- Print Queue Simulation ---")
    printer_queue.enqueue({"job_name": "Job1", "page_count": 5})
    printer_queue.enqueue({"job_name": "Job2", "page_count": 12})
    printer_queue.enqueue({"job_name": "Job3", "page_count": 1})
    
    sequence = 1
    while not printer_queue.is_empty():
        current_job = printer_queue.dequeue()
        print(f"Wait Order {sequence}: Printed {current_job['job_name']} ({current_job['page_count']} pages)")
        sequence += 1


def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Test ArrayStack")
        print("2. Test LinkedQueue")
        print("3. Check Balanced Parentheses")
        print("4. Simulate Print Queue")
        print("5. Exit")
        
        selection = input("Select an option: ").strip()

        if selection == '1':
            my_stack = ArrayStack(3)
            try:
                my_stack.push(10)
                my_stack.push(20)
                my_stack.push(30)
                print(f"Peek top: {my_stack.peek()}")
                my_stack.push(40)  # Triggers overflow error
            except Exception as err:
                print(f"Error caught: {err}")
                
        elif selection == '2':
            my_queue = LinkedQueue()
            try:
                my_queue.enqueue("A")
                print(f"Dequeued: {my_queue.dequeue()}")
                my_queue.dequeue()  
            except Exception as err:
                print(f"Error caught: {err}")
                
        elif selection == '3':
            user_expr = input("Enter parentheses string to check: ")
            print(f"Is balanced? {is_balanced(user_expr)}")
            
        elif selection == '4':
            simulate_print_queue()
            
        elif selection == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()

