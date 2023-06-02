import re
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def isEmpty(string: str):
    return len(string) == 0

def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid

def Calculate(number1, number2, opr_escolhido):
    if opr_escolhido == '+':
        return float(number1) + float(number2)
    elif opr_escolhido == '-':
        return float(number1) - float(number2)
    elif opr_escolhido == '*':
        return float(number1) * float(number2)
    elif opr_escolhido == '/':
        return float(number1) / float(number2)
    elif opr_escolhido == '**':
        return float(number1) ** float(number2)
    elif opr_escolhido == '%':
        return float(number1) % float(number2)
    else:
        print('nao era pra ter chegado aq')
        return