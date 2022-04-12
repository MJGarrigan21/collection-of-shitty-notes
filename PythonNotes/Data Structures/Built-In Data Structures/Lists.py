# Lists are pretty useful and easy to maniuplate. Create a list by using brackets "[]". You can index lists, merge them together, all kinds of stuff. Here's some examples of indexing and merging:


world_cup = [[2006, "Italy"], [2010, "Spain"]]
world_cup2 = [[2014, "Germany"], [2018, "France"]]

print(world_cup[1])
print(world_cup2[0])

mergedlist = world_cup2 + world_cup
print(mergedlist)

world_cup.extend(world_cup2)
print(world_cup)


#The append methoid can be used to add an element to the end of a list. It's pretty easy:

num_list = []
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)

#You can also add an element at a particular point in the lsit by using the insert() method. It'll look like this- aList.insert(index, Element).

num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4) #inserting 4 at the 3rd index
print(num_list)

#Removing elements is also pretty easy. The counterpart of append() is pop(), which removes the last element in a list. You can store that element in a variable

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)
print(houses)

houses.remove("Ravenclaw")
print(houses)

#You can slice a list to find a specific part of it:

print(num_list[2:5])
print(num_list[0::2])


#you can verify an elements existence with the "in" operator.

cities = ["london", "paris", "beirut", "denver"]

print("denver" in cities)
print("moscow" not in cities)
print("moscow" in cities)
 

