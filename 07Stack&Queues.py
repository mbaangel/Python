"""
Stack & Queues
"""

# Stack (LIFO)
stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# Pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print (stack.pop())

# Queue (FIFO)

queue = []

# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# Dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print (queue.pop(0))

print(queue)

# Web

def web_navigation():

    stack = []

    while True:

        action = input(
            "Add a url or acttion with next options 1. Forward, 2. Back/ 3. Exit"
        )

        if action == "3":
            print("Exiting web browser.")
            break
        elif action == "1":
            pass
        elif action == "2":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"You have navigated to the web: {stack[len(stack) - 1]}.")
        else:
            print("You are on the home page.")

web_navigation()

def shared_printed():

    queue = []

    while True:

        action = input("Add a document or select print/exit: ")

        if action == "exit":
            break
        elif action == print:
            if len(queue) > 0:
                print(f"Printing: {queue.pop(0)}")
        else:
            queue.append(action)

        print(f"Print Queue: {queue}")

shared_printed()
