global size, stack


def create_stack(N):
    global size, stack
    stack = [0] * N
    size = 0


def pop():
    global size, stack
    if size > 0:
        size -= 1
        return stack[size]


def push(x):
    global size, stack
    stack[size] = x
    size += 1


def main():
    create_stack(10)
    print(pop())
    push(5)
    push(3)
    print(pop())
    push(15)
    print(pop())
    push(13)
    print(pop())
    print(pop())
    print(pop())


if __name__ == '__main__':
    main()
