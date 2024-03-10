pocketMoney =  3000
for day in range(32):
    if(day%2 == 0):
        continue
    if(pocketMoney == 0):
        break
    print('Go out Today!')
    pocketMoney = pocketMoney - 300
else:
    print('No go away from Home further more!')
