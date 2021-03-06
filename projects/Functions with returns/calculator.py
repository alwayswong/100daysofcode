import art

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

dict = {
            '+': add,
            '-': sub,
            '*': mult,
            '/': div,
}

print(art.logo)
num1 = float(input('What is the first number?'))
for operator in dict:
    print(operator)

while True:
    operation = input(f'Which operator do you want to use?')
    num2 = float(input('What is the next number?'))
    calculation = dict[operation]
    answer = calculation(num1,num2)
    print(f'{num1} {operation} {num2} = {answer}')
    cont = input('Do you want to continue (y/n)?').strip().lower()
    if cont == 'y':
        num1 = answer
    elif cont == 'n':
        break


    # operation = input('Pick another operation: ')
    # num3 = int(input('What is the third number?'))
    # calculation = dict[operation]
    # second_answer = calculation(first_answer,num3)
    # print(second_answer)




