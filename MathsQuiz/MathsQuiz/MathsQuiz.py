import random

input("What is your name? ")
score = 0
loop = 0
while loop < 10:
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    x1 = random.randint(1, 3)
    if x1 == 1:
        ans = n1 + n2
        op = " + "
    elif x1 == 2:
        ans = n1 - n2
        op = " - "
    else:
        ans = n1 * n2
        op = " x "

    while True:
        try:
            usrAns = int(input(str(n1) + op + str(n2) + " = "))
        except ValueError:
            print("That is not a valid answer")
            continue
        else:
            breaks