import string
import random
from timeit import default_timer as timer


start = timer()


a = str(input("Enter first name nibha \n"))
e = int(input("How many emails bruh? \n"))
g = int(input("how many digits bruh..? \n"))
c = open("email.txt", 'w', encoding='utf-8')
f = open("last_names.all.txt", "r", encoding='utf-8')
k = f.readlines()
for i in range(2):
    for j in range(e):
        d = a+str(k[j])+''.join(random.SystemRandom().choice(string.digits) for _ in range(g+1))+"@gmail.com\n"
        c.write(d)
c.close()

print("time : ", timer()-start)
