#Task 1 Lists
your_list = [200, 50, "Python", 3 + 6, "Lab 3"]

print("") #Task 2

print(len(your_list))

print("") #Task 3

your_list.append(3.50)
print(your_list)

print("") #Task 4

your_list.insert(0, "OOP")
print(your_list)

print("") #Task 5

your_list.remove(3.5)
print(your_list)

print("") #Task 6

print(len(your_list))

print("") #Task 7

print(your_list[3])

print("") #Task 8

your_list[1] = 1000
print(your_list)

print("") #Task 9

print(type(your_list))

print("") #Task 10 Tuples

your_tuple = tuple(your_list)
print(your_tuple)

print("") #Task 11

print(type(your_tuple))

print("") #Task 12

print(your_tuple[0])

print("") #Task 13

print(len(your_tuple))

print("") #Task 14 (You can't change any value)

#your_tuple[0] = 5
#print(your_tuple)

print("") #Task 15

another_tuple = (5, 13, 24)
print(another_tuple)

print("") #Task 16

joined_tuple = your_tuple + another_tuple

print("") #Task 17

print(joined_tuple)

print("") #Task 18

your_list = list(joined_tuple)

print("") #Task 19

print(type(your_list))

print("") #Task 20 Set

your_set = set(your_list)

print("") #Task 21

print(len(your_set))

print("") #Task 22

your_set.add("Red")
print(your_set)

print("") #Task 23

your_set.add(1000)

print("") #Task 24

print(your_set)

print("") #Task 25

another_set = {1000, 3, 4}

print("") #Task 26

new_set= your_set & another_set
print(new_set)