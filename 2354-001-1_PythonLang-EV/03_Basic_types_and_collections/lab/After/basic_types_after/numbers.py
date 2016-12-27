import math

print("Working with numbers:")
print()

text = input("What is your favorite *complex* number [x + yj]? ")  # 3+5j is a good one
z = complex(text)

while z.real == 0 or z.imag == 0:
    print("Come on, that's not a very imaginative imaginary number, try again.")
    text = input("What is your favorite *complex* number [x + yj]? ")  # 3+5j is a good one
    z = complex(text)

print("Oh, that's a good one")
print("Here are some facts about " + str(z) + ".")
len_z = math.sqrt((z * z.conjugate()).real)
print("Length: {0} which is approximately {1}.".format(len_z, int(len_z + .5)))
print('The real part is {0} and the imaginary part is {1}'.format(z.real, z.imag))
print('The real part {0} divisible by 2.'.format('is' if int(z.real) % 2 == 0 else 'is not'))

print()
print()