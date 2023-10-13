f=open("myfile.txt","x")
f=open("myfile.txt","w")
f.write('''Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing contentow the file has more content!ow the file has more content! ''')
f=open("myfile.txt","r")
print(f.read())