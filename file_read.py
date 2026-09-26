file = open("/content/emp.txt","w")
file.write("HELLO HOW ARE YOU")

with open("/content/emp.txt","r") as f:

    print(f.read)