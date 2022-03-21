from collections import defaultdict, namedtuple,Counter,ChainMap,deque
from functools import reduce

#namedtuple
# point=namedtuple("point","x y")
# point(2,4)
# print(point)

#counter # deafaultdict
# counter = defaultdict(int)
# for i in "mississippi":
#     counter[i]+=1
# print(counter)

#Chainmap
# num=["abc",'uhfc']
# letters={"a":"A","b":"B"}
# num_letters=ChainMap(num,letters) 
# print(num_letters)

#deque
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