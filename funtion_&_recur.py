# def sum_recur(n):
#     if(n==0):   return 0
#     return sum_recur(n-1) + n
# n = int(input("enter number\n"))
# value = sum_recur(n)
# print(value)
# print()
# -----------------------------------------------------------------------------------------
def pattern(n):
    col = 1
    row = n
    while(row!=0):
        store = col
        while(store!=0):
            print("*",end="")
            store-=1
        col+=1
        row-=1
        print()
n = int(input("enter no "))
pattern(n)

