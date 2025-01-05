# square = [i**2 for i in range(1,30)]
# print(square)
# l = ['abc','tuv','fgh']
# reverse = [i[::-1] for  i in l]
# print(reverse)
                            # OR

# def reverse_val(l):
#     return [name[::-1] for name in l]

# print(reverse_val(['abd','fnjkew','jfjsefjewh']))
# for nums in range(1,11):
#     print (nums,end = ' ')
# def mixed (l):
#     mixed_number = []
#     for i in l:
#         if (type(i) == int or type (i)== float):
#             mixed_number.append(int(i))
#     return mixed_number
# print(mixed([True,False,[1,2,3],1,1.0,3]))
# new_list = [i**2 for i in range (1,10) ]
# for i in range(1,4):
#     new_list.append([1,2,3])
# even_number =[i if (i%2==0) else (i%2!=0) for i in range(1,11)]
# print(even_number)
# def func(l,**kwargs):
#     if kwargs.get('reverse_str') == True :
#         return [name[::-1].title() for name in l]
#     else:
#         return[name.title() for name in l]

# names =['ashwnani','rozor']
# print(func(names))
# def func(l,**kwargs):
#     lenovo = []
#     for name in l:
#         if kwargs.get ('reverse_str') == True:
#             return(lenovo.append(name[::-1].title()))
#         else:
#             return (name.title())
#     return lenovo
# names =['ashwnai','rozer']
# print(func(names))
def func(item):
    return len(item)
names = ['sabir','amit','niraj','nidhi']
print(max(names, key = func))