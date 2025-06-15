import re
from typing import List, Dict


def tokenize_expression(expression):
    token_specs = [
        ('constant', r'\b(pi|e|sqrt2|ln2|ln10)\b'),
        ('function', r'\b(sin|cos|tg|ctg|tan|cot|sinh|cosh|th|cth|tanh|coth|ln|lg|log|exp|sqrt|cbrt|abs|sign)\b'),
        ('number', r'\b\d+(\.\d*)?\b'),
        ('variable', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
        ('operator', r'[\+\-\*/^]'),
        ('left_parenthesis', r'\('),
        ('right_parenthesis', r'\)'),
        ('whitespace', r'\s+')
    ]

    token_re = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)
    token_pattern = re.compile(token_re)

    tokens = []
    for match in token_pattern.finditer(expression):
        token_type = match.lastgroup
        if token_type == 'whitespace':
            continue

        tokens.append({
            'type': token_type,
            'span': (match.start(), match.end())
        })

    return tokens


print(*tokenize_expression(input("Введите математическое выражение --> ")), sep="\n")