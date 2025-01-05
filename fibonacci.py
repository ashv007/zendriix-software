# def fibonacci_seq(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n== 2:
#         print(a,b)
#     else:
#         print(a,b,end =" ")
#         for i in range (n-2):
#             c= a+b
#             a= b
#             b=c
#             print(b,end=" ")
# fibonacci_seq(100)
# fruits = ['orange','apple','pear','banana','kiwi']
# # for loop
# for engry in fruits:
#     print(engry,end=" fuck u space ")
# number = list(range(1,16))
# def num1(l):
#     l.reverse()
#     # for i in l:
#     #     num1.append(:-1)
#     return l
# print(num1(number))
word = ['abc','tuv','xyz' ]
def reverse_element(l):
    elements = []
    for i in l:
        elements.append(i [:: -1])
    return elements
print(reverse_element(word))