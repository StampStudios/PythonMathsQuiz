import random, sqlite3, os
name = input("What is your name? ").title()
score = 0
if os.path.isfile("t2db.db"):   con = sqlite3.connect("t2db.db")
else:
    con = sqlite3.connect("t2db.db")
    for i in range(1, 4):   con.execute("CREATE TABLE class%s (ID INTEGER PRIMARY KEY, NAME TEXT, SCORE INTEGER);" %i)
cur = con.cursor()
for i in range(10):
    n1 = random.randint(1, 10)  
    n2 = random.randint(1, 10)
    op_int = random.randint(1, 3)
    if op_int == 1: ans = n1 + n2
    elif op_int == 2:   ans = n1 - n2
    else:    ans = n1 * n2
    if op_int == 1: op = " + "
    elif op_int == 2:   op = " - "
    else:   op = " x "
    while True:
        try:    usrAns = int(input(str(n1) + op + str(n2) + " = "))
        except ValueError:  continue
        else:    break
    if int(usrAns) == ans:  score += 1
print("Well done you got a score of " + str(score) + "/10.")
table = "class%s" %s_class
with con:   cur.execute("INSERT INTO " + table + "(NAME, SCORE) VALUES (?, ?);", (name, score))
