# File IO Basics
"""
"r"  -  Open file for reading   - default
"w"  -  Open a file for writing
"x"  -  Creates files if not exists
"a"  -  Add more content to a file (also called as Append)
"t"  -  Text mode    - default
"b"  -  Binary mode
"+"  -  Read and write
"""

# OPEN()   READ()  &  READLINE()    functions in file
1
fp = open("17_William.txt")  # File Pointer "fp" is made`which is returned by "open" func
text = fp.read()  # value is stored in random variable text
print(text)  # whole Text file is printed
"""
William is a good boy.
He never fight with his younger sister Bella,
as he is afraid of his parents.
But when his parents leave the home,
he and his younger sibling fight like a WWE championship.
"Hahaha....kinda funny story, right ? "
"""
# 2
fp = open("17_William.txt")
print(fp.readline())  # First linne of file'll be printed
print(fp.readline())  # Second line of file'll be printed
"""William is a good boy.
He never fight with his younger sister Bella,"""
# 3
fp = open("17_William.txt")
for line in fp:  # to print line by line
    print(line)
"""William is a good boy.
He never fight with his younger sister Bella,
....
....
....
"""
# 4
m = open("17_William.txt", "rb")  # to read the file in Binary form
content = m.read(100)  # Only the characters read and printed
print(content)  # Binary mode is not the default mode for reading a file
m.close()  # to clode the file
"""b'William is a good boy.\nHe never fight with his younger sister Bella,
\nas he is afraid of his parents.'
"""

#############################

# WRITING()  &   APPENDING()  into a file
# 1
fp = open("17_William.txt", "w")  # 'w' for writing in the file
fp.write("This story actually belongs to me...hahaha")  # original text replaced
fp.close()
# 'This story actually belongs to me...hahaha'
# The above line will replace the text of file '17_William.txt'

# 2
fp = open("17_William.txt", "w")  # 'w' for writing in the file
c = fp.write("This story actually belongs to me...hahaha")  # No of characters in file printed
print(c)  # 42
fp.close()

# 3
fp = open("17_William.txt", "r+")  # 'r+' means both reading and writing in the file
print(fp.read())
fp.write("...Thanks for reading this sweet story")  # This line will be added to the file
fp.close()

# seek()  tell()  and  readline()   functions
fp = open("17_William.txt")
print(seek(0))  # seek() func will set our file pointer to 0'th character
print(fp.tell())
print(fp.readline())  # first line of the file will be printed
print(fp.tell())  # It tells us at which character our file pointer is right now
print(fp.readline())
print(fp.readlines())  # complete file will be printed

fp.close()  # closing the file is a good habit


# Use of WITH() function in place of OPEN() and CLOSE()
with open("17_William.txt") as fp:  # with() function can be used instead of open()
    print(fp.read())  # so basically there is no need for open() and close() functions now
