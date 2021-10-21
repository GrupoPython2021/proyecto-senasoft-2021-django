import random
import string


def code_generator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#a = code_generator()


r = lambda: random.randint(90000,99999)
#print(str('%02X' % (r())))
#print('========')


b = random.randint(1, 6)
print('valor aleatorio:' + str(b))

#crear salas
#unirse sala
#hexadecimal