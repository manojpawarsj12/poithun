import string
import random


def randomword(length):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(length+1))


a = str(input("Enter first name nibha \n"))
b = int(input("length of last letter nibha\n"))
e= int(input("How many emails bruh? \n"))

c = open("email.txt", 'w', encoding='utf-8')

for i in range(0, e+1):
    d = a+randomword(b)+"@gmail.com\n"
    c.write(d)
c.close()
