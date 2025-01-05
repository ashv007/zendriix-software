# def filter_odd_even(l):
#     even_num = []
#     odd_num = []
#     for i in l:
#         if i%2 == 0:
#             even_num.append(i)
#         else:
#             odd_num.append(i)
#     output = [odd_num , even_num]
#     return output
# nums = list(range(1,20))
# print(filter_odd_even(nums))
# def coman_finder(l1,l2):
#     output = []
#     for i in l1:
#         if i in l2 :
#             output.append(i)
#         # else:
#         #     None
#     return output
# print(coman_finder([1,2,3,4,5,6],[1,2,3,8,9,10,11]))
# number = [1,5,7,9]
# print(min(number))
# print(max(number))
# def sublist_counter (l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count
# print(sublist_counter(number))
mixed = (1,2,3,40.2)
for i in mixed:
    print(i,end = ' ')