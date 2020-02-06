list = []
num = 11
value = 2
for value in range(num):
	value = value * value
	if value != 0:
		list.append(value)
print("\n")		
print(list)
print("Above is the list with square of numbers from 1 to 10 \n")
list.sort(reverse = True)
print(list)
print("Above is the list sorted in decending order \n")
del list[len(list)-3]
del list[len(list)-3]
print(list)
print("Above is the list with the 7th and 8th elements removed \n")
print("--------------------------------------------------------------------------------\n")


#code to copy dictionary in python
original = {1:'geeks', 2:'for'}
new_copy = original.copy()
print("Printing copy of the original dictionary ")
print(new_copy)

#code to clear dictionary in python
original.clear()
print("\nPrinting Original dictionary after clearing it ")
print(original)
print("\nPrinting the copy of original dictionary again")
print(new_copy)
print("\n -------------------------------------------------------------------------------")
print("\n")

#code to get the value of key shoes
inventory = {'shirts': 25, 'paints': 220, 'tshirts': 217}
num = inventory.pop('shoes',100)
print(num)
print("Value of Key shoes")
print("\n")

	  
# write the code using popitem() to return + remove arbitrary key value pair and print it 	
test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" : 2 } 
num1 = test_dict.popitem()
print(num1)
print("Arbitrary key value pair removed and returned")
print("\n")

# write the code to get the value for key 'C'. Print "Not found" if the key is not present
dic = {"A":1, "B":2} 
print(dic.get("C","Not Found"))
print("Tried to find the value of C")
print("\n")

# write the code to print the values in the dictionary
dictionary = {"A": 2, "B": 3, "C": 4} 
print(dictionary.values())
print("Printed the values in dictionary")
print("\n")

# Write the code to update "Dictionary1" with "Dictionary2" and print 	
Dictionary1 = { 'A': 'Geeks', 'B': 'For', } 
Dictionary2 = { 'B': 'Geeks' }  
print("Original Dictionary:") 
print(Dictionary1) 
Dictionary1.update(Dictionary2)
print("Updated Dictionary")
print(Dictionary1)
print("\n -------------------------------------------------------------------------------")
print("\n")

#Create a list of strings based on a list of numbers
numbers = [1, 3, 4, 6, 81, 80, 100, 95]
my_list = []
for num in numbers:
	a=num%2
	if a == 0:
		b=num%5
		if b==0:
			my_list.append("five even")
			#print(str(num) + " is five even ")
		else:
			my_list.append("even")
			#print(str(num) + " is even ")
	else:
		c=num%5
		if c==0:
			my_list.append("five odd")
			#print(str(num) + " is five odd")
		else:
			my_list.append("odd")
			#print(str(num) + " is odd ")	

print(my_list)

print("\n----- THE END -----")
assert my_list == ['odd', 'odd', 'even', 'even', 'odd', 'five even', 'five even', 'five odd']		