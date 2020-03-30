f= open("my_first_calculator.py","w+")

f.write('print(\'Welcome to this calculator!\')\n')
f.write('print(\'It can add, subtract, multiply and divide whole numbers from 0 to 50\')\n')
f.write('num1 = int(input(\'Please choose your first number: \'))\n')
f.write('sign = input(\'What do you want to do? +, -, /, or *: \')\n')
f.write('num2 = int(input(\'Please choose your second number: \'))\n')

countNum1=0
countNum2=0
calculationLimit=50

while countNum1<=calculationLimit:
	if countNum2<=calculationLimit:
		countNum2=countNum2+1
	if countNum2==calculationLimit:
		countNum2=0
		countNum1=countNum1+1
	print(countNum1+countNum2)