#   *  
#  *** 
# *****

n = 3
leftpart = n
rightpart = n
while n != 0:
    for f in range(1, 6):
        if leftpart <= f <= rightpart:
            print("*", end="")
        else:
            print(" ", end="")
    leftpart -= 1
    rightpart += 1
    n -= 1
    print()
print()
# -------------------------------------------------------------------------------
# *
# **
# ***
n=0
while(n!=3):
    count=n+1
    while(count!=0):
        print("*",end="")
        count-=1
    print()
    n+=1
print()
# ------------------------------------------------------------------------------------
"""
    ***
    * *
    ***
"""
n=3
while(n!=0):
    count=3
    while(count!=0):
        if(count==2 and n==2):   print(" ",end="")  #didnt find skip like name thing
        else:   print("*",end="")
        count-=1
    n-=1
    print()
print()