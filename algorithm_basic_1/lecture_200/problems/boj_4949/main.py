from sys import stdin


def validate_parens(sentence: str) -> str:
    left_parens: list = []
    for ch in sentence:
        if ch in '([':
            left_parens.append(ch)
        elif ch == ')':
            if not left_parens or left_parens.pop() != '(':
                return 'no'
        elif ch == ']':
            if not left_parens or left_parens.pop() != '[':
                return 'no'

    return 'yes' if not left_parens else 'no'


def sol(sentences: list) -> str:
    return '\n'.join([validate_parens(sentence) for sentence in sentences])


print(sol(stdin.readlines()[:-1]))
