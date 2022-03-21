from collections import deque

# stack=deque()


# stack.append('first')
# stack.append('second')
# stack.append('third')
# stack.append('fourth')

# print(stack.pop())
# print(stack)

class stack:
    def __init__(self):
        self.container=deque()

    def push(self,v):
        self.container.append(v)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

s=stack()
s.push('1')
s.peek()
  

# #stack
# s=[]
# s.append('first')
# s.append('second')
# s.append('third')
# s.append('fourth')

# print(s)


# print(s.pop())
# print(s)

# print(s.pop())
# print(s)

# print(s.pop())
# print(s)