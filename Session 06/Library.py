from queue import LifoQueue as Stack

# Function to sort dictionary by keys [Task 1]
def sort_by_keys(dictionary):
    Sorted = {}
    for key,value in sorted(dictionary.items()):
        Sorted[key] = value
    return Sorted

# Function resieves stack from user [Task 5]
def get_stack(prompts="Enter non-zero value: "):
    stack = Stack()
    while True:
        answer = input(prompts)
        if answer and answer != '0':stack.put(answer)
        else:break
    return stack

# Function print stack elements
def display(stack):
    print("[",end=" ")
    while stack.qsize():
        if stack.qsize() == 1: print(stack.get(), "]")
        else: print(stack.get(),end=" ")