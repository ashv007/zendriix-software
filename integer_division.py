def is_year_leap(year):
    test_data = [1900,2000,2016,1987]
test_resut = [False,True,True,False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_resut[i]:
        print("ok")
    else:
        print("Failed")