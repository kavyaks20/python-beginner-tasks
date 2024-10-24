#-----sum of square of first 10 natuaral numbers

#1 * (2*2)*(3*3)*(4*4)
#sum of sqares of first 4 = 1+4+9+16

sum = 0
for i in range(1,4):
    i=i*i
    sum = sum+i
print (sum)
