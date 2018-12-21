#An example of for loops

my_string = "this is a string"

for char in my_string: 
        print(char) #prints each character

a_string = "this is my string"

for g in a_string:
        if g == "g": #if there a g in the variable a_string
            print("G")

my_fruits = ["banana", "apple", "pear"]

for f in my_fruits:
    print("I like to eat " + f + ".")#prints out the sentence for each item on the list

for f in my_fruits:
        if f == "banana": #checks if banana is in the list
                print("I like bananas.") 
