#Calculator

import pyperclip, sys

def main():
    print('Calculator HAHAAHHA (python version)\n')
    #choices
    print('Choose operation\n')
    print('\t1. Addition (+)')
    print('\t2. Substraction (-)')
    print('\t3. Multiplication (x)')
    print('\t4. Division (/)')
    print('\t5. Find remainder (%)')

    choice = input('Input choice: ')

    if choice == '1':
        calcAdd()
    elif choice == '2':
        calcSub()
    elif choice == '3':
        calcProduct()
    elif choice == '4':
        calcDivide()
    elif choice == '5':
        calcModulo()
    else:
        print('Invalid!')

    print()
    print('Answer has been copied to the clipboard')
    print()

    sys.exit()

def calcAdd():
    print('This operation will add two numbers together\n')
    firstNum = float(input('\tEnter first number: '))
    secondNum = float(input('\tEnter second number: '))
    hasil = firstNum + secondNum
    print('The value of ',firstNum,' + ',secondNum, 'is ',hasil)
    pyperclip.copy(hasil)

def calcSub():
    print('This operation will substract two numbers together\n')
    firstNum = float(input('\tEnter first number: '))
    secondNum = float(input('\tEnter second number: '))
    hasil = firstNum - secondNum
    print('The value of ', firstNum, ' - ', secondNum, 'is ', hasil)
    pyperclip.copy(hasil)

def calcProduct():
    print('This operation will multiply two numbers together')
    firstNum = float(input('\tEnter first number: '))
    secondNum = float(input('\tEnter second number: '))
    hasil = firstNum * secondNum
    print(f'The value of {firstNum} * {secondNum} is {hasil}')
    pyperclip.copy(hasil)

def calcDivide():
    print('This operation will divide two numbers together')
    firstNum = float(input('\tEnter first number: '))
    secondNum = float(input('\tEnter second number: '))
    hasil = firstNum / secondNum
    print(f'The value of {firstNum} * {secondNum} is {hasil}')
    pyperclip.copy(hasil)

def calcModulo():
    print('This operation will find remainder of two number divided')
    firstNum = float(input('\tEnter first number: '))
    secondNum = float(input('\tEnter second number: '))
    hasil = firstNum % secondNum
    print(f'The remainder of {firstNum} divided by {secondNum} is {hasil}')
    pyperclip.copy(hasil)

if __name__ == "__main__":
    main()