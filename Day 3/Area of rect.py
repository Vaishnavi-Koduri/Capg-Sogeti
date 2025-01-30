def display(data):
    print(f"The area: {data}")

def get_input():
    received_len=input()
    received_wid=input()
    return (received_len,received_wid)

def area(len,wid):
    res= int(len)*int(wid)
    return(res)

def main():
    (len,wid)= get_input()
    comp_area= area(len,wid)
    display(comp_area)
main()