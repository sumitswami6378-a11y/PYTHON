# read first n lines

def read(filename,n):

    file = open(filename,"r")

    for line in range(n):


        line = filename.readlines()

        print(line)

        if not line:
            break
        
    file.close()

read("test.txt",5)


