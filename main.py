#
# # Variabler, string
# first_name = "Bro"
# last_name = "Code"
# full_name = first_name + " " + last_name
# print("Hej " + full_name)
# # print(type(full_name))
#
# # integer
# age = 20
# age += 1
# print("Your Age is: " + str(age))
# # print(type(age))
#
# # float
# height = 100.5
# print("Your height is: " + str(height))
# #print(type(height))
#
# # boolean
# human = True
# print("Are you a human: " + str(human))
#
#
# # name, age, attractive = "Bro", 21, True
# # print(name, age, attractive)
#
# #String methods
# name = "Bro Code"
# print(len(name))
# print(name.find("B"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("Bro Code", "Kalle Anka"))

#input
# name = input("What is your name? ")
# print("Hello " + name + "!")
#
# age = int(input("How old are you? "))
# print("You are " + str(age) + " years")

#slicing [start: stop: step]

# name = "Bro Code"
#
# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[0:8:2]
#
# print(funky_name)

#If statement

# age = int(input("How old are you? "))
#
# if age >= 18:
#     print("You are a adult")
# elif age < 0:
#     print("You havent been born get")
# else:
#     print("You are a child")

# list
#
# food = ["pizza", "hamburger", "hotdog", "spaghetti", "sushi", "pudding"]
#
# food[0] = "chicken"
# #print(food)
#
# #food.append("ice-cream")
# #food.remove("ice-cream")
# #food.pop()
# #food.insert(0, "cake")
# #food.sort()
#
# for x in food:
#     print(x)

#functions

# def hello(first_name, last_name, age):
#     print("Hello " + first_name + " " + last_name + "!", str(age) + " years old")
#     print("Have a nice day")
#
# hello("Bro","Code", 21)