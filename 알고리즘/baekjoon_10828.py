import sys

q = lambda : sys.stdin.readline().strip()
num_lines=int(q())
lists = [q() for _ in range(num_lines)]

if num_lines< 0 or  num_lines > 10000:
    sys.exit()



class Queue:
    

    def __init__(self):
        self.lists=[]

    def push(self,x):
        self.lists.append(x)
        return

    def pop(self):
        if self.size()!=0:
            return self.lists.pop()
        else:
            return -1

    def size(self):
        return len(self.lists)

    def empty(self):
        if self.size()!=0:
            return 0
        else:
            return 1

    def top(self):
        if self.size()!=0:
            return self.lists[-1]
        else:
            return -1
Queue=Queue()


for i in lists:

    if i.startswith('push'):
        Queue.push(i.split(' ')[1])
    elif i=='top':
        print(Queue.top()) 
    elif i=='pop':
        print(Queue.pop())
    elif i=='size':
        print(Queue.size())
    elif i=='empty':
        print(Queue.empty())

