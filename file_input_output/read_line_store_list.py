with open("test.txt","r") as file:

    list = []

    data = file.readline()

    if data in file:

        list.append(data.strip())


    print(list)
 
        

