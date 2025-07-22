# name = input("Enter your name sir\n")
# print("Good Afternoon ",name)

# replacing a string character with other string character
# letter = "Hello <name> " \
# "your age is <age> " \
# "thanks"
# print(letter.replace("<name>","Deepak").replace("<age>","34"))  #this aka replace chaining as now letter.replace("<name>","Deepak") work as a str for the later of the code
# # a new string is made and there is no change in the OG one
# print(letter)

# finding and replacing (double space)

doublespace = "This is a  str  "
print(doublespace.find("  ")) #tells the fiest index no. where "  " occured
print(doublespace.replace("  "," "))