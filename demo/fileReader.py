def fileToStringList(filename):
    file = open(filename, 'r', encoding = "utf8")
    return file.readlines()