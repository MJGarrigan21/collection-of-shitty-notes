#Dictionaries are really useful data strucutres used to store key value pairs. Think first name/phone number. There are a few ways to make a dictionary, the first is to use curly brackets {}

empty_dict = {} #Empty dictionary
print(empty_dict)

phone_book = {"Batman": 468433, "Cersei": 237745, "Ghostbusters": 123456}

print(phone_book)

#We can also create a dictionary using the dict() constructor. Values will be assigned to keys using the + operator in this method.

empty_dict = dict()
print(empty_dict)

phone_book = dict(Batman=123456, Cersei=987654, Varonwe=456789)
print(phone_book)

#Alternative approach
phone_book = dict([('Batman', 123456), ('Cersei', 234567), ('Tuor', 3456789)])
print(phone_book)

#Now, since dictionaries have no linear indices, we don't need to keep track of specifically where values are stored. We can access a value by enclosing its key in square brackets, or by using the get() method. Here are some examples:

print(phone_book["Tuor"])
print(phone_book.get("Batman"))

#We can add new entries to a dictionary fairly easily, just assign a value to a key. If a vlaue already exists at this key, it will be updated.

phone_book["Godzilla"] = 858256
print(phone_book)

phone_book["Godzilla"] = 9000
print(phone_book)

#Just use the del keyword to remove an entry

del phone_book["Batman"]
print(phone_book)

#if you want to use the value you're trying to delete, use the pop(), or popitem() method.

tuor = phone_book.pop("Tuor")
print(phone_book)
print(tuor)

lastAdded = phone_book.popitem()
print(lastAdded)


#Just redefining our dictionary to a previous state-
phone_book = dict([('Batman', 123456), ('Cersei', 234567), ('Tuor', 3456789)])

#Check the length of a dict. by using the len() method
print(len(phone_book))

#The in keyword can be used to check the existence of a value-
print("Tuor" in phone_book)
print("Godzilla" in phone_book)


#To copy the contents of one dictionary into another, use the update() operation:
second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623} #Just creating a second dict. for this example
phone_book.update(second_phone_book)
print(phone_book)

#Python also support dictionary comprehensions, which are similar to list comprehensions- we'll be creating new key-value pairs based on an existing dictionary. To iterate through the dict., we'll use the dict.items() operation, which turns a dict into a list of key-value pairs. Here's an exmaple where we square the key, and append an exclamation point onto the end of each string value:

houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)
