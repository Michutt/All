# hanoi towers


def hanoi(num):
    stack = [[item for item in range(num, 0, -1)], [], []]
    while len(stack[0]) != 0 or len(stack[1]) != 0:
        print(stack)
        item = int(input("From: "))
        item_dest = int(input("To: "))

        try:
            if len(stack[item_dest]) == 0 or stack[item][-1] < stack[item_dest][-1]:
                x = stack[item].pop()
                stack[item_dest].append(x)
            else:
                print("bigger disk")
        except:
            print("wrong move")


hanoi(5)