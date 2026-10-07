def calculate_sum(*args):
    return sum(args)

def student_info(**kwargs):
    return kwargs

print(calculate_sum(10, 20,30))

print(student_info(name="John", role="Ml Engineer", skill="Python"))

stack = []
stack.append("Book-1")
stack.append("Book-2")
stack.append("Book-3")

print("Stack:", stack)

removed = stack.pop()
print("Removed:", removed)
print("Stack after pop:", stack)

from collections import deque
queue = deque()
queue.append("Person-1")
queue.append("Person-2")
queue.append("Person-3")

print("Queue:", queue)

removed = queue.popleft()
print("Removed:", removed)
print("Queue after popleft:", )