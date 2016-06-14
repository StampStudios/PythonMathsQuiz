import random
usrName = input("What is your name? ")
score = loop = 0
while loop < 10:
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    op_int = random.randint(1, 3)
    if op_int == 1:
        ans = n1 + n2
        op = " + "
    elif op_int == 2:
        ans = n1 - n2
        op = " - "
    else:
        ans = n1 * n2
        op = " x "
    while True:
        try:    usrAns = int(input(str(n1) + op + str(n2) + " = "))
        except ValueError:
            print("That is not a valid answer")
            continue
        else:    break
    if int(usrAns) == ans:
        print("Correct!")
        score += 1
    else:   print("Incorrect!")
    loop += 1
print("Well done, " + usrName + " you got a score of " + str(score) + "/10.")