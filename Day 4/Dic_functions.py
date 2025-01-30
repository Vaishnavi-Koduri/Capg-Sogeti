d= {'egg': 1, 'milk':2, 'bread':3, 'butter':4}
print(d.items()) #prints all the items in the list

print(d.keys()) #prints all the keys

print(d.values()) #prints all the values

a= d.copy()
print(a) #prints all the copied key and values

print(d.get('milk',0)) #extracts the value of the mentioned key

d.push('sugar':5)
print(d.items())