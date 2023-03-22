# LexerForPascal
![11650986_1608213091](https://user-images.githubusercontent.com/107740684/226783574-28825e0e-22e1-46e5-a2bb-60db06776c86.jpg)

<h2>Pascal Lexer</h2>
	<p>This is a simple lexer for the Pascal programming language, implemented in Python. It reads a Pascal source code file, tokenizes it and outputs the resulting tokens.</p>
<h3>Installation</h3>
<p>You can simply download the <code>pascal_lexer.py</code> file and run it in your Python environment.</p>

<h3>Usage</h3>
<p>To use the lexer, run the <code>pascal_lexer.py</code> script and provide the path to the input Pascal file as an argument. For example:</p>
<pre><code>python pascal_lexer.py input_file.pas</code></pre>
<p>The output will be a list of tuples, where each tuple represents a token and its value.</p>

<h3>Token Types</h3>
<p>The lexer recognizes the following token types:</p>
<table>
	<tr>
		<th>Token Type</th>
		<th>Description</th>
	</tr>
	<tr>
		<td><code>VAR</code></td>
		<td>Variable declaration keyword</td>
	</tr>
	<tr>
		<td><code>PROGRAM</code></td>
		<td>Program declaration keyword</td>
	</tr>
	<tr>
		<td><code>BEGIN</code></td>
		<td>Beginning of program block</td>
	</tr>
	<tr>
		<td><code>END</code></td>
		<td>End of program block</td>
	</tr>
	<tr>
		<td><code>INTEGER</code></td>
		<td>Integer data type keyword</td>
	</tr>
	<tr>
		<td><code>REAL</code></td>
		<td>Real data type keyword</td>
	</tr>
	<tr>
		<td><code>BOOLEAN</code></td>
		<td>Boolean data type keyword</td>
	</tr>
	<tr>
		<td><code>CHAR</code></td>
		<td>Character data type keyword</td>
	</tr>
	<tr>
		<td><code>ARRAY</code></td>
		<td>Array declaration keyword</td>
	</tr>
<tr>
		<td><code>OF</code></td>
		<td>Array index keyword</td>
	</tr>
	<tr>
		<td><code>IF</code></td>
		<td>Conditional statement keyword</td>
	</tr>
	<tr>
		<td><code>THEN</code></td>
		<td>Keyword used after an if statement to indicate the block of code that should be executed if the condition is true</td>
	</tr>
	<tr>
		<td><code>ELSE</code></td>
		<td>Keyword used after an if statement to indicate the block of code that should be executed if the condition is false</td>
	</tr>
	<tr>
		<td><code>WHILE</code></td>
		<td>While loop keyword</td>
	</tr>
	<tr>
		<td><code>DO</code></td>
		<td>Keyword used after a while loop to indicate the block of code that should be executed while the condition is true</td>
	</tr>
	<tr>
		<td><code>REPEAT</code></td>
		<td>Repeat until loop keyword</td>
	</tr>
	<tr>
		<td><code>UNTIL</code></td>
		<td>Keyword used after a repeat loop to indicate the condition that should be checked before executing the block of code again</td>
	</tr>
	<tr>
		<td><code>FOR</code></td>
		<td>For loop keyword</td>
	</tr>
	<tr>
		<td><code>TO</code></td>
		<td>Keyword used after a for loop to indicate the upper bound of the loop</td>
	</tr>
	<tr>
		<td><code>DOWNTO</code></td>
		<td>Keyword used after a for loop to indicate the lower bound of the loop</td>
	</tr>
	<tr>
		<td><code>FUNCTION</code></td>
		<td>Function declaration keyword</td>
	</tr>
	<tr>
		<td><code>PROCEDURE</code></td>
		<td>Procedure declaration keyword</td>
	</tr>
	<tr>
		<td><code>NOT</code></td>
		<td>Logical not operator</td>
	</tr>
	<tr>
		<td><code>IDENTIFIER</code></td>
		<td>Name of a variable, function, or procedure</td>
	</tr>
	<tr>
		<td><code>NUMBER</code></td>
		<td>Integer or real number</td>
	</tr>
	<tr>
		<td><code>PLUS</code></td>
		<td>Addition operator</td>
	</tr>
	<tr>
		<td><code>MINUS</code></td>
		<td>Subtraction operator</td>
	</tr>
	<tr>
		<td><code>MULTIPLY</code></td>
		<td>Multiplication operator</td>
	</tr>
	<tr>
		<td><code>DIVIDE</code></td>
		<td>Division operator</td>
	</tr>
	<tr>
		<td><code>ASSIGN</code></td>
		<td>Assignment operator</td>
	</tr>
	<tr>
		<td><code>SEMICOLON</code></td>
		<td>Semicolon used to separate statements</td>
	</tr>
<tr>
		<td><code>LPAREN</code></td>
		<td>Left parenthesis</td>
	</tr>
	<tr>
		<td><code>RPAREN</code></td>
		<td>Right parenthesis</td>
	</tr>
	<tr>
		<td><code>DOT</code></td>
		<td>Dot symbol</td>
	</tr>
	<tr>
		<td><code>COMMA</code></td>
		<td>Comma symbol</td>
	</tr>
	<tr>
		<td><code>COLON</code></td>
		<td>Colon symbol</td>
	</tr>
	<tr>
		<td><code>ASSIGN</code></td>
		<td>Assignment operator</td>
	</tr>
	<tr>
		<td><code>SEMICOLON</code></td>
		<td>Semicolon symbol</td>
	</tr>
	<tr>
		<td><code>PLUS</code></td>
		<td>Addition operator</td>
	</tr>
	<tr>
		<td><code>MINUS</code></td>
		<td>Subtraction operator</td>
	</tr>
	<tr>
		<td><code>MULTIPLY</code></td>
		<td>Multiplication operator</td>
	</tr>
	<tr>
		<td><code>DIVIDE</code></td>
		<td>Division operator</td>
	</tr>
	<tr>
		<td><code>NOT</code></td>
		<td>Boolean negation operator</td>
	</tr>
	<tr>
		<td><code>IDENTIFIER</code></td>
		<td>Identifier (variable or function name)</td>
	</tr>
	<tr>
		<td><code>NUMBER</code></td>
		<td>Numeric literal value</td>
	</tr>
</table>

<h2 color=red>Errors</h2>
<p>If the <b>lexer</b> encounters an invalid variable name or integer value, it will raise a <code>SyntaxError</code> with a corresponding message.</p>
<h2>License</h2>
<p>This program is licensed under the MIT license.</p>
