#  take set input from user and print unique one
# a_set = set((input("Enter int number\n ")))
# # a_set.remove(' ')
# print(a_set)
#  the above one didnt work hehe
a_set = set()
n = int(input("enter a number\n "))
a_set.add(n);
n = int(input("enter a number\n "))
a_set.add(n);
n = int(input("enter a number\n "))
a_set.add(n);
n = int(input("enter a number\n "))
a_set.add(n);
print(a_set)
# I didnt use loop here

# can we have more than one data type in set
b_set = {23,'23'}
print(b_set)        # Yes can do
#  using len
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20')
print(s)
print(len(s)) # len = 2 cuz set take 2 and 2.0 as same so it only takes in one 

# can you change list in set 
s = {8, 7, 12, "Harry", [1,2]}
s.update(s(4,2))
print(s)
#  cant work cuz list is immutable