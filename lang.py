"""
Russian Python - A Python-like language with Russian Keywords.
This is a rudimentary interpreter, not a full compiler. It translates
Russian keywords into valid Python code and then *executes* that Python code.
This approach has significant limitations, but it's a good way to demonstrate
the basic concept without building a full-blown compiler and virtual machine.

This project also has potential to translate any languages supported by UTF-8
into valid python code.

Key Design Choices:

-   **Interpreter, not Compiler:** This is easier to implement for a demo.
-   **Entire File Translation:** We process all the Russian code before executing.
-   **exec() for Execution:** After translating a line to Python, we use `exec()`
    to run it. `exec()` is powerful but can be dangerous with untrusted input.
    In a real language, you'd build an Abstract Syntax Tree (AST) and evaluate it.
-   **Limited Scope:** This interpreter supports only a subset of Python features.
-   **Global Namespace:**  We use a single global dictionary (`global_vars`) to
    store variables. This keeps things simple but would be problematic in a
    real language (no function-local scope, etc.).
-   **String handling** Strings are supported, so the rant is very functional.
"""

import re
import sys


def translate_line(line: str, global_vars: dict[str, None]) -> str | None:
	"""
	Translates a single line of Russian Python to standard Python.
	
	:param line: The line of Russian Python code.
	:param global_vars: The dictionary holding global variables.
	:return: The equivalent Python code, or None if the line should be skipped.
	:raise ValueError: If the Russian syntax is invalid.
	"""
	
	if not line:  # Skip empty lines
		return None
	
	translations: list[tuple[str, str]] = [
		('None', 'ничего'),
		('int', 'цел'),
		('float', 'вещ'),
		('str', 'стр'),
		('bool', 'бул'),
		('True', 'да'),
		('False', 'нет'),
		('if', 'если'),
		('else', 'иначе'),
		('while', 'пока'),
		('break', 'прервать'),
		('continue', 'продолжить'),
		('for', 'для'),
		('return', 'воз'),
		('print', 'печать'),
		('input', 'ввод'),
		('match', 'соп'),
		('try', 'поп'),
		('case', 'случай'),
		('raise', 'выб'),
		('def', 'функ'),
		
		(' not ', ' не '),
		(' and ', ' и '),
		(' or ', ' или '),
		
		(':', '{'),
		('', '}')
	]
	
	for eng, rus in translations:
		line = line.replace(rus, eng)
	
	# --- Function Definition (Very Basic) ---
	#   def my_function(arg1, arg2):
	match = re.match(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*)\)\s*:', line)
	if match:
		func_name = match.group(1)
		args_str = match.group(2).strip()
		return f'def {func_name}({args_str}):'
	
	# --- Return Statements (Limited) ---
	# We can't *really* handle return values properly without a full AST.
	# This is a VERY basic 'return' that works *only* at the top level
	# (outside of functions) and only for simple expressions.  It stores
	# the return value in a special variable.
	if line.startswith('return'):
		return_value_expression = line[len('return'):].strip()
		return f'__return_value__ = {return_value_expression}'
	
	return line


def run_rus_code(code: str) -> None:
	"""
	Executes Russian Python code.
	
	:param code: The Russian Code
	"""
	
	global_vars = {'__return_value__': None}  # Initialize the global namespace
	lines = code.split('\n')
	in_function_def = False
	translated_program = []
	
	for original_line in lines:
		translated_line = translate_line(original_line, global_vars)
		
		if translated_line is None:  # Skip empty or comment lines
			continue
		
		# --- Indentation Handling (Crucial for Python) ---
		# This is a *very* simplified indentation handler.  It assumes:
		# 1. Indentation is always consistent (e.g., always 4 spaces).
		# 2. There's no multi-line statements within blocks (which is illegal in Python anyway).
		leading_spaces = len(original_line) - len(original_line.lstrip())
		new_indent_level = leading_spaces // 4  # Assume 4 spaces per indent
		
		# --- Function Definition Indentation
		if translated_line.startswith('def'):
			in_function_def = True
			new_indent_level = 0
		
		if not in_function_def:
			# Adjust to be outside function defs
			new_indent_level = 0
		
		# Prepend the correct number of spaces for indentation
		translated_line = '    ' * new_indent_level + translated_line
		translated_program.append(translated_line)
	
	# --- Execute The Full Translated Program ---
	try:
		exec('\n'.join(translated_program), global_vars)
	except Exception as e:
		print(f'Error: {e}')
		return  # Stop on error
	
	# --- Print the "Return Value" (if any) ---
	if global_vars['__return_value__'] is not None:
		print(f'Returned: {global_vars['__return_value__']}')


def main():
	"""Main function: handles file input."""
	
	if len(sys.argv) > 1:
		# Read code from file
		filename = sys.argv[1]
		
		if not filename.endswith('.blyad'):
			print('Your Chosen File Is Not A .blyad File')
			return
		
		try:
			with open(filename, 'r', encoding='utf-8') as f:
				code = f.read()
			run_rus_code(code)
		except FileNotFoundError:
			print(f'Error: File not found: {filename}')
	
	else:  # TODO: remove later
		# Interactive mode
		print('Gen Alpha Python Interpreter (Interactive Mode)')
		print('Enter "exit" to quit.')
		code_buffer = []
		while True:
			try:
				line = input('> ')  # Prompt
				if line.strip().lower() == 'exit':
					break
				code_buffer.append(line)
				# Check if the entered line completes a block (very basic check)
				if line.strip().endswith(':'):
					# If colon start multi line statement
					continue
				else:
					# Run accumulated code if no more multi-line input is needed
					run_rus_code('\n'.join(code_buffer))
					code_buffer = []  # Reset Buffer
			except KeyboardInterrupt:
				print('\nExiting...')
				break
			except EOFError:
				print('\nExiting...')
				break


if __name__ == '__main__':
	main()
