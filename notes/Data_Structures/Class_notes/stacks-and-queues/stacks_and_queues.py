from collections import deque

# make a new queue
our_queue = deque()

# we are going to limit pop() append()
our_stack = []

# start with a stack [1, 2, 3, 4, 5]
our_stack.append(1)
our_stack.append(2)
our_stack.append(3)
our_stack.append(4)
our_stack.append(5)

# how do we get that first element over to my queue
our_queue.append(our_stack.pop())
our_queue.append(our_stack.pop())
our_queue.append(our_stack.pop())
our_queue.append(our_stack.pop())
our_queue.append(our_stack.pop())

# we want a stack [5, 4, 3, 2, 1] so we can
our_stack.append(our_queue.popleft())
our_stack.append(our_queue.popleft())
our_stack.append(our_queue.popleft())
our_stack.append(our_queue.popleft())
our_stack.append(our_queue.popleft())

print(our_stack.pop())
print(our_stack.pop())
print(our_stack.pop())
print(our_stack.pop())
print(our_stack.pop())

# this helped us reverse our order of our stack
