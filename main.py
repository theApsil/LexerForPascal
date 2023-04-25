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
    'WRITELN': r'writeln',
    'WRITE': r'write',
    'READLN': r'readln',
    'READ': r'read',
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
             'TYPE', 'UNTIL', 'VAR', 'WHILE', 'WITH', 'WRITELN', 'WRITE', 'READ', 'READLN'
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
                raise ValueError(f'SyntaxError: Invalid number "{token_value}" on line {line_number - 1}')
            try:
                int_value = int(token_value)
            except ValueError:
                raise ValueError(f'SyntaxError: Invalid integer "{token_value}" on line {line_number - 1}')
            if not -32768 <= int_value <= 32767:
                raise ValueError(f'ValueError: Integer overflow "{token_value}" on line {line_number - 1}')
        elif token_type == 'SEMICOLON' or token_type in KEY_WORDS:
            line_number += 1
        tokens.append((token_type, token_value))
    return tokens


import unittest


class TestLexer(unittest.TestCase):
    def test_empty_input(self):
        code = ''
        expected_tokens = []
        self.assertEqual(tokenize(code), expected_tokens)

    def test_single_identifier(self):
        code = 'foo'
        expected_tokens = [('IDENTIFIER', 'foo')]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_single_integer(self):
        code = '123'
        expected_tokens = [('NUMBER', '123')]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_single_float(self):
        code = '3.14159'
        expected_tokens = [('NUMBER', '3.14159')]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_single_string(self):
        code = "'hello, world'"
        expected_tokens = [('STRING', "'hello, world'")]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_invalid_identifier(self):
        code = '123foo'
        with self.assertRaises(ValueError):
            tokenize(code)

    def test_integer_overflow(self):
        code = '32768'
        with self.assertRaises(ValueError):
            tokenize(code)

    def test_valid_keywords(self):
        code = 'program begin end if then else while do repeat until for to function procedure var integer real boolean char array of read readln write writeln'
        expected_tokens = [('PROGRAM', 'program'),
                           ('BEGIN', 'begin'),
                           ('END', 'end'),
                           ('IF', 'if'),
                           ('THEN', 'then'),
                           ('ELSE', 'else'),
                           ('WHILE', 'while'),
                           ('DO', 'do'),
                           ('REPEAT', 'repeat'),
                           ('UNTIL', 'until'),
                           ('FOR', 'for'),
                           ('TO', 'to'),
                           ('FUNCTION', 'function'),
                           ('PROCEDURE', 'procedure'),
                           ('VAR', 'var'),
                           ('INTEGER', 'integer'),
                           ('REAL', 'real'),
                           ('BOOLEAN', 'boolean'),
                           ('CHAR', 'char'),
                           ('ARRAY', 'array'),
                           ('OF', 'of'),
                           ('READ', 'read'),
                           ('READLN', 'readln'),
                           ('WRITE', 'write'),
                           ('WRITELN', 'writeln')]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_invalid_keywords(self):
        code = 'begin2 end4 if-then while_2 do# repeat^until 5for goto'
        with self.assertRaises(ValueError):
            tokenize(code)

    def test_multiple_tokens(self):
        code = 'var x : integer ; x := 42 ; writeln (            x )'
        expected_tokens = [('VAR', 'var'),
                           ('IDENTIFIER', 'x'),
                           ('COLON', ':'),
                           ('INTEGER', 'integer'),
                           ('SEMICOLON', ';'),
                           ('IDENTIFIER', 'x'),
                           ('ASSIGN', ':='),
                           ('NUMBER', '42'),
                           ('SEMICOLON', ';'),
                           ('WRITELN', 'writeln'),
                           ('LPAREN', '('),
                           ('IDENTIFIER', 'x'),
                           ('RPAREN', ')')]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_simple_assignment(self):
        code = "x := 10;"
        expected_tokens = [
            ('IDENTIFIER', 'x'),
            ('ASSIGN', ':='),
            ('NUMBER', '10'),
            ('SEMICOLON', ';')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_variable_declaration(self):
        code = "var x: integer;"
        expected_tokens = [
            ('VAR', 'var'),
            ('IDENTIFIER', 'x'),
            ('COLON', ':'),
            ('INTEGER', 'integer'),
            ('SEMICOLON', ';')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_function_declaration(self):
        code = "function add(a, b: integer): integer;\nbegin\n  add := a + b;\nend;"
        expected_tokens = [
            ('FUNCTION', 'function'),
            ('IDENTIFIER', 'add'),
            ('LPAREN', '('),
            ('IDENTIFIER', 'a'),
            ('COMMA', ','),
            ('IDENTIFIER', 'b'),
            ('COLON', ':'),
            ('INTEGER', 'integer'),
            ('RPAREN', ')'),
            ('COLON', ':'),
            ('INTEGER', 'integer'),
            ('SEMICOLON', ';'),
            ('BEGIN', 'begin'),
            ('IDENTIFIER', 'add'),
            ('ASSIGN', ':='),
            ('IDENTIFIER', 'a'),
            ('PLUS', '+'),
            ('IDENTIFIER', 'b'),
            ('SEMICOLON', ';'),
            ('END', 'end'),
            ('SEMICOLON', ';')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_invalid_variable_name(self):
        code = "2x := 10;"
        with self.assertRaises(ValueError):
            tokenize(code)

    def test_invalid_number(self):
        code = "x := 1.2;"
        with self.assertRaises(ValueError):
            tokenize(code)

    def test_single_line_comment(self):
        code = "x := 5; {this is a comment} y := 7;"
        expected_tokens = [
            ('IDENTIFIER', 'x'),
            ('ASSIGN', ':='),
            ('NUMBER', '5'),
            ('SEMICOLON', ';'),
            ('IDENTIFIER', 'y'),
            ('ASSIGN', ':='),
            ('NUMBER', '7'),
            ('SEMICOLON', ';')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_multi_line_comment(self):
        code = """
            (*
            This is a
            multi-line
            comment
            *)
            x := 5;
        """
        expected_tokens = [
            ('IDENTIFIER', 'x'),
            ('ASSIGN', ':='),
            ('NUMBER', '5'),
            ('SEMICOLON', ';')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_identifier(self):
        code = 'x y1 _z abc_123'
        tokens = tokenize(code)
        expected_tokens = [('IDENTIFIER', 'x'),
                           ('IDENTIFIER', 'y1'),
                           ('IDENTIFIER', '_z'),
                           ('IDENTIFIER', 'abc_123')]
        self.assertEqual(tokens, expected_tokens)

    def test_invalid_identifier2(self):
        code = '1x abc.def'
        with self.assertRaises(ValueError) as cm:
            tokenize(code)
        self.assertEqual(str(cm.exception), 'SyntaxError: Invalid variable name "1x" on line 1')

        code = 'x.y'
        with self.assertRaises(ValueError) as cm:
            tokenize(code)
        self.assertEqual(str(cm.exception), 'SyntaxError: Invalid variable name "x.y" on line 1')

    def test_number(self):
        code = '123 456'
        tokens = tokenize(code)
        expected_tokens = [('NUMBER', '123'),
                           ('NUMBER', '456')]
        self.assertEqual(tokens, expected_tokens)

    def test_invalid_number2(self):
        code = '1.23'
        with self.assertRaises(ValueError) as cm:
            tokenize(code)
        self.assertEqual(str(cm.exception), 'SyntaxError: Invalid number "1.23" on line 1')

        code = '999999999999999999999999999999999999999999999999999999999999999'
        with self.assertRaises(ValueError) as cm:
            tokenize(code)
        self.assertEqual(str(cm.exception),
                         'ValueError: Integer overflow "999999999999999999999999999999999999999999999999999999999999999" on line 1')

    def test_keywords(self):
        code = 'begin while do end if then else'
        tokens = tokenize(code)
        expected_tokens = [('BEGIN', 'begin'),
                           ('WHILE', 'while'),
                           ('DO', 'do'),
                           ('END', 'end'),
                           ('IF', 'if'),
                           ('THEN', 'then'),
                           ('ELSE', 'else')]
        self.assertEqual(tokens, expected_tokens)

    def test_operators(self):
        code = '+ - * / := ; ( ) . , :'
        tokens = tokenize(code)
        expected_tokens = [('PLUS', '+'),
                           ('MINUS', '-'),
                           ('MULTIPLY', '*'),
                           ('DIVIDE', '/'),
                           ('ASSIGN', ':='),
                           ('SEMICOLON', ';'),
                           ('LPAREN', '('),
                           ('RPAREN', ')'),
                           ('DOT', '.'),
                           ('COMMA', ','),
                           ('COLON', ':')]
        self.assertEqual(tokens, expected_tokens)


if __name__ == '__main__':
    unittest.main()

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
