import sys

input = sys.stdin.readline

stack = []
tail = 0
def io(n):
    global tail
    for i in range(n):
        command = input().strip()
        if command == 'pop':
            pop()
        elif command == 'size':
            print(tail)
        elif command == 'empty':
            empty()
        elif command == 'top':
            top()
        else:
            input_x = int(command.split()[1])
            push(input_x)

def pop():
    global tail
    if tail == 0:
        print(-1)
    else:
        print(stack[tail-1])
        del stack[tail-1]
        tail -= 1

def empty():
    global tail
    if tail == 0:
        print(1)
    else:
        print(0)

def top():
    global tail
    if tail == 0:
        print(-1)
    else:
        print(stack[tail-1])

def push(x):
    global stack, tail
    stack.append(x)
    tail += 1

N = int(input())

io(N)