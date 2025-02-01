import sys
file= open("sample.txt","w")
file.write("Hello, a sample text")
file.close()

with open("sample.txt","w") as file: #Overwrites the text written before 
    file.write("Today is saturday. What are you doing?")

with open("sample.txt","r") as file:
    content= file.read()
    print(content)

with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())