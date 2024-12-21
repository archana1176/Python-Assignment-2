#List Exercise Q1. Create a list of 5 random numbers and print the list
list1=[1,5,4,6,10]
print(list1)
#print(type(list1))
# Q2. Insert 3 new values to the list and print the updated list.
list1.extend([11,15,20])
print(list1)
#Q3. Try to use a for loop to print each element in the list.
for elements in list1:
    print(elements)
# Dictionary Exercise Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
user={'name':'John','age':'25','address':'New York'}
print(type(user))
print(user)
#Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.
user['phone']='1234567890'
print(user)
#Set Exercise Q1.Create a set with values 1, 2, 3, 4, and 5
set1={1,2,3,4,5}
#print(type(set1))
print(set1)
#Add the value 6 to the set created in Q1.
set1.add(6)
print(set1)
# Remove the value 3 from the set created in Q1.
set1.remove(3)
print(set1)
#Tuple Exercise Q1. Create a tuple with values 1, 2, 3, and 4
tuple1=(1,2,3,4)
print(tuple1)
print(type(tuple1))
#Q2. Print the length of the tuple created in Q1
print(len(tuple1))
