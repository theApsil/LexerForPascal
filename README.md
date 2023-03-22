# LexerForPascal
Pascal Lexer
This is a simple lexer for the Pascal programming language, implemented in Python. It reads a Pascal source code file, tokenizes it and outputs the resulting tokens.

Installation
You can simply download the pascal_lexer.py file and run it in your Python environment.

Usage
To use the lexer, run the pascal_lexer.py script and provide the path to the input Pascal file as an argument. For example:

Copy code
python pascal_lexer.py input_file.pas
The output will be a list of tuples, where each tuple represents a token and its value.

Token Types
The lexer recognizes the following token types:

VAR
PROGRAM
BEGIN
END
INTEGER
REAL
BOOLEAN
CHAR
ARRAY
OF
IF
THEN
ELSE
WHILE
DO
REPEAT
UNTIL
FOR
TO
DOWNTO
FUNCTION
PROCEDURE
NOT
IDENTIFIER
NUMBER
PLUS
MINUS
MULTIPLY
DIVIDE
ASSIGN
SEMICOLON
LPAREN
RPAREN
DOT
COMMA
COLON
Error Handling
If the lexer encounters an invalid variable name or integer value, it will raise a SyntaxError with a corresponding message.

License
This program is licensed under the MIT license.
