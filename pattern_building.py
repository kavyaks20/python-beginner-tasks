# print like this pattern
# *
# **
# ***
# ****
# *****

# for i in range(1,6):  #take the value of i in range 1to 5
#     # print (i,"ith value")
#     for k in range(1,i+1):
#         print("*", end ='')  #end ='' is used for to print in same line
#     print()   # this empty print function is used for to print in next line



#=========================

#####
####
###
##
#

# print like this pattern

for i in range (6,0,-1):
    # print(i)
    for k in range(1,i+1):
        print('#',end ='')
    print()



#not complete