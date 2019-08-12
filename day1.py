# def PowTwoGen(max=0):
#     n = 0
#     while n < max
#         yield 2**n
#         n +=1

# x = PowTwoGen(8)

# n = [1,2,3,4]
# sq = []
# for x in n:
#     x = x**2
#     sq.append(x)
# print(sq)

# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

a = 0
b = 0
steps = 0
direction = ' '
while True:
    q = input("enter the direction : ")
    if not q:
        break
    try:
        direction, steps = q.split(' ')
        steps = int(steps)
    except:
        print("sorry myan")
    if direction == "left":
        a = a-steps
    elif direction == "right":
        a = a+steps
    elif direction == "up":
        b = b+steps
    elif direction == "down":
        b = b-steps
    else:
        pass
q = (a**2 + b**2)**(1/2)
print("the output is ", int(q))


# x = int(input("up"))
# y = int(input("down"))
# z = int(input("left"))
# v = int(input("right"))
# a = (x-y)
# b = (z-v)

# e =((x-y)**2+(z-v)**2)**1/2
# print("the output is",int(e))
