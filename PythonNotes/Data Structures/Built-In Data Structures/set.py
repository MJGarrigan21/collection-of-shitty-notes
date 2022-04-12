#Sets are maybe the simplest data structure in Python. They're essentially an unordered collection of data, sort of like a bag just containing random items. They're great for simply keeping track of the existence of items, though. Sets also do not allow duplicates, so you can convert another data structure to a set to remove them. Contents of a set are surrounded by curly brackets {}

random_set = {"Educative", 1408, 3.142, (True, False)}
print(random_set)
print(len(random_set))

#We can also create a set using the set() constructor. The main advantage it gives us is the ability to create an empty set.

empty_set = set()
print(empty_set)

random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)


#We can add a single item to a set by using the add() method. To add multiple items we can use update(). The input for update() must another set, list, tuple, or string. 

print(empty_set)

empty_set.add(1)
print(empty_set)

empty_set.update([2, 3, 4, 5])
print(empty_set)

#We can delete an item from a set by using discard() or remove(). The remove() method will generate an error is the item is not found, unlike discard().

print(random_set)

random_set.discard(1408)
print(random_set)

random_set.remove((True, False))
print(random_set)


#We can iterate through a set by using a for loop. SInce a set is unordered though, elements will be picked at random. In this next example, we'll take the elements of a set and append them to a list if they are odd:

odd_list = [1, 3, 5, 7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

for num in unordered_set:
    if(not num % 2 == 0):
        odd_list.append(num)

print(odd_list)