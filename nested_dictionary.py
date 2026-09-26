student = {

"name" : "sumit swami",
"branch" : "cse hindi",
"roll no." : "2501921690056",
"subject" : {

"DSTL" : 95 ,
"DIGITAL ELECTRONICS " : 89 ,
"DATA STRUCTURE AND ALGORITHM " : 89 ,
"COA " : 85,
"PYTHON " : 89 ,
"TECHNICAL COMMUNICATION" : "85"


}

}

print(student.keys())
print(student.values())
print(student.items())

student.update({"age" : 21 , "blood group" : "b+" })

print(student.items())

