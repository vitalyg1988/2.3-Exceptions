def user_input():
    math_input = input('Введите знак математической операции, а затем два числа через пробел: ').split()
    math_list = [math_input[0]]
    for value in math_input[1:]:
        assert '-' not in value, 'AssertionError: Числа должны быть положительными'
        try:
            if '.' in value:
                math_list.append(float(value))
            else:
                math_list.append(int(value))
        except ValueError as error:
            print(error)
    return math_list


def summ(first_num, second_num):
    print(first_num + second_num)


def subtraction(first_num, second_num):
    print(first_num - second_num)


def multiplication(first_num, second_num):
    print(first_num * second_num)


def division(first_num, second_num):
    try:
        print(first_num / second_num)
    except ZeroDivisionError as error:
        print(error)


def main_func():
    try:
        math_operation = user_input()
        assert (len(math_operation)) == 3, 'Недопустимое количество знаков/чисел!'
        assert math_operation[0] in ('+', '-', '*', '/'), 'AssertionError: Недопустимая математическая операция'
        if math_operation[0] == '+':
            summ(math_operation[1], math_operation[2])
        elif math_operation[0] == '-':
            subtraction(math_operation[1], math_operation[2])
        elif math_operation[0] == '*':
            multiplication(math_operation[1], math_operation[2])
        elif math_operation[0] == '/':
            division(math_operation[1], math_operation[2])
    except AssertionError as error:
        print(error)


if __name__ == '__main__':
    print('"Реализация Польской Нотации"')
    main_func()