n1 = int(input('Enter num1 '))
n2 = int(input('Enter num2 '))
op = input('Enter operator ')

match op:
    case '+':
        print(n1+n2)
    case '-':
        print(n1-n2)
    case '/':
        print(n1/n2)
    case '*':
        print(n1*n2)
    case '%':
        print(n1%n2)
    case _ if(op == '//'):
        print(n1//n2)
    case _ if(op == '**'):
        print(n1**n2)
    case _ :
        print('Enter another operator')
