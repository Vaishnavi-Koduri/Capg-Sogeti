# with open("example.csv","w") as file:
#     file.write("Enter: Name, ID, Age")
#     n= int(input())
#     for i in range(n):
#         name,id,age= input("Enter name,id, age :").split()
#         file.write(f"{name} {id} {age}")

file1=open("sample1.csv","a")
n=int(input("enter no of employees:"))
file1.write("name,"+"id,"+"phone no,\n")
with open("sample1.csv","a") as file:
    # file.write("name,"+"id,"+"phone no,\n")
    while n!=0:
        name=input("enter name: ")
        file.write(name+",")
        id=(input("enter id: "))
        file.write(id+",")
        p_no=input("enter phone number: ")
        file.write(p_no+",\n")
        n-=1

with open("sample1.csv","r") as file:
    content=file.read()
    print(content)