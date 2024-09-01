# x = float(input("Enter a floating point number: "))
# if x >= 10.0:
#     print("High")
# else:
#     print("Low")

# num = int(input("Enter an integer: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# text = input("Enter some text: ")
# if text.isupper():
#     print("All uppercase")
# elif text.islower():
#     print("All lowercase")
# else:
#     print("Mix of both")

# dofw = input("Enter a day of the week: ")
# print("Number of letters in the day's name is: ", len(dofw))

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# print("Average of a, b, c is: ", (a + b + c) / 3)

# def H_L(x):
#     if x >= 10.0:
#         print("High")
#     else:
#         print("Low")

# H_L(float(input("Enter a floating point number: ")))

# def P_N(num):
#     if x > 0:
#         print("Positive")
#     elif x < 0:
#         print("Negative")
#     else:
#         print("Zero")

# P_N(int(input("Enter an integer: ")))

# def case(text):
#     if text.isupper():
#         print("All uppercase")
#     elif text.islower():
#         print("All lowercase")
#     else:
#         print("Mix of both")

# case(input("Enter some text: "))

# def num_letters(dofw):
#     print("Number of letters in the day's name is: ", len(dofw))

# num_letters(input("Enter a day of the week: "))

def avg(a, b, c):
    print("Average of a, b, c is: ", (a + b + c) / 3)

avg(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: ")))