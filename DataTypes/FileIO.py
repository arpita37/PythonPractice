myfile = open('DataTypes/test.txt')
print(myfile)
print(myfile.read()) ## Reads all the content of the file
print(myfile.read()) ### cursor reached the EOF because of the first reed
myfile.seek(0) ## resets the cursor
content = myfile.read()
print(content)
myfile.seek(0)
all = myfile.readlines() ## Retuns list of all lines
print(all)
myfile.close()

## to open and close together
with open('DataTypes/test.txt') as file:
    contents = file.readlines()
    
print(contents)

## write to a file
with open('DataTypes/test.txt',mode='w') as file:
    #contents = file.read() #io.UnsupportedOperation: not readable
    print(contents)

## read and write to a file
with open('DataTypes/test.txt',mode='r+') as file:
    contents = file.read()
    print(contents)