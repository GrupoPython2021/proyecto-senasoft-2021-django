import random
import string


def code_generator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

a = code_generator()

#print(a)
'''
r = lambda: random.randint(10000,99999)
print('%02X%02X%02X' % (r(),r(),r()))
print('%02X' % (r()))
'''

r = lambda: random.randint(90000,99999)
print(str('%02X' % (r())))
print('========')

#crear salas
#unirse sala
#hexadecimal









