t1= (0,)
print(t1) #Prints the values in the tuple

t2= (0,'no',1.9,3)
print(t2) # All values

t3= 0,'no',2.8,7
print(t3) #accepts values without the brackets

t4= (0,('ab',2,3))
print(t4) #Nested tuple

t5=tuple('vaish')
print(t5) #splits each char as one item

t6= ('ab','bc',6,0.3)
print(t6[1]) #prints the item at index 1

t7= (76,('vara','roh','vaish',8,6.4))
print(t7[1][2]) #prints the item at index 1 and index 2 in the sub tuple

t8= (76,('vara','roh','vaish'))
print(t8[1:3]) #slices the index 

t9= (223,5.6,9,'shd')
print(len(t9)) #length of the tuple

t10= ('srinitha',('vara','roh','vaish',8,6.4))
print(t10[0][1])