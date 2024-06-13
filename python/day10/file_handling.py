####text filesappend
# open()
# modes of file - read(default), write,


## write - no file exist- create and write the content
# file exist - overwrite

# fh = open("./file1.txt", mode="w")
# fh.write("this is statement1\n")
# fh.write("this is statement2\n")
# fh.write("this is statement3\n")
# fh.close()#save

## append - no file exist- create and write the content
# file exist - append at the end of file

# fa= open("./file2.txt", mode="a")
# fa.write("this is statement4\n")
# fa.write("this is statement5\n")
# fa.write("this is statement6\n")
# fa.close()

## read(default)
# open("./file3.txt", mode="r")#FileNotFoundError: [Errno 2] No such file or directory: './file3.txt'
fr = open("./file2.txt", mode="r")
content = fr.read()
print(content)