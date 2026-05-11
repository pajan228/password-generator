import random
import time

a='abcdefghijklmnopqrstuvwxyz'
b='ABCDIFGHIJKLMNOPQRSTUVWXYZ'
c='0123456789'
d='{}[]()*/,_"-!&@?'

all=a+b+c+d
length=8
password="".join(random.sample(all,length))
print('password generation is underway...')
time.sleep(2)
print(password)
print('Your password is ready!')
input()