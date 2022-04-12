#List comprehension is using a for loop to create a new list from an existing list.

#We want to create a new list, wherein it's values have been doubled. Here's one way of doing it-

nums = [10, 20, 30, 40, 50]
nums_double = []

for n in nums:
    nums_double.append(n * 2)

print(nums)
print(nums_double)


#lets do that same thing using list comprehension

nums_doubled = [n * 2 for n in nums]

print(nums_doubled)


#We can add conditions, too. Say we wanted to double our list, but only values that were divisible by 4?

nums_doubled = [n * 2 for n in nums if n % 4 == 0]
print(nums_doubled)

#We can do it with multiple lists, too. Let’s write a list comprehension which creates tuples out of the values in two lists when their sum is greater than 100. These tuples are the elements of the new list.

list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)
