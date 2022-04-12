#Evvery linked list consists of two components: data and next. Data stores data (woah) and the next compenent is a pointer from one node to another. The start of a linked list is known as the "head". It's a pointer, that points to the beginning of a linked list. The final component of a linked list is the idea of null. We call it None in Python, and it terminates the linked list. The last node in a singly linked list points to a null object, signifying the end of the linked list. 

#Inserting vlaues into a linked list is a constant time operation, versus an array which is O(n) time complexity. You have to shift all values over to add or remove a value to the beginning of an array, while you just have to change a couple pointers to insert a new node into a linked list. 

#Arrays are contiguous in memory, which allows the access time to values to be constant. You dont have that luxury with a linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None