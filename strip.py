# Question take two comma separated inputs from user
# 1.user name
# 2.A single character
# output
# 1 user name length
# count the character that user input(case insensitive)
# name, char =input("Enter the name and character comma seperated :").split(",")
# print(f"length of your name is {len(name)}")
# print(f"character count {name.strip().lower().count(char.strip().lower())}")
# replace
# find
# name ="she is beautiful and she is good dancer"
# is_pos1=(string.find("is"))#is_pos1----->number
# is_pos2=(string.find("is",is_pos1+1))
# print(is_pos2)
# print(name.center(len(name)+2, "*"))
# age = input("Enter the age : ")
# age = int(age)
# if age >= 14:
# print("you are above 14")
# else:
# print("you are small 14"
# wining_num = 50
# guess_num = int(input("enter the win number: "))
# if wining_num==guess_num:
# print("You win game!!!!")
# else:
# if wining_num >=guess_num:
# print("too low")
# else:
# print ("too high")
# name =input("enter the name lower/Upper :")
# age=int(input("enter the age:"))
# if (name.lower() or name.Upper()) and age >= 10: #excute via lower and upper method
# # if (name[0]=='a' or name[0]=='A') and age>=10: #excute via indexing method
#     print("You can watch coco movie")
# else:
#     print("You can not watch movie")

# s[] = int(input())
# print(s)
# print(s)
def main():
    n = int(input())
    arr = input()
    list1 = arr.split()
    list2 = list(map(int, list1))
    sort = sorted(list2)
    print(sort[-3])


main()
