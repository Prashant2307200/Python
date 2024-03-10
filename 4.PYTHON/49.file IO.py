'''
file = open(fileName,mode:w,a,r,rb,rt)
text = file.read() or len = file.write("Hi")
file.close()
'''

# file = open('myFile.txt','w')
# len = file.write("Hi, harry how are you?")
# print(len)
# file.close()

file = open('myFile.txt','a')
len = file.write("Hi, harry")
print(len)
file.close()

with open('./myFile.txt','r') as file:
    text = file.read()
    print(text)