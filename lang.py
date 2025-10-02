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
import os


def translate_line(line: str) -> str | None:
	"""
	Translates a single line of Russian Python to standard Python.
	
	:param line: The line of Russian Python code.
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
		('in', 'в'),
		('range', 'диапазон'),
		
		(' not ', ' не '),
		(' and ', ' и '),
		(' or ', ' или '),
		
		(':', '{'),
		('', '}')
	]
	
	for eng, rus in translations:
		line = line.replace(rus, eng)
	
	# Function Definition
	# def my_function(arg1, arg2):
	match = re.match(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*)\)\s*:', line)
	if match:
		func_name = match.group(1)
		args_str = match.group(2).strip()
		return f'def {func_name}({args_str}):'
	
	return line


def run_rus_code(code: str) -> str:
	"""
	Executes Russian Python code.
	
	:param code: The Russian Code
	"""
	
	lines = code.split('\n')
	translated_program = []
	
	for original_line in lines:
		translated_line = translate_line(original_line)
		
		if translated_line is None:  # Skip empty or comment lines
			continue
		
		translated_program.append(translated_line)
	
	# Execute The Full Translated Program
	try:
		exec('\n'.join(translated_program))
	except Exception as e:
		raise Exception(e)
	finally:
		return '\n'.join(translated_program)


def main():
	"""Main function: handles file input."""
	
	if len(sys.argv) > 1:
		# Read code from file
		filename = sys.argv[1]
		
		if not filename.endswith('.blyad'):
			raise FileNotFoundError('Your Chosen File Is Not A .blyad File')
		
		try:
			with open(filename, 'r', encoding='utf-8') as f:
				code = f.read()
			python_program = run_rus_code(code)
			
			if len(sys.argv) == 3 and sys.argv[2] == '--debug':
				if not os.path.exists('debug'):
					os.makedirs('debug')
				
				with open(
						f'debug/{filename.removesuffix('.blyad')}.py', 'w',
						encoding='utf-8'
				) as f:
					f.write(python_program)
		except FileNotFoundError:
			raise FileNotFoundError(f'Error: File not found: {filename}')


if __name__ == '__main__':
	main()
