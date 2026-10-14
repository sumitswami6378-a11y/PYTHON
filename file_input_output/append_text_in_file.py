#program to append the text into the file and display it

def appending(filename,text):

    file = open(filename,"a+")

    file.write(text)

    file.seek(0)       # write k baad file pointer end pr hota h vo end pr hota h end pr hota h usko starting pr laane k liye seek(0) krenge


    content = file.read()

    print(content)

text = "sumit is the good boy"


appending("filename",text)