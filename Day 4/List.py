l1=[] #empty list
print("This is an empty list ", l1)

l2=[9,8,7] #list declaration with values
print("The list values are: ",l2)

l3=['vaish', ['roh','vara']] #nested list
print("The nested list values are: ",l3)

l4=list('spam')  #Converts a string into a list where each char in the string is an element
print("List of char values: ",l4)

l5=list(range(-5,5)) #Range between two integers
print(f"The values between -5 to 5:", l5)

l6=[10,9,8,7,6] 
print("The value at index 3 is: ",l6[3]) #Prints the value at index 3

l7=['x',[10,9,8,7],'y']
print("The element at l7[1][2] (nested list): ",l7[1][2]) #Accesses the index value 2 from the sublist

l8=[1,2,3,4,5,99,100,423]
print("Slicing  l8 from index 2 t0 6 :", l8[2:6]) #Slices and prints the values between index 2 to index 6
print("Length of l8",len(l8)) #Length of the list

l9=[1,[1,2,3,4],5]
print("Element at l9[1]: ",l9[1]) #Accesses the sublist 
print("Element at l9[1]: ",l9[1][3]) # Access element 3 from sublist
print("Element at l9[1]: ",l9[1][1:3]) #Slicing the sublist

print("Summary of the lists: ")
print("l1: ", l1)
print("l2: ", l2)
print("l3: ", l3)
print("l4: ", l4)
print("l5: ", l5)
print("l6: ", l6)
print("l7: ", l7)
print("l8: ", l8)
print("l9: ", l9)