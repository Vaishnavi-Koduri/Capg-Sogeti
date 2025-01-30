# Empty dictionary
d1= {}
print("d1 is empty")

# key-value
d2= {'egg': 2, 'milk': 3}
print(d2)

# Nested dictionary
d3= {'food': {'egg':2,'milk':3}}
print(d3)

# alternative construction methods
d4= dict(name='vaish',age=30)
print(d4)

# zip
keyslist= [1,2,3]
valslist= [4,5,6]
d5= dict(zip(keyslist,valslist))
print(d5)

d6= dict.fromkeys(['a','b'],[1,2])
print(d6)

flower= { 2:'rose', 3:'lilly', 4:'tulip'}
print("I bought a",flower[2])