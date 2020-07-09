import sys

inputs='''
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
'''


a = [i for i in inputs.split('\n')[1:-1]]
print(a)


class Queue:
    

    def __init__(self):
        self.lists=[]

    def push(self,x):
        self.lists.append(x)
        return

    def pop(self):
        return self.lists.pop()

    def size(self):
        return len(self.lists)

    def empty(self):
        if not self.lists:
            return 1
        else:
            return 0

    def front(self):
        return self.lists[0]

    def back(self):
        return(self.lists[-1])

Queue=Queue()


for i in range(1,int(a[0])):

    if a[i].startswith('push'):
        Queue.push(int(a[i].split(' ')[1]))
    elif a[i]=='front':
        print(Queue.front())
    elif a[i]=='pop':
        print(Queue.pop())
    elif a[i]=='size':
        print(Queue.size())
    elif a[i]=='empty':
        print(Queue.empty())
    elif a[i]=='back':
        print(Queue.back())

