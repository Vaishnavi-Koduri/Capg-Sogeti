# from math import inf
# def max_val(list):
#     max=-inf
#     for i in list:
#         if i>max:
#             max=i
#     print(max)

# def min_val(list):
#     min=inf
#     for i in list:
#         if i<min:
#             min=i
#     print(min)

# def main():
#     list= []
#     size= int(input("Enter size: "))
#     for i in range(size):
#         nums= int(input("Enter the numbers: "))
#         list.append(nums)
#     print("The list is: ",list)
#     max_val(list)
#     min_val(list)
# main()

def get_input():
    nums = [int(input(f"Enter number {i+1}:")) for i in range((int(input("Enter the size of nums:"))))]
    return nums

def min_max(nums):
    max = nums[0]
    min = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max:
            max = nums[i]
        else:
            nums[i] < min
            min = nums[i]
    return (max,min)

def main():
    nums = get_input()
    print("The maximun and minimum values are:", min_max(nums))
main()