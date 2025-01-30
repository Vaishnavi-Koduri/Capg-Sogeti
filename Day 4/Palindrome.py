def Palindrome(sentence):
    # value=sentence[::-1]
    if sentence == sentence[::-1]:
        print("The string is Palindrome!! ")
    else:
        print("The string is Not Palindrome ")
        
def main():
    str= input()
    sentence= list(str)
    print("The list: ",sentence)
    res= Palindrome(sentence)
    print(res)
main()