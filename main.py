import re

# Define regular expressions for each token
regex_patterns = {
    'VAR': r'var',
    'PROGRAM': r'program',
    'BEGIN': r'begin',
    'END': r'end',
    'INTEGER': r'integer',
    'REAL': r'real',
    'BOOLEAN': r'boolean',
    'CHAR': r'char',
    'ARRAY': r'array',
    'OF': r'of',
    'IF': r'if',
    'THEN': r'then',
    'ELSE': r'else',
    'WHILE': r'while',
    'DO': r'do',
    'REPEAT': r'repeat',
    'UNTIL': r'until',
    'FOR': r'for',
    'TO': r'to',
    'FUNCTION': r'function',
    'PROCEDURE': r'procedure',
    'NOT': r'not',
    'IDENTIFIER': r'[a-zA-Z][a-zA-Z0-9_]*|(?<![0-9])[0-9]+[a-zA-Z_]+',
    'NUMBER': r'[0-9]+',
    'PLUS': r'\+',
    'MINUS': r'\-',
    'MULTIPLY': r'\*',
    'DIVIDE': r'\/',
    'ASSIGN': r':=',
    'SEMICOLON': r';',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'DOT': r'\.',
    'COMMA': r',',
    'COLON': r':',

}

# Combine all the regex patterns into one regular expression
token_regex = re.compile('|'.join('(?P<%s>%s)' % pair for pair in regex_patterns.items()))

KEY_WORDS = ['AND', 'ARRAY', 'BEGIN', 'BOOLEAN', 'CASE', 'CHAR', 'CONST', 'DIV',
             'DO', 'DOWNTO', 'ELSE', 'END', 'FILE', 'FOR', 'FUNCTION', 'GOTO', 'IF',
             'IN', 'INTEGER', 'LABEL', 'MOD', 'NIL', 'NOT', 'OF', 'OR', 'PACKED',
             'PROCEDURE', 'PROGRAM', 'REAL', 'RECORD', 'REPEAT', 'SET', 'THEN', 'TO',
             'TYPE', 'UNTIL', 'VAR', 'WHILE', 'WITH'
             ]


def tokenize(code):
    tokens = []
    line_number = 1
    for match in token_regex.finditer(code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type == 'IDENTIFIER':
            if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', token_value):
                raise ValueError(f'SyntaxError: Invalid variable name "{token_value}" on line {line_number}')
        elif token_type == 'NUMBER':
            if not re.match(r'^[0-9]+$', token_value):
                raise ValueError(f'SyntaxError: Invalid number "{token_value}" on line {line_number}')
            try:
                int_value = int(token_value)
            except ValueError:
                raise ValueError(f'SyntaxError: Invalid integer "{token_value}" on line {line_number}')
            if not -32768 <= int_value <= 32767:
                raise ValueError(f'ValueError: Integer overflow "{token_value}" on line {line_number}')
        elif token_type == 'SEMICOLON' or token_type in KEY_WORDS:
            line_number += 1
        tokens.append((token_type, token_value))
    return tokens


def main():
    with open('file.pas', 'r') as file:
        code = file.read()

    try:
        tokens = tokenize(code)
        for token in tokens:
            print(token)
    except ValueError as e:
        print('Error:', str(e))
        return

    print('Parsed successfully!')


if __name__ == '__main__':
    main()
