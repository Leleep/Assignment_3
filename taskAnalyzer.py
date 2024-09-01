def is_palindrome(text):
    if text == text[::-1]:
        print("The text is a palindrome")
    else:
        print("The text is not a palindrome")

#is_palindrome(input("Enter a text: "))

def smthn(x):
    if x.isnumeric() == True and int(x) >= 0:
        y = int(x)
        if y % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        smthn(input("Please enter a positve integer: "))

#smthn(input("Enter a positve integer: "))

def only_alphabets(inp):
    if inp.isalpha() == True:
        print("Alphabet only")
    else:
        print("Contains non-alphabetic characters.")

#only_alphabets(input("Enter a single word: "))

def longest_word(x):
    list1 = x.split(" ")
    for i in range(len(list1)):
        for j in list1[i+1:]:
            if len(list1[i]) >= len(j):
                lrgst = list1[i]
            else: lrgst = j
    print(lrgst)

#longest_word(input("Enter a text: "))

def num_words(x):
    list2 = x.split(" ")
    print("Number of words in this string is: ", len(list2))

#num_words(input("Enter a text: "))