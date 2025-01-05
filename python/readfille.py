file = open('test.txt') 
# read all the contents of file
#read n number of characters by passing parameter
# print(file.read(5))
#read one single line at a time readline
# print(file.readline())
# print(file.readline())

# print line by line using readline method
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()
# count = 0
# line = file.readline()
# while line != "":
#     print(line)
#     count += 1
#     line = file.readline()

# print("Total number of lines: ", count)

for line in file.readline():
    print(line)

file.close()



# Print line by line using readline method