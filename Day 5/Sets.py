empty_set={}
flowers={"rose","lilly","tulip"}
print(empty_set)
print(flowers)

flowers.add("hibiscus") #adds an item to the set
print(flowers)
flowers.remove("lilly") #removes an item from set
print(flowers)

l= [7,2,3,'rtc','pop']
l1= set(l)
print(l1)

flowers={"rose","lilly","tulip"}
colors= {"red","white","blue"}
res= (flowers|colors)
res1= (flowers^colors)
res2= (flowers-colors)
res3= (flowers&colors)
print(res)
print(res1)
print(res2)
print(res3)

