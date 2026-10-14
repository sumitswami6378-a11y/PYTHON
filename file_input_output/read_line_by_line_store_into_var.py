def var(filename):

    var = ""

    file = open(filename,"r")

    for line in file:

        var = var + line

    file.close()

    return var

variable = var("text.txt")

print(variable)