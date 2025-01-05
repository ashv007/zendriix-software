# user = input("enter the number: ")
# total =0
# i = 0
# while i <len(user):
#     total +=int(user[i])
#     i +=1
# print(total)
# name = input("enter the name : ")
# total= 0
# i = 0
# while i < len(name):
#     total += name[i]
#     print(total)

# total = 0
# for i in range(10):
#     i +=1

#     total += i
#     print(total)
name = input("Enter your name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp +=name[i]