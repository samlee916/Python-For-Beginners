#An example about lists

another_list = []

my_list = ["apple", "pear", "orange", 1, another_list]

print(len(my_list))#prints out 5 since there are five elements in the list my_list

my_list1 = ["apple", "pear", "orange"]

my_list1.append("banana")#adds banana to my_list1

print(my_list1)#prints out my_list1

my_list1.pop()#pops out banana

print(my_list1)#prints only the three items originally listed

my_list1.pop(0)#pops out the first item in the list

print(my_list1)

my_list2 = ["apple", "pear", "orange"]

my_fruit = my_list2[1]#stores pear in the variable

print(my_fruit)#prints out pear 

my_list2.insert(0, "banana")#adds banana to item 0

print(my_list2)#prints out a list of four items

my_list2.remove("banana")#removes banana from the list

print(my_list2)#prints out three items: apple, pear, and orange

my_list3 = ["apple", "pear", "orange"]

my_list3.extend(["strawberry", "kiwi", "peach"])#adds multiple items in the list

print(my_list3)#prints out six items

new_list = ["apple", "pear", "orange", "strawberry", "kiwi", "peach"]

new_list1 = new_list[0:2]#shows only the first two items in the list

print(new_list1)#prints the first two items in the list