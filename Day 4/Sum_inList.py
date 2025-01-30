list= []
size=int(input("Enter size: "))
for i in range(size):
    num= int(input())
    list.append(num)
total_sum= sum(list)
print(total_sum)
print(list)