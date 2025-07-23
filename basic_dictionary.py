# # A small dictionary for hindi keywords to english one
# hindi_keywords = {
#     "insaan": "human",
#     "kutta": "Dog",
#     "billi": "Cat"
# }
# words = input("What do you want to see\n")
# print(hindi_keywords.get(words))

# same keys 
language = {}
name = input("Enter your name\n")
lan = input("Enter your preferred language\n")
language.update({name:lan})
name = input("Enter your name\n")
lan = input("Enter your preferred language\n")
language.update({name:lan})
name = input("Enter your name\n")
lan = input("Enter your preferred language\n")
language.update({name:lan})
name = input("Enter your name\n")
lan = input("Enter your preferred language\n")
language.update({name:lan})
print(language)
# so it updates the key to the latest thing assigned to it
# if the value assigned to key is same then there is no change to it