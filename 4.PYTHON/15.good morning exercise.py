import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hours = int(time.strftime('%H'))
if(hours <= 12):
    print('Good Morning Sir!')
elif(hours <= 17):
    print('Good Afternoon Sir!')
else:
    print('Good Night Sir!')