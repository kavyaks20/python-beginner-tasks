
a = {1: 'kavya',2:'jack',3:'jane',4:'hope',5:'don'}
z = {i:a[i] for i in a}
print(z)

k = {i:i*2 for i in range(1,10) if i%2==0}
print('hi',k)


b = {1: 'nika',2:'jao',3:'lane',4:'hipe',5:'jon'}
c = {b[i]:i for i in b}
print(c)