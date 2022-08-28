
def calculator(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Вырожение должно содержать минимум один знак ({allowed})')
    for sing in allowed:
        if sing in expression:
            try:
                left, right = expression.split(sing)
                left, right = int(left), int(right)
                if sing == '+':
                    return left + right
                elif sing == '-':
                    return left - right
                elif sing == '*':
                    return left * right
                elif sing == '/':
                    return left / right
            except (ValueError, TypeError):
                raise ValueError('Вырожение должно содержать два целых числа и один знак')


if __name__ == "__main__":
    print(calculator('24/2'))