with open('newfile.txt','a') as file:
    file.write("10111213")
    file.truncate(15)

with open('newfile.txt','r') as file :
    file.seek(4)
    seek = file.tell()
    print(seek)
    text = file.read(2)
    print(text)