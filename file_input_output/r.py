file1 = open("file_input_output/test.txt", "r")

print(type(file1))

data = file1.read()     # reads all content 
line1 = file1.readline()   #read only one line

print(data)
file1.close()
